#another_shiny_fractal

import pygame as pg
import numba
import numpy as np
import math
import time
import os
import random

'''
###################################################################
controls:

[x] zoom in
[y] zoom out
[v] seed z(+,0)         [1] g -
[c] seed z(-,0)         [2] g + 
[f] seed z(0,+)         [3] f - 
[d] seed z(0,-)         [4] f + 
[5] o - 
[6] o +     f(z)**o/k
[7] k -  
[8] k +       
[9] cc +  {-2;2}
[0] cci + {-2i;2i}
[#] cz [on/off]{+/-}  
[u] maximum iterations -  
[i] maximum iterations +         
[ö] precision - 
[ä] precision + 
[r] reset                        
[m] control menu
[o|k|j] change colors       (1;9,random)
[s] save image            
[p|l] switch formula        (-4;15)
[arrowkeys] move       
[a] rotate
[space] toggle surf mode
[+] modulo stripes          (0,1,2,3)
[-] colorshift              (0,1,2)
[,] sound on/off
[.] inner squircle          (0,1,2,3,4,5,6,7)
[ü] specialmode             (0,1,2,3) 
[q] zoom outomat
[leftmouse] trace
[rightmouse] trace on/off

[p/l|o/k/j|-|+|.|ü|ö/ä|space]
###################################################################
'''

pg.init()
pg.mixer.init()

start_time=time.time()
time_counted=False

def sound_x():
    pg.mixer.music.load("c:/Users/eks/Desktop/python/fractal_video_maker/sound.mp3")
    pg.mixer.music.play()

def pixel2fractal(x,y):
  return x/breite*(x2-x1), y/höhe*(y2-y1)

za = 0 #0.01
zb = 0 #0.02
o = 2
f1 = 1 #1.2
g1 = 1 #0.7
f = complex(f1,0)
g = complex(g1,0)
k = 1      
stopstop = True     # surf mode
rounder = 1         # precision
redline = False     # green modulo lines on/off
menu = -1           # info
zoom = 1    
#modus=random.randint(-4,11)
modus = 7           # formula 
inv = 1             
mod7 = 1            # green modulo lines
smallline = 7       # inner squircle
smalll = False      # inner squircle on/off
global scr
scr = 10            # start value for naming saved pictures
specialmode = 0 
bw = 0              # [0/1]  
cz = 0              # [0/1/2]
cc = -1             #              
cci = 0

fullscreen = True
if fullscreen == True:
  screen_info = pg.display.Info()
  breite = screen_info.current_w
  höhe = screen_info.current_h
else:
  breite = 1050
  höhe = 700
größe = breite, höhe
fenster = pg.display.set_mode(größe,pg.SCALED)
clock = pg.time.Clock()
time_sum=0

x1,x2,y1,y2 = -2,1,-1,1
fractal = np.full((breite, höhe, 3), (0,0,0), dtype=np.uint8)
farben = np.full((20000, 3), (0,0,0), dtype=np.uint8)
verschiebe = False
max_iter = 30

test = False
if test == True:         # (-0.7+0.5i)
  specialmode = 1
  za = 0 # 0.2 
  zb = 0 # -0.1
  cz = 1              
  cc = 0.4 # -0.9              
  cci = 0 # -0.2

notrace = True
traces = []
traces_out = []
#@numba.jit(nopython=True,fastmath=True, parallel=True)
def trace2(t1,t2):
  traces = []
  traces_out = []
  tracer = 1
  zz = complex(t1/breite,t2/höhe)
  x_s = (x2-x1)/breite
  y_s = (y2-y1)/höhe
  c = complex(x1+t1*x_s,y1+t2*y_s)
  while tracer < max_iter:
    if (zz.real+zz.imag)**2 > 7:
      break
    zz = zz**2 + c 
    #print(zz)
    traces.append(zz)
    tracer += 1
  for _ in traces:
    traces_out.append((_.real*breite,float(_.imag*höhe)))
  print(traces)
  print(traces_out)
  return traces_out

def trace(t1, t2, cc, cci,x1,x2,y1,y2):
  global traces_out
  traces_out = [(t1,t2)]
  traces = []
  # Coordinate scaling
  x_scale = (x2 - x1) / breite
  y_scale = (y2 - y1) / höhe
  # Complex starting point (mapped to fractal coordinates)
  c = complex(x1 + t1 * x_scale, y1 + t2 * y_scale)
  if cz == 1 or cz == 2:
    c = complex(cc,cci)
  #zz = 0  # or maybe zz = c for Julia sets
  if cz != 0:
    zz = c
  else:
    zz = 0
  zz = complex(x1 + t1 * x_scale, y1 + t2 * y_scale)
  for _ in range(max_iter):
      if (zz.real**2 + zz.imag**2) > 4:
          break
      zz = zz**2 + c
      # map to screen coordinates
      sx = int((zz.real - x1) / (x2 - x1) * breite)
      sy = int((zz.imag - y1) / (y2 - y1) * höhe)
      sy = höhe - sy  # invert Y
      traces_out.append((sx, sy))
  return traces_out

trace(500,200, cc, cci,x1,x2,y1,y2)

def zoomer_plus():
  global zoom
  zoom = zoom - 2*zoom/10

def zoomer_minus():
  global zoom,outomat
  zoom = zoom + 2*zoom/10

#def zoom_to_loc():

#@numba.jit(nopython=True)
#def complex_log(z):
#    """Compute the logarithm of a complex number manually."""
#    abs_z = np.sqrt(z.real ** 2 + z.imag ** 2)  # |z|
#    arg_z = np.arctan2(z.imag, z.real)  # angle
#    return (np.log(abs_z), arg_z)  # Returns log(|z|) and arg(z)

@numba.jit(nopython=True,fastmath=True, parallel=True)
def zeichne_fractal(x1,x2,y1,y2,fractal,max_iter,za,zb,f1,g1,o,k,modus,farben,mod7,smallline,specialmode,cc,cci,cz):
  #global traces_out
  #traces_out = [(t1,t2)]
  #traces = []
  #if specialmode == 2 or specialmode == 3:
  #  f1 = round(f1,rounder)
  #  g1 = round(g1,rounder)
    #za = round(za,rounder)
    #zb = round(zb,rounder)
  x_s = (x2-x1)/breite
  y_s = (y2-y1)/höhe

  #if specialmode == 2 or specialmode == 3:
  if rounder != 1:
    f = complex(round(f1,rounder),0)
    g = complex(round(g1,rounder),0)
  else:
    f = complex(f1,0)
    g = complex(g1,0)
  
  for x in numba.prange(breite):
    for y in range(höhe):
      redline = False
      smalll = False
      bw = 0
      #z = 0
      if cz == 1 or cz == 2:
        c = complex(cc,cci)
        z = complex(x1+x*x_s,y1+y*y_s)
      else:
        c = complex(x1+x*x_s,y1+y*y_s)
        z = complex(za, zb)
      for i in range(max_iter):
        '''
        if round != 1...
        specialmode 0: no round, direct
        specialmode 1: no round, indirect
        specialmode 2: round, direct 
        specialmode 3: round, indirect
        '''
        if modus == 11:
          if specialmode == 0:
            zRe = f*complex(z.real,0)
            zIm = g*complex(0,z.imag)
          if specialmode == 1:
            zRe = f*complex(z.real,0)
            zIm = g*complex(0,math.sin(z.imag))
          if specialmode == 2:
            zRe = f*complex(math.sin(z.real),0)
            zIm = g*complex(0,z.imag)
          if specialmode == 3:
            zRe = f*complex(math.sin(z.real),0)
            zIm = g*complex(0,math.tan(z.imag))
        elif modus == 12:
          if specialmode == 0:
            zRe = f*complex(z.real**2-z.real-z.imag,0)
            zIm = g*complex(0,z.imag)
          if specialmode == 1:
            zRe = f*complex(math.tan(math.sin(z.real)),0)
            zIm = g*complex(0,math.tan(math.sin(z.imag)))
          if specialmode == 2:
            zRe = f*complex(math.tan(math.sin(z.real)),0)
            zIm = g*complex(0,math.sin(z.imag))
          if specialmode == 3:
            zRe = f*complex(math.sin(z.real),0)
            zIm = g*complex(0,math.tan(math.sin(z.imag)))
        elif modus == 13:
          if specialmode == 0:
            zRe = f*complex(math.sin(z.real),0)
            zIm = g*complex(0,math.cos(z.imag))
          if specialmode == 1:
            zRe = f*complex(z.real,0)
            zIm = g*complex(0,math.tan(math.sin(z.imag)))
          if specialmode == 2:
            zRe = f*complex(math.tan(math.sin(z.real)),0)
            zIm = g*complex(0,z.imag)
          if specialmode == 3:
            zRe = f*complex(math.tan(z.real),0)
            zIm = g*complex(0,z.imag)
        elif modus == 8:
          if specialmode == 0:
            zRe = f*complex(z.imag,0)
            zIm = g*complex(0,z.real)
          if specialmode == 1:
            zRe = f*complex(z.real**2,0)
            zIm = g*complex(0,z.imag**2)
          if specialmode == 2:
            zRe = f*complex(math.tan(z.imag),0)
            zIm = g*complex(0,z.imag)
          if specialmode == 3:
            zRe = f*complex(math.sin(z.real),0)
            zIm = g*complex(0,z.imag)
        elif modus == 10:
          if specialmode == 2:
            zRe = f*complex(math.tan(z.real)*z.imag,0)
            zIm = g*complex(0,z.real/math.log(z.imag))
          if specialmode == 3:
            zRe = f*complex(math.tan(z.real)*z.real,0)
            zIm = g*complex(0,z.imag/math.log(z.imag))
        else:
          zRe = f*complex(z.real,0)
          zIm = g*complex(0,z.imag)

        if modus == -4:
          z = f*z.real+g*math.sin(math.tan(z.imag))+(zRe+zIm)**round(o,4)/k + c
        if modus == -3:
          z = (zRe+zIm)**(round(o,4))/k + c
        if modus == -2:
          z =  (f*z.real-math.sin(y/1000)*g*z.imag)**(round(o,4))+(f*zRe+g*zIm)*k + c
        if modus == -1:
          z =  (z.real+z.imag)**2-(zRe+zIm)**2 + c 
        if modus == 0:
          z = f*math.tan(z.real)+(zRe+zIm)**(round(o,4))/k + c
        if modus == 1:
          z = (zRe+zIm)**(round(o,4))/k + c
        if modus == 2:
          if specialmode == 0:
            z = f1*math.tan(z.real)+g1*math.tan(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c
          if specialmode == 1:
            z = f1*math.sin(z.real)-g1*math.sin(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c
          if specialmode == 2:
            z = f1*math.cos(z.real)+g1*math.cos(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c
          if specialmode == 3:
            z = f1*math.tan(z.real)-g1*math.sin(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c 
        if modus == 3:
          if specialmode == 3:
            specialmode = 0
          if specialmode == 0:
            z = f1*math.tan(z.real)+g1*math.tan(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c
          if specialmode == 1:
            z = f1*math.sin(z.real)+g1*math.cos(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c
          if specialmode == 2:
            z = f1*math.cos(z.real)+g1*math.sin(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c
        if modus == 4:
          if specialmode == 0:
            z = f1*math.tan(z.real)+g1*math.sin(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c
          if specialmode == 1:
            z = f1*math.sin(z.real)+g1*math.tan(z.imag)+(f1*z.real+zIm)**(round(o,4))/k + c
          if specialmode == 2:
            z = f1*math.sin(z.real)+g1*z.imag**2+(f1*z.real+zIm)**(round(o,4))/k + c
          if specialmode == 3:
            z = f1*math.sin(z.real)+g1*math.sin(z.imag**2)+(f1*z.real+zIm)**(round(o,4))/k + c 
        if modus == 5:
          if specialmode == 0:
            z = f*z.real+g*math.sin(math.tan(z.imag))+(zRe+zIm)**(round(o,4))/k + c
          if specialmode == 1:
            z = (math.floor(10*z.real)/10+math.floor(10*z.imag)/10)+(zRe+zIm)**(round(o,4))/k + c
          if specialmode == 2:
            z = k*(f1*zRe)**(math.floor(10*o)/10)+(1-k)*(g1*zIm)**(math.floor(10*o)/10) + c
            #z = (math.sin(z.real)+math.sin(z.imag))+(zRe+zIm)**(math.floor(10*o)/10)/k + c
          if specialmode == 3:
            z = (zRe*zIm)**(round(o,4))/k + c
        if modus == 6:
          if specialmode == 0:
            z = f1*math.sin(z.real)+(zRe+zIm)**(round(o,4))/k + c
          if specialmode == 1:  
            z = f1*math.tan(z.real)+(zRe+zIm)**(round(o,4))/k + c
          if specialmode == 2:
            z = f1*math.sin(z.imag)+(zRe+zIm)**(round(o,4))/k + c
          if specialmode == 3:
            z = f1*math.tan(z.imag)+(zRe+zIm)**(round(o,4))/k + c
        if modus == 7:
          # z = z*1.1 + c
          # z = f*math.tan(z.real)+(zRe+zIm)**(math.floor(10*o)/10)/k + c
          if specialmode == 0:
            #z = (zRe*zIm)**(round(o,4))/k + c
            z = f*math.sin(math.tan(z.real))+g*math.cos(z.imag)+(zRe+zIm)**(math.floor(10*o)/10)/k + c 
          if specialmode == 1:
            z = (f*zRe+g*zIm) + c**(math.floor(10*o)/10)/k
          if specialmode == 2:
            z = (math.sin(z.real)+math.sin(z.imag))+(zRe+zIm) + c**(math.floor(10*o)/10)/k
          if specialmode == 3:
            z = (math.sinh(z.real) + math.cosh(z.imag)) / k + c
        if modus == 8:
          z = (zRe+zIm)**(round(o,4))/k + c 
        if modus == 9:
          if specialmode == 0:
            z = z.real+(zIm)**(round(o,4))/k + c**z.real  
          if specialmode == 1:
            z = z.real**z.imag+(zIm)**(round(o,4))/k + c  
          if specialmode == 2:
            z = z.real**z.real+(zIm)**(round(o,4))/k + c  
          if specialmode == 3:
            z = z.imag**z.imag+(zIm)**(round(o,4))/k + c  
        if modus == 10:
          if specialmode == 0:
            r = math.sqrt(z.real**2 + z.imag**2)
            theta = math.atan2(z.imag, z.real)
            z = complex(math.sin(r) + math.cos(theta), math.cos(r) - math.sin(theta)) + c
          if specialmode == 1:
            z = complex(math.log(abs(z.real+1)), math.atan(z.imag+1)) + c
          if specialmode > 1:
            z = (zRe+zIm)**2 + c
        if modus == 11:
          z = (zRe+zIm) + c 
        if modus >= 12:
          z = (zRe+zIm)**(round(o,4))/k + c 

        #print(z.real,z.imag,zRe,zIm,z,f,g,c)

        #-1.24609375 0.2777777777777777 0j 0j (-1.24609375+0.2777777777777777j) (0.8414709848078965+0j) (0.8414709848078965+0j) (-1.24609375+0.2777777777777777j)
        #-2.2946454849754647 0.5115197180021933 (-1.0485517349754647+0j) 0.2337419402244156j (-2.2946454849754647+0.5115197180021933j) (0.8414709848078965+0j) (0.8414709848078965+0j) (-1.24609375+0.2777777777777777j)
        #######
        if modus < -2:
          if z.real**2 + z.imag**2 < 0.01:
            rand77 = (1/(z.real**2 + z.imag**2))%255
          if z.real**2 + z.imag**2 > 5: break
          if mod7 != 0:
            if int((z.real**2 + z.imag**2)%7) == 4:
              redline = True
        #elif modus == 12:
        #  if z.real**2 + z.imag**2 > 5: break
        else:
          #if mod7 != 0:   # green stripes on
          if smallline == 4:
            if z.real**2 + z.imag**2 < 4:
              smalll = True
          else:
            if smallline != 1 and smallline != 3:
              smalll = True
            if z.real**2 + z.imag**2 > 2 or z.real**2 + z.imag**2 < 0.1:
              if int((z.real**2 + z.imag**2)%7) == 4:
                redline = True
              if smallline == 1:
                if z.real**2 + z.imag**2 < 0.01:
                  smalll = True
              #if smallline == 2:
              #  if z.real**2 + z.imag**3 < 4:
              #    smalll = True
              if smallline == 3:
                if z.real**2 + z.imag**2 < 4:
                  smalll = True
          if z.real**2 + z.imag**2 > 4: 
            bw = 1
            break
      if smalll == True:                                  # inner squircle
        if smallline == 1:
          rand777 = (1/(z.real**2 + z.imag**2))%255
          if random.randint(0,1) == 1:
            fractal[x][y] = (rand777,rand777,rand777)
          else:
            fractal[x][y] = farben[i]
        if smallline == 2:
          #rand777 = (100/(z.real**3 + z.imag**3))%255
          #if random.randint(0,2) != 0:
          #  fractal[x][y] = (rand777,rand777,rand777)
          #fractal[x][y] = farben[min(max_iter,abs(rand777))]
          if bw == 0:
            rand777 = (100/(z.real**3 + z.imag**3))%255
            fractal[x][y] = (rand777,rand777,rand777)
          else:
            fractal[x][y] = farben[i]
        if smallline == 7:
          if bw == 0:
            rand777 = (100/(z.real**2 + z.imag**3))%255
            fractal[x][y] = (rand777,rand777,rand777)
          else:
            fractal[x][y] = farben[i]
        if smallline == 8:
          if bw == 0:
            rand777 = (100/(z.real**3 + z.imag**2))%255
            fractal[x][y] = (rand777,rand777,rand777)
          else:
            fractal[x][y] = farben[i]
        if smallline == 3:
          rand777 = (100/(z.real**2 + z.imag**2))%255
          if random.randint(0,2) != 0:
            fractal[x][y] = (rand777,rand777,rand777)
        if smallline == 4:
          rand777 = (100/(z.real**2 + z.imag**2))%255
          if random.randint(0,2) != 0:
            fractal[x][y] = (rand777,rand777,rand777)
        if smallline == 5:
          if bw == 1:
            rand777 = (100/(z.real**2 + z.imag**2))%255
            fractal[x][y] = (rand777,rand777,rand777)
          else:
            fractal[x][y] = farben[i]
        if smallline == 6:
          if bw == 0:
            rand777 = (100/(z.real**2 + z.imag**2))%255
            fractal[x][y] = (rand777,rand777,rand777)
          else:
            fractal[x][y] = farben[i]

      if redline == True:                                 # green modulo lines
        #if smalll == False:
        if modus < -2:
          fractal[x][y] = (rand77/2,rand77,rand77/2)
        else:
          if mod7 == 1:
            fractal[x][y] = (0,random.randint(0,244),0)
          if mod7 == 2:
            rand7 = random.randint(0,1)
            if rand7 == 1:
              fractal[x][y] = (0,244,0)
            else:
              fractal[x][y] = farben[i]
          if mod7 == 3:
            fractal[x][y] = (0,244,0)
          if mod7 == 0:
            fractal[x][y] = farben[i]
      else:
          if modus < -2:
            fractal[x][y] = (rand77/2,rand77,rand77/2)
          #elif modus == 12:
          #  complex_color = z.imag+z.real
          #  fractal[x][y] = (math.log(complex_color)%255,(math.log(complex_color)+70)%255,(math.log(complex_color)+70)%255)
          else:
            if smallline == 5:
              fractal[x][y] = farben[i]
            else:
              if smalll == False:
                fractal[x][y] = farben[i]
  return fractal   

def color_calc_randint():
    for i in range(20000):
        r = random.randint(0,17)*15
        g = int(255-abs(math.sin(i/10)) * 255)   # Keep g as sine
        b = random.randint(0,17)*15
        farben[inv * i] = (r, g, b)

def color_calc_green():
    for i in range(20000):
        r = 20
        g = int(255-(0.5 * math.sin(0.1 * i + 2.618) + 0.5) * 255)   # Keep g as sine
        b = 20
        farben[inv * i] = (r, g, b)

def color_calc_inv0():
  for i in range(20000):
    r = int((0.5 * math.cos(0.1 * i**1.1 +2.094+random.randint(0,100)/1000) + 0.5) * 255)
    g = int(max(0,min(255,(0.5 * math.tan(0.1 * i +4.188+random.randint(0,100)/1000) + 0.5))))
    b = int((0.5 * math.sin(0.1 * i+random.randint(0,100)/1000) + 0.5) * 255)
    farben[inv*i] = (r,g,b)

def color_calc_inv():
  for i in range(20000):
    r = int((0.5 * math.cos(0.1 * i**1.1 +2.094+random.randint(0,100)/1000) + 0.5) * 255)
    g = int((0.5 * math.sin(0.1 * i +4.188+random.randint(0,100)/1000) + 0.5) * 255)
    b = int((0.5 * math.sin(0.1 * i+random.randint(0,100)/1000) + 0.5) * 255)
    farben[inv*i] = (r,g,b)

def color_calc_smooth():
    for i in range(20000):
        r = int(255-(0.5 * math.sin(0.08 * i + 1.047) + 0.5) * 255)  # Cosine for r
        g = int(255-(0.5 * math.sin(0.1 * i + 2.618) + 0.5) * 255)   # Keep g as sine
        b = int(255-(0.5 * math.sin(0.05 * i + 3.141) + 0.5) * 255)  # Cosine for b
        farben[inv * i] = (r, g, b)

def color_calc_random():
    for i in range(20000):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        farben[i] = (r,g,b)
color_calc_random()

colorshift = 0
shifter = 0

def color_shift():
    global shifter
    for i in range(20000):
        r = int((127+(math.sin(i*0.1+shifter)))*127)
        g = r
        b = r
        farben[i] = (r,g,b)

def color_shift2():
    global shifter
    for i in range(20000):
        r = int((127+(math.sin(i*0.1+shifter)))*127)
        g = int((127+(math.sin(i*0.1+shifter+1)))*127)
        b = int((127+(math.sin(i*0.1+shifter+2)))*127)
        farben[i] = (r,g,b)

mini1 = 1
mini2 = -1
mini3 = 1
mini4 = -1

angle = 0
rotation_speed = 45  # in degree
save = False
alpha = 0
color = 0
outomat = False
intomat = False
sound_on = True

while True:
    if -7 < modus < 17:
      '''
      if modus == -4:
          formula = (f"z = (modus 7)**"+str((math.floor(10*o)/10))+" + (f*zRe,g*zIm)*"+str((math.floor(10*k)/10))+" + c           z("+str(round(za,3))+","+str(round(zb,3))+")")
      if modus == -3:
          formula = (f"z = (modus 1)**"+str((math.floor(10*o)/10))+" + (f*zRe,g*zIm)*"+str((math.floor(10*k)/10))+" + c           z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == -2:
          formula = (f"z = (f*z.real-g*z.imag)**"+str((math.floor(10*o)/10))+" + (f*zRe,g*zIm)*"+str((math.floor(10*k)/10))+" + c           z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == -1:
          formula = (f"z = z**2 - (zRe,zIm)**2 + c           z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 0:
          formula = (f"z = f*tan(zRe)+(f*zRe+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c           z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 1:
          formula = (f"z = (f*zRe+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c           z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 2:
          formula = ("z = f*tan(zRe)+g*tan(zIm)+g*tan(f*zRe+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 3:
          formula = ("z = f*sin(zRe)+g*tan(zIm)+g*cos(f*zRe+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 4:
          formula = ("z = f*tan(zRe)+g*tan(zIm)+((f+1)*tan(zRe)+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 5:
          formula = ("z = f*sin(zRe)+g*sin(zIm)+((f+1)*zRe+zIm)**e/k + c"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 6:
          formula = ("z = -f*sin(zRe)+(zRe+g*zIm)**"+str((math.floor(10*o)/10))+"/"+str((math.floor(10*k)/10))+" + c    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 7:
          formula = ("modus 7"+"    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 8:
          formula = ("modus int"+"    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 9:
          formula = ("modus sin tan"+"    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 10:
          formula = ("modus sin sin"+"    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      if modus == 11:
          formula = ("modus sin cos"+"    z("+str(math.floor(10*za)/10)+","+str(math.floor(10*zb)/10)+")")
      '''
      if modus > -5:
        formula = ("modus: "+str(modus)+"     z("+str(round(za,3))+","+str(round(zb,3))+")")
    if menu == -1:
      formula += str("        zoom: "+str(int(100/zoom)/100))
      formula += str("       f:"+str(round(f1,7))+" | g:"+str(round(g1,7)))
      formula += ("\n"
                  "\n"
                  "\n"
                  "\n"
                  "\n")
    if menu == 1:
      formula += "      "
    formula += str("maximum iterations = "+str(max_iter))
    #if menu == -1:
    formula += str("\n")
    formula += str("\n")
    formula += str("\n")
    if cz == 1 or cz == 2:
      cct = str(str(round(cc,2))+"+"+str(round(cci,2))+"i")
    else:
      cct = str("-")
    if stopstop == False:
        formula += str(str(modus)+" | "+str(color)+" | "+str(colorshift)+" | "+str(mod7)+" | "+str(smallline)+" | "+str(specialmode)+" | "+str(1/10**(rounder))+" | "+cct+" | . . .") 
    else:
        formula += str(str(modus)+" | "+str(color)+" | "+str(colorshift)+" | "+str(mod7)+" | "+str(smallline)+" | "+str(specialmode)+" | "+str(1/10**(rounder))+" | "+cct+" | .")
    if menu == 1:
      formula += str("        zoom factor: "+str(1/zoom))
      formula += str("\n"+"\n"+"\n"+"\n"
                     "controls: "+"\n"
                     "\n"
                     "[x] zoom in"+"\n"
                     "\n"
                     "[y] zoom out"+"\n"
                     "\n"
                     "[v] seed z(+,0)        [1] g -     g:"+str(g1)+"\n"
                     "\n"
                     "[c] seed z(-,0)         [2] g + "+"\n"
                     "\n"
                     "[f] seed z(0,+)         [3] f -     f:"+str(f1)+"\n"
                     "\n"
                     "[d] seed z(0,-)         [4] f + "+"\n"
                     "\n"
                     "[7] k -     k:"+str(math.floor(k*10)/10)+"           [5] o - "+"\n"
                     "\n"
                     "[8] k +           o:"+str(o)+"       [6] o + "+"\n"
                     "\n"
                     "[i] maximum iterations +        [ä/ö] precision: "+"\n"
                     "\n"
                     "[u] maximum iterations -                 "+str(1/10**(rounder))+"\n"
                     "\n"                                      # 0."+(rounder-1)*"0"+"1"+"\n"
                     "[r] reset                        [o|k|j] change colors"+"\n"
                     "\n"
                     "[s] save image            [p|l] switch formula"+"\n"
                     "\n"
                     "[arrowkeys] move       [a] rotate"+"\n"
                     "\n"
                     "[space] toggle surf mode  "+"\n"
                     "\n"
                     "[,] sound on/off  "+"\n"
                     "\n"
                     "[+] modulo stripes      [-] colorshift  "+"\n")
    clock.tick()
    for ereignis in pg.event.get():
        if ereignis.type == pg.QUIT or \
           ereignis.type == pg.KEYDOWN and ereignis.key == pg.K_ESCAPE:
          quit()
        if ereignis.type == pg.MOUSEBUTTONDOWN: 
          mx, my = pg.mouse.get_pos()
          print(mx,my)
          print(mx/breite,my/höhe)
          if pg.mouse.get_pressed()[0]:
            trace(mx,my, cc, cci,x1,x2,y1,y2)
          elif pg.mouse.get_pressed()[2]:
            notrace = not notrace
        elif ereignis.type == pg.MOUSEMOTION:
          mx, my = pg.mouse.get_pos()
          print(mx,my)
          print(mx/breite,my/höhe)
          if pg.mouse.get_pressed()[0]:
            trace(mx,my, cc, cci,x1,x2,y1,y2)
        elif ereignis.type == pg.MOUSEBUTTONUP: 
          mx, my = pg.mouse.get_pos()
          print(mx,my)
          print(mx/breite,my/höhe)
          if pg.mouse.get_pressed()[0]:
            trace(mx,my, cc, cci,x1,x2,y1,y2)
        ''' 
        if ereignis.type == pg.MOUSEBUTTONDOWN: # and not verschiebe:
          mx, my = pg.mouse.get_pos()
          print(mx,my)
          if pg.mouse.get_pressed()[0]:
            dx, dy = pixel2fractal(breite/4, höhe/4)
            x1 += dx*mx/breite; x2 -= dx*(1-mx/breite); y1 += dy*my/höhe; y2 -= dy*(1-my/höhe);
            print(x1,x2,y1,y2,dx,dy,mx/breite,my/höhe)
            #x1 += dx; x2 -= dx; y1 += dy; y2 -= dy
            #zoomer_minus()
            time_counted = False

            #verschiebe = True   
        
        if verschiebe and ereignis.type != pg.MOUSEBUTTONUP:
          mx2, my2 = pg.mouse.get_pos()
          dx, dy = pixel2fractal(mx2-mx, my2-my)
          x1 -= dx; x2 -= dx; y1 -= dy; y2 -= dy
          mx, my = mx2, my2
        if verschiebe and ereignis.type == pg.MOUSEBUTTONUP:
          verschiebe = False
        '''
        if ereignis.type == pg.KEYDOWN:                   #          <~~ KEYS
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
          if ereignis.key == pg.K_SPACE:
            stopstop = not stopstop
            '''
            if f1 > 1.2:
              f1 = 1.1
            if g1 > 1.2:
              g1 = 1.1
            if za > 1.2:
              za = 1.1
            if zb > 1.2:
              zb = 1.1    
            if f1 < -0.7:
              f1 = -0.7
            if g1 < -0.7:
              g1 = -0.7
            if za < -0.7:
              za = -0.7
            if zb < -0.7:
              zb = -0.7   
            '''
          if ereignis.key == pg.K_i:
            if max_iter > 19:
                max_iter += 10
            #    rounder += 1 
            else: 
                max_iter += 5
            time_counted = False
          if ereignis.key == pg.K_u:
            if max_iter > 20:
                max_iter -= 10
            #    rounder -= 1
            else:
                max_iter -= 5
                #rounder -= 1
            #if rounder < 1:
            #    rounder = 1
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
          if ereignis.key == pg.K_g:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 -= dx; x2 -= dx 
            dx, dy = pixel2fractal(breite/10, höhe/10)
            y1 -= dy; y2 -= dy
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 += dx; x2 -= dx; y1 += dy; y2 -= dy
            zoomer_plus()
            time_counted = False
          if ereignis.key == pg.K_h:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 += dx; x2 += dx
            dx, dy = pixel2fractal(breite/10, höhe/10)
            y1 -= dy; y2 -= dy
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 += dx; x2 -= dx; y1 += dy; y2 -= dy
            zoomer_plus()
            time_counted = False
          if ereignis.key == pg.K_b:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 -= dx; x2 -= dx 
            dx, dy = pixel2fractal(breite/10, höhe/10)
            y1 += dy; y2 += dy
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 += dx; x2 -= dx; y1 += dy; y2 -= dy
            zoomer_plus()
            time_counted = False
          if ereignis.key == pg.K_n:
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 += dx; x2 += dx
            dx, dy = pixel2fractal(breite/10, höhe/10)
            y1 += dy; y2 += dy
            dx, dy = pixel2fractal(breite/10, höhe/10)
            x1 += dx; x2 -= dx; y1 += dy; y2 -= dy
            zoomer_plus()
            time_counted = False
          if ereignis.key == pg.K_k:
            color = 0
            color_calc_random()
            time_counted = False
            colorshift = 0
          if ereignis.key == pg.K_j:
            if color == 0:
              color = 9
            else:
              color -= 1
            if color == 0:
              color_calc_random()
            elif color == 1:
              inv = -1
              color_calc_smooth()
            elif color == 2:
              inv = -1
              color_calc_inv()
            elif color == 3:
              inv = 1
              color_calc_smooth()
            elif color == 4:
              inv = 1
              color_calc_inv0()
            elif color == 5:
              inv = -1
              color_calc_inv0()
            elif color == 6:
              inv = 1
              color_calc_green()
            elif color == 7:
              inv = -1
              color_calc_green()
            elif color == 8:
              inv = 1
              color_calc_randint()
            elif color == 9:
              inv = -1
              color_calc_randint()
            else:
              color = 0
              color_calc_random()
            time_counted = False
            colorshift = 0
          if ereignis.key == pg.K_o:
            #farben = np.full((20000, 3), (0,0,0), dtype=np.uint8)
            color += 1
            if color == 0:
              color_calc_random()
            elif color == 1:
              inv = -1
              color_calc_smooth()
            elif color == 2:
              inv = -1
              color_calc_inv()
            elif color == 3:
              inv = 1
              color_calc_smooth()
            elif color == 4:
              inv = 1
              color_calc_inv0()
            elif color == 5:
              inv = -1
              color_calc_inv0()
            elif color == 6:
              inv = 1
              color_calc_green()
            elif color == 7:
              inv = -1
              color_calc_green()
            elif color == 8:
              inv = 1
              color_calc_randint()
            elif color == 9:
              inv = -1
              color_calc_randint()
            else:
              color = 0
              color_calc_random()
            time_counted = False
            colorshift = 0
          if ereignis.unicode == '9':
            if cz == 1:
              cc += 0.1
              if cc > 2:
                cc = -2
            if cz == 2:
              cc -= 0.1
              if cc < -2:
                cc = 2
            if cz == 0:
              cz = 1
          if ereignis.unicode == '0': 
            if cz == 1:
              cci += 0.1
              if cci > 2:
                cci = -2
            if cz == 2:
              cci -= 0.1
              if cci < -2:
                cci = 2
            if cz == 0:
              cz = 1
          if ereignis.unicode == '#': 
            cz += 1
            if cz > 2:
              cz = 0
          if ereignis.unicode == ',': 
            sound_on = not sound_on
          if ereignis.unicode == '.':
            smallline += 1
            if smallline > 8:
              smallline = 0
          if ereignis.unicode == '+':
            mod7 += 1
            if mod7 > 3:
              mod7 = 0
          if ereignis.unicode == '-':
            colorshift += 1
            if colorshift > 2:
              colorshift = 0
            if colorshift == 1:
              color_shift()
            if colorshift == 2:
              color_shift2()
          if ereignis.unicode == 'ä':
            rounder += 1
          if ereignis.unicode == 'ö':
            rounder -= 1
            if rounder < 0:
              rounder = 0
            print("rounder: ",rounder)
          if ereignis.unicode == 'ü':
            specialmode += 1
            if specialmode > 3:
              specialmode = 0
            print("specialmode: ",specialmode)
          if ereignis.unicode == '3':
            f1-=min(0.2,0.1*zoom)
            time_counted = False
          if ereignis.unicode == '4':
            f1+=min(0.2,0.1*zoom)
            time_counted = False
          if ereignis.unicode == '1':
            g1-=min(0.2,0.1*zoom)
            time_counted = False
          if ereignis.unicode == '2':
            g1+=min(0.2,0.1*zoom)
            time_counted = False
          if ereignis.unicode == '5':
            o-=0.1
            if o<1:
              o=0.1
            o = round(o,4)
            time_counted = False
          if ereignis.unicode == '6':
            o+=0.1
            o = round(o,4)
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
            if modus > 13:
              modus = -4
          if ereignis.key == pg.K_l:
            modus -= 1
            if modus == -5:
              modus = 13
          if ereignis.key == pg.K_a:
            angle += rotation_speed
            if angle >= 360:
              angle = 0
          if ereignis.key == pg.K_s:
            save = not save
          if ereignis.key == pg.K_q:
            outomat = not outomat
          if ereignis.key == pg.K_w:
            intomat = not intomat
          if ereignis.key == pg.K_r:
            #stopstop = True
            time_counted = False
            x1,x2,y1,y2 = -2,1,-1,1
            zoom = 1
            fractal = np.full((breite, höhe, 3), (0,0,0), dtype=np.uint8)
            farben = np.full((20000, 3), (0,0,0), dtype=np.uint8)
            zeichne_fractal(x1,x2,y1,y2,fractal,max_iter,za,zb,f1,g1,o,k,modus,farben,mod7,smallline,specialmode,cc,cci,cz)
            color = 0
            color_calc_random()
            verschiebe = False
            max_iter = 40   
            za = 0
            zb = 0
            o = 2
            f1 = 1
            g1 = 1
            k = 1
            print("reset")
    if outomat == True:
      if zoom < 1:
        save = True
        dx, dy = pixel2fractal(breite/10, höhe/10)
        x1 -= dx; x2 += dx; y1 -= dy; y2 += dy
        zoomer_minus()
        time_counted = False
    if intomat == True:
      #save = True
      dx, dy = pixel2fractal(breite/10, höhe/10)
      x1 += dx; x2 -= dx; y1 += dy; y2 -= dy
      zoomer_plus()
      time_counted = False
    if save == True:
      fname = font.render("saving...", True, (0,0,0))  # Render the formula text
      fname_rect = fname.get_rect(topleft=(10, höhe-40))  # Position the formula text
      fenster.blit(fname, fname_rect) 
      pg.display.flip()
    if time_counted == False:
      start_time = time.time()
    fractal = zeichne_fractal(x1,x2,y1,y2,fractal,max_iter,za,zb,f1,g1,o,k,modus,farben,mod7,smallline,specialmode,cc,cci,cz)
    if save == True:
      fname = font.render("saving...", True, (0,0,0))  # Render the formula text
      fname_rect = fname.get_rect(topleft=(10, höhe-40))  # Position the formula text
      fenster.blit(fname, fname_rect) 
      pg.display.flip()
    # Render and draw text
    font = pg.font.Font(None, 17)  # Choose a font and size
    if menu == 1:
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

    if stopstop == False:
      time_counted = False
      f1 += mini3*0.01*zoom
      g1 += mini4*0.01*zoom
      if f1>1.2:
        mini3*=-1
      if f1<-1.1:
        mini3*=-1
      if g1>1.2:
        mini4*=-1
      if g1<-1.1:
        mini4*=-1
      za += mini1*0.01*zoom
      zb += mini2*0.01*zoom
      if za>1.2:
        mini1*=-1
      if za<-0.7:
        mini1*=-1
      if zb>1.2:
        mini2*=-1
      if zb<-0.7:
        mini2*=-1
      if cz == 1 or cz == 2:
        cc += 0.01*zoom
        if cc > 1:
          cc = -1
        cci += 0.01*zoom
        if cci > 1:
          cci = -1
      #f1 = round(f1,rounder)
      #g1 = round(g1,rounder)
      #za = round(za,rounder)
      #zb = round(zb,rounder)

    #pg.display.flip()
    pg.display.set_caption(f'FPS = {clock.get_fps():.1f} iterations = {max_iter:,.0f}')    # formula = {formula}

    if colorshift != 0:
      shifter += 0.1
      if shifter > 100:
        shifter = 0
      if colorshift == 1:
        color_shift()
      if colorshift == 2:
        color_shift2()

    # ROTATE
    if angle != 0:
      screen_surface = pg.display.get_surface()
      rotated_surface = pg.transform.rotate(screen_surface, angle)
      rotated_rect = rotated_surface.get_rect(center=(breite // 2, höhe // 2))
      fenster.fill((0,0,0))
      fenster.blit(rotated_surface, rotated_rect)
    #if outomat == True:
    #  save = True
    if save == True:
      screenshot = pg.Surface((breite,höhe)) # 1200, 700
      screenshot.blit(fenster, (0, 0))
      while scr<2000:
        filename = str("frac_"+str(scr)+".png")
        if os.path.exists(filename):
          scr+=1
        else:
          filename = str("frac_"+str(scr)+".png")
          pg.image.save(screenshot, filename) 
          print("saved.") 
          break 
      fname = font.render("saved as "+filename, True, (0,0,0))  # Render the formula text
      fname_rect = fname.get_rect(topleft=(10, höhe-20))  # Position the formula text
      fenster.blit(fname, fname_rect) 
      if stopstop == True and colorshift == 0:
        save = False
    alpha += 1
    print(alpha)
    if sound_on == True:
      sound_x()
    if notrace == False:
      ttt = 1
      while ttt < len(traces_out):
        pg.draw.line(fenster,(0,244,0),traces_out[ttt],traces_out[ttt-1],2)
        ttt += 1
    pg.display.flip()
    #time.sleep(0.005)
    #pg.time.delay(5)

pg.quit()

