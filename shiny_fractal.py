#shiny_fractal

#download_fractal
import pygame as pg
import numba
import numpy as np
import math
#import sympy
import time
import os

#i = sympy.I

global scr
scr = 10

pg.init()

start_time=time.time()
time_counted=False

def pixel2fractal(x,y):
  return x/breite*(x2-x1), y/höhe*(y2-y1)

za=0
zb=0
o=2
f1=1
g1=1
f=complex(f1,0)
g=complex(g1,0)
k=1

menu=-1

def zoomer_plus():
  global zoom
  zoom = zoom - 2*zoom/10

def zoomer_minus():
  global zoom
  zoom = zoom + 2*zoom/10 

zoom=1
modus=1
inv=1

@numba.jit(fastmath=True, parallel=True)
def zeichne_fractal(x1,x2,y1,y2,fractal,max_iter,za,zb,f1,g1,o,k):
  x_s = (x2-x1)/breite
  y_s = (y2-y1)/höhe
  
  for x in numba.prange(breite):
    for y in range(höhe):
      c = complex(x1+x*x_s,y1+y*y_s)
      #z = 0
      z = complex(za, zb)
      for i in range(max_iter):
        f=complex(f1,0)
        g=complex(g1,0)
        zRe = f*complex(z.real,0)
        zIm = g*complex(0,z.imag)
        
        if modus == 1:
          z = (zRe+zIm)**(math.floor(10*o)/10)/k + c
        if modus == 2:
          z = f*math.tan(z.real)+g*math.tan(z.imag)+(zRe+zIm)**(math.floor(10*o)/10)/k + c
        if modus == 3:
          z = f1*math.tan(z.real)+g1*math.tan(z.imag)+((f1+1)*z.real+zIm)**(math.floor(10*o)/10)/k + c 
        if modus == 4:
          z = f1*math.sin(z.real)-g1*math.tan(z.imag)+((f1+1)*z.real+zIm)**(math.floor(10*o)/10)/k + c
        if modus == 5:
          z = -f1*math.sin(z.real)+(zRe+zIm)**(math.floor(10*o)/10)/k + c
        #z = z.imag**2 + z.real**2 + c
        #z = z**2 + c
        #z = z.imag*z-(z.imag+z.real)**2 + c
        #z = (z.real + z.imag)**2 + c # math.sin(z.imag)**3
        #z = (sympy.re(z) + sympy.im(z))**2 + c
        #z = z**2/2 + c   
           
        if z.real**2 + z.imag**2 > 4: break
      fractal[x][y] = farben[i]
  return fractal   

größe = breite, höhe = 1050,700
fenster = pg.display.set_mode(größe,pg.SCALED)
clock = pg.time.Clock()
time_sum=0

x1,x2,y1,y2 = -2,1,-1,1
fractal = np.full((breite, höhe, 3), (0,0,0), dtype=np.uint8)
farben = np.full((20000, 3), (0,0,0), dtype=np.uint8)
verschiebe = False
max_iter = 100

def color_calc():
  for i in range(20000):
    r = int((0.5 * math.sin(0.1 * i +2.094) + 0.5) * 255)
    g = int((0.5 * math.sin(0.1 * i +4.188) + 0.5) * 255)
    b = int((0.5 * math.sin(0.1 * i) + 0.5) * 255)
    farben[inv*i] = (r,g,b)
color_calc()

while True:
    if modus == 1:
      formula = ("z = (f*zRe+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c           z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
    if modus == 2:
      formula = ("z = f*tan(zRe)+g*tan(zIm)+(f*zRe+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
    if modus == 3:
      formula = ("z = f*tan(zRe)+g*tan(zIm)+((f+1)*tan(zRe)+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
    if modus == 4:
      formula = ("z = f*sin(zRe)+g*sin(zIm)+((f+1)*zRe+zIm)**e/k + c"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
    if modus == 5:
      formula = ("z = -f*sin(zRe)+(zRe+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
    if menu == -1:
      formula += ("\n"
                  "\n"
                  "\n"
                  "\n"
                  "\n")
    if menu == 1:
      formula += "      "
    formula += str("maximum iterations = "+str(max_iter))
    if menu == 1:
      formula += str("        zoom factor: "+str(1/zoom))
      formula += str("\n"+"\n"+"\n"+"\n"
                     "controls: "+"\n"
                     "\n"
                     "[x] zoom in"+"\n"
                     "\n"
                     "[y] zoom out"+"\n"
                     "\n"
                     "[v] seed z(+0.2,0)        [1] g - 1     g:"+str(g1)+"\n"
                     "\n"
                     "[c] seed z(-0.2,0)         [2] g + 1"+"\n"
                     "\n"
                     "[f] seed z(0,+0.2)         [3] f - 1     f:"+str(f1)+"\n"
                     "\n"
                     "[d] seed z(0,-0.2)         [4] f + 1"+"\n"
                     "\n"
                     "[7] k - 1     k:"+str(math.floor(k*10)/10)+"           [5] o - 1 "+"\n"
                     "\n"
                     "[8] k + 1           o:"+str(o)+"       [6] o + 1 "+"\n"
                     "\n"
                     "[i] maximum iterations + 20 "+"\n"
                     "\n"
                     "[u] maximum iterations - 20 "+"\n"
                     "\n"
                     "[r] reset                        [o] invert colors"+"\n"
                     "\n"
                     "[s] save image            [p] switch formula"+"\n"
                     "\n"
                     "[arrowkeys] move "+"\n")
    clock.tick()
    for ereignis in pg.event.get():
        if ereignis.type == pg.QUIT or \
           ereignis.type == pg.KEYDOWN and ereignis.key == pg.K_ESCAPE:
          quit()
        if ereignis.type == pg.MOUSEBUTTONDOWN and not verschiebe:
          if pg.mouse.get_pressed()[0]:
            mx, my = pg.mouse.get_pos()
            verschiebe = True
        if verschiebe and ereignis.type != pg.MOUSEBUTTONUP:
          mx2, my2 = pg.mouse.get_pos()
          dx, dy = pixel2fractal(mx2-mx, my2-my)
          x1 -= dx; x2 -= dx; y1 -= dy; y2 -= dy
          mx, my = mx2, my2
        if verschiebe and ereignis.type == pg.MOUSEBUTTONUP:
          verschiebe = False
        if ereignis.type == pg.KEYDOWN:
          if ereignis.key == pg.K_y:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 -= dx; x2 += dx; y1 -= dy; y2 += dy
            zoomer_minus()
            time_counted = False
          if ereignis.key == pg.K_x:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 += dx; x2 -= dx; y1 += dy; y2 -= dy
            zoomer_plus()
            time_counted = False
          if ereignis.key == pg.K_LEFT:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 -= dx; x2 -= dx 
            time_counted = False
          if ereignis.key == pg.K_RIGHT:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 += dx; x2 += dx
            time_counted = False
          if ereignis.key == pg.K_UP:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            y1 -= dy; y2 -= dy
            time_counted = False
          if ereignis.key == pg.K_DOWN:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            y1 += dy; y2 += dy
            time_counted = False
          if ereignis.key == pg.K_i:
            max_iter += 20
            time_counted = False
          if ereignis.key == pg.K_u:
            max_iter -= 20
            time_counted = False
          if ereignis.key == pg.K_c:
            za-=0.1
            time_counted = False
          if ereignis.key == pg.K_v:
            za+=0.1
            time_counted = False
          if ereignis.key == pg.K_d:
            zb-=0.1
            time_counted = False
          if ereignis.key == pg.K_f:
            zb+=0.1
            time_counted = False
          if ereignis.key == pg.K_o:
            inv*=-1
            #farben = np.full((20000, 3), (0,0,0), dtype=np.uint8)
            color_calc()
            time_counted = False
          if ereignis.unicode == '5':
            o-=0.1
            if o<1:
              o=0.1
            time_counted = False
          if ereignis.unicode == '6':
            o+=0.1
            time_counted = False
          if ereignis.unicode == '3':
            f1-=0.1
            time_counted = False
          if ereignis.unicode == '4':
            f1+=0.1
            time_counted = False
          if ereignis.unicode == '1':
            g1-=0.1
            time_counted = False
          if ereignis.unicode == '2':
            g1+=0.1
            time_counted = False
          if ereignis.unicode == '7':
            k-=0.2
            if k==0:
              k=-0.2
            time_counted = False
          if ereignis.unicode == '8':
            k+=0.2
            if k==0:
              k=0.2
            time_counted = False
          if ereignis.key == pg.K_m:
            menu*=-1
          if ereignis.key == pg.K_p:
            modus += 1
            if modus == 6:
              modus = 1
          if ereignis.key == pg.K_s:
            screenshot = pg.Surface((1200, 700))
            screenshot.blit(fenster, (0, 0))
            while scr<1000:
              filename = str("frac_"+str(scr)+".png")
              if os.path.exists(filename):
                scr+=1
              else:
                filename = str("frac_"+str(scr)+".png")
                pg.image.save(screenshot, filename) 
                print("saved.") 
                break 
          if ereignis.key == pg.K_r:
            time_counted = False
            x1,x2,y1,y2 = -2,1,-1,1
            fractal = np.full((breite, höhe, 3), (0,0,0), dtype=np.uint8)
            farben = np.full((20000, 3), (0,0,0), dtype=np.uint8)
            verschiebe = False
            max_iter = 100   
            za = 0
            zb = 0
            o = 2
            f1=1
            g1=1
            k=1
            print("reset")
    
    if time_counted == False:
      start_time = time.time()
    fractal = zeichne_fractal(x1,x2,y1,y2,fractal,max_iter,za,zb,f1,g1,o,k)

    # Render and draw text
    font = pg.font.Font(None, 17)  # Choose a font and size
    if menu ==1:
      font = pg.font.Font(None, 27)

    pg.surfarray.blit_array(fenster,fractal)   
    # Draw the formula
    formula1 = font.render(formula, True, (0,0,0))  # Render the formula text
    formula_rect = formula1.get_rect(topleft=(10, 10))  # Position the formula text
    fenster.blit(formula1, formula_rect) 
    #pg.image.save(fenster, str("out.png"))
    if time_counted == False:
      end_time=time.time()
      calculation_time=end_time-start_time
      time_counted=True 
    calc = font.render(str("calculation time: " + str(calculation_time) + " seconds"), True, (0,0,0))
    time_rect = calc.get_rect(topleft=(10, 40))
    fenster.blit(calc, time_rect) 
    pg.display.flip()
    pg.display.set_caption(f'FPS = {clock.get_fps():.1f} iterations = {max_iter:,.0f}')    # formula = {formula}