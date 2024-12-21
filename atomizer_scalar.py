#atomizer_scalar

import pygame
import random
import os

pygame.init()

width, height = 900,700
image = pygame.image.load(os.path.join("universe_filament.jpg"))
image1 = pygame.image.load(os.path.join("full_earth.png"))
image2 = pygame.image.load(os.path.join("sun1.jpg"))
image = pygame.transform.scale(image, (width-20, height-20))  # Resize the image
image1 = pygame.transform.scale(image1, (70, 70))
image2 = pygame.transform.scale(image2, (70, 70))
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("standard")
font = pygame.font.Font(None, 70)
font2 = pygame.font.Font(None, 36)
font3 = pygame.font.Font(None, 27)

slider_bar_rect1 = pygame.Rect(width-70, 50, 20, 500)  # x, y, width, height
slider_handle_rect1 = pygame.Rect(width-75, 50, 30, 20)  # x, y, width, height

slider_bar_rect2 = pygame.Rect(width-147, 50, 20, 500)  # x, y, width, height
slider_handle_rect2 = pygame.Rect(width-152, 50, 30, 20)  # x, y, width, height

dragging1 = False
dragging2 = False

RED = (244,0,0)

#ballx = width/2
#bally = height/2
balls = []
speed = 1
ball_color = (0,244,0)

inner_circle = 70

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.growing = True
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.lining = True
    
    def update(self):
        global speed
        self.x += self.vx*speed
        self.y += self.vy*speed #self.vy+self.vy*trash_1 #+random.randint(0,2)
        if self.x < 0 or self.x > width:
            self.vx *= -1
        if self.y < 0 or self.y > height:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, ball_color, (int(self.x), int(self.y)), int(self.radius))
        photon = random.randint(0,100)
        if photon == 1:
            pygame.draw.line(screen, (207,144,20),(int(self.x), int(self.y)),(int(width/2),int(height/2)))

balls2 = []
balls3 = []
speed2 = 0.1
speed3 = 0.04
ball_color2 = (244,0,0)
ball_color3 = (144,144,144)
ball_color_u = (0,177,0)
ball_color_d = (0,0,233)

x_half = width/2
y_half = height/2

class Ball2:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.growing = True
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.lining = True
    
    def update(self):
        global speed2
        self.x += self.vx*speed2
        self.y += self.vy*speed2 #self.vy+self.vy*trash_1 #+random.randint(0,2)
        if ((x_half-self.x)**2+(y_half-self.y)**2)**0.5 > inner_circle:
            self.vx *= -1
            self.vy *= -1

    def draw(self):
        fact = value3*7/270
        pygame.draw.circle(screen, ball_color2, (int(self.x), int(self.y)), int(self.radius)*fact)
        pygame.draw.circle(screen, ball_color_u, (int(self.x-4*fact), int(self.y-3*fact)), int(self.radius/3)*fact)
        pygame.draw.circle(screen, ball_color_u, (int(self.x+4*fact), int(self.y-3*fact)), int(self.radius/3)*fact)
        pygame.draw.circle(screen, ball_color_d, (int(self.x), int(self.y+4*fact)), int(self.radius/4)*fact)

class Ball3:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.growing = True
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.lining = True
    
    def update(self):
        global speed3
        self.x += self.vx*speed3
        self.y += self.vy*speed3 #self.vy+self.vy*trash_1 #+random.randint(0,2)
        if ((x_half-self.x)**2+(y_half-self.y)**2)**0.5 > 70:
            self.vx *= -1
            self.vy *= -1

    def draw(self):
        fact = value3*7/270
        pygame.draw.circle(screen, ball_color3, (int(self.x), int(self.y)), int(self.radius)*fact)
        pygame.draw.circle(screen, ball_color_u, (int(self.x-4*fact), int(self.y-3*fact)), int(self.radius/3)*fact)
        pygame.draw.circle(screen, ball_color_d, (int(self.x+4*fact), int(self.y-3*fact)), int(self.radius/4)*fact)
        pygame.draw.circle(screen, ball_color_d, (int(self.x), int(self.y+4*fact)), int(self.radius/4)*fact)

modi = 1
# Ball class
class Ball4:
    def __init__(self, x, y, radius, attraction_point):
        self.x = x
        self.y = y
        self.radius = radius
        self.attraction_point = attraction_point
        self.vx = 1
        self.vy = 0.7

    def update(self):
        # Calculate the attraction force
        ax, ay = self.attraction_point
        dx = ax - self.x
        dy = ay - self.y
        dist = max((dx**2 + dy**2)**0.5, 1)  # Prevent division by zero
        force = 0.2  # Adjust this value for stronger or weaker attraction
        
        # Acceleration proportional to the force
        ax = (force * dx) / dist
        ay = (force * dy) / dist

        # Update velocity
        self.vx += ax
        self.vy += ay

        # Update position
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, (0,40,144), (int(self.x), int(self.y)), self.radius)
        # Draw attraction point
        #pygame.draw.circle(screen, WHITE, (int(self.attraction_point[0]), int(self.attraction_point[1])), 3)

# Create 8 balls with random positions and attraction points
balls4 = []
for _ in range(8):
    x = width/2-100#+random.randint(-100, 100)
    y = height/2-20#+random.randint(-100, 100)
    attraction_x = width/2#random.randint(10, width - 100)
    attraction_y = height/2#random.randint(10, height - 100)
    radius = 10
    balls4.append(Ball4(x, y, radius, (attraction_x, attraction_y)))

#t = 0
#while t < 7:        
#    balls.append(Ball(random.randint(0, width), random.randint(0, height), random.randint(7,10)))
#    balls2.append(Ball2(width/2, height/2, 12))
#    balls3.append(Ball3(width/2, height/2, 12))
#    t += 1

value1 = 1
value2 = 1
value3 = 1
modus = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mx,my = mouse_pos[0],mouse_pos[1]
            print(mx,my)
            if slider_handle_rect1.collidepoint(event.pos):
                dragging1 = True
            if slider_handle_rect2.collidepoint(event.pos):
                dragging2 = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if modus == 2:
                image1 = pygame.image.load(os.path.join("full_earth.png"))
                image1 = pygame.transform.scale(image1, (70+value3*7,70+value3*7))
                image2 = pygame.image.load(os.path.join("sun1.jpg"))
                image2 = pygame.transform.scale(image2, (10000/max(1,value3),10000/max(1,value3)))
            dragging1 = False
            dragging2 = False
            value1 = (118 -(slider_handle_rect1.y - slider_bar_rect1.top) / (slider_bar_rect1.height - slider_handle_rect1.height) * 118)
            value3 = (100 -(slider_handle_rect2.y - slider_bar_rect2.top) / (slider_bar_rect2.height - slider_handle_rect2.height) * 100)
            balls = []
            balls2 = []
            balls3 = []
            t = 1
            while t < value2:
                balls3.append(Ball3(width/2, height/2, 12))
                t += 1
            t = 1
            while t < value1:
                balls.append(Ball(random.randint(0, width), random.randint(0, height), random.randint(4,7)))
                balls2.append(Ball2(width/2, height/2, 12))
                t += 1
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            print(event.w,event.h)
        elif event.type == pygame.MOUSEMOTION:
            if dragging1:
                mouse_y = event.pos[1]
                handle_y = max(slider_bar_rect1.top, min(mouse_y, slider_bar_rect1.bottom - slider_handle_rect1.height))
                slider_handle_rect1.y = handle_y
            if dragging2:
                mouse_y = event.pos[1]
                handle_y = max(slider_bar_rect2.top, min(mouse_y, slider_bar_rect2.bottom - slider_handle_rect2.height))
                slider_handle_rect2.y = handle_y
                if modus == 2:
                    image1 = pygame.transform.scale(image1, (70+value3*7,70+value3*7))
                    image2 = pygame.transform.scale(image2, (10000/max(1,value3),10000/max(1,value3)))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                value1 += 1
                if modus == 1:
                    value1 = 77
                balls = []
                balls2 = []
                balls3 = []
                t = 1
                while t < value2:
                    balls3.append(Ball3(width/2, height/2, 12))
                    t += 1
                t = 1
                while t < value1:
                    balls.append(Ball(random.randint(0, width), random.randint(0, height), random.randint(4,7)))
                    balls2.append(Ball2(width/2, height/2, 12))
                    t += 1
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_UP]:
            if event.key == pygame.K_DOWN:
                value1 -= 1
                if modus == 1:
                    value1 = 44
                balls = []
                balls2 = []
                balls3 = []
                t = 1
                while t < value1:
                    balls.append(Ball(random.randint(0, width), random.randint(0, height), random.randint(4,7)))
                    balls2.append(Ball2(width/2, height/2, 12))
                    t += 1
                t = 1
                while t < value2:
                    balls3.append(Ball3(width/2, height/2, 12))
                    t += 1

    screen.fill((0,0,0))

    # SLIDERS
    if modus != 2:
        pygame.draw.rect(screen, (44,44,44), slider_bar_rect1)
        pygame.draw.rect(screen, (244,0,0), slider_handle_rect1)
    pygame.draw.rect(screen, (44,44,44), slider_bar_rect2)
    pygame.draw.rect(screen, (104,144,104), slider_handle_rect2)

    if dragging1 == True:
        value1 = (118 - (slider_handle_rect1.y - slider_bar_rect1.top) / (slider_bar_rect1.height - slider_handle_rect1.height) * 118)
    if dragging2 == True:
        value3 = 100 - (slider_handle_rect2.y - slider_bar_rect2.top) / (slider_bar_rect2.height - slider_handle_rect2.height) * 100
    if value3 > 70:
        modus = 1
        for ball in balls4:
            ball.radius = 7
    elif 10 <= value3 <= 30:
        modus = 2
    elif value3 < 10:
        modus = 3
    else:
        modus = 0
    if modus == 0:
        text1 = font2.render(f'protons: {int(value1)}', True, (244,0,0))
        text2 = font3.render(f'electrons: {int(value1)}', True, (0,244,0))
        text3 = font3.render(f'neutrons: {int(value2)}', True, (144,144,144))
        if int(value1) == 0:
            text4 = "-"
            value2 = 0
        if int(value1) == 1:
            text4 = "HYDROGEN"
            value2 = 0
        elif int(value1) == 2:
            text4 = "HELIUM"
            value2 = value1
        elif int(value1) == 3:
            text4 = "LITHIUM"
            value2 = value1+1
        elif int(value1) == 4:
            text4 = "BERYLLIUM"
            value2 = value1+1
        elif int(value1) == 5:
            text4 = "BORON"
            value2 = value1+1
        elif int(value1) == 6:
            text4 = "CARBON"
            value2 = value1
        elif int(value1) == 7:
            text4 = "NITROGEN"
            value2 = value1
        elif int(value1) == 8:
            text4 = "OXYGEN"
            value2 = value1
        elif int(value1) == 9:
            text4 = "FLOURINE"
            value2 = value1+1
        elif int(value1) == 10:
            text4 = "NEON"
            value2 = value1
        elif int(value1) == 11:
            text4 = "SODIUM"
            value2 = value1+1
        elif int(value1) == 12:
            text4 = "MAGNESIUM"
            value2 = value1
        elif int(value1) == 13:
            text4 = "ALUMINIUM"
            value2 = value1+1
        elif int(value1) == 14:
            text4 = "SILICIUM/SILICON"
            value2 = value1
        elif int(value1) == 15:
            text4 = "PHOSPHOROUS"
            value2 = value1+1
        elif int(value1) == 16:
            text4 = "SULFUR"
            value2 = value1
        elif int(value1) == 17:
            text4 = "CHLORINE"
            value2 = value1+1
        elif int(value1) == 18:
            text4 = "ARGON"
            value2 = value1+4
        elif int(value1) == 19:
            text4 = "KALIUM/POTASSIUM"
            value2 = value1+1
        elif int(value1) == 20:
            text4 = "CALCIUM/CALX"
            value2 = value1
        elif int(value1) == 21:
            text4 = "SCANDIUM"    
            value2 = value1+3
        elif int(value1) == 22:
            text4 = "TITANIUM"
            value2 = value1+2
        elif int(value1) == 23:
            text4 = "VANADIUM"
            value2 = value1+5
        elif int(value1) == 24:
            text4 = "CHROMIUM"
            value2 = value1+4
        elif int(value1) == 25:
            text4 = "MANGANESE"
            value2 = value1+5    
        elif int(value1) == 26:
            text4 = "FERRUM"
            value2 = value1+4
        elif int(value1) == 27:
            text4 = "COBALT"
            value2 = value1+5
        elif int(value1) == 28:
            text4 = "NICKEL"
            value2 = value1+2
        elif int(value1) == 29:
            text4 = "CUPRUM/COPPER"
            value2 = value1+5
        elif int(value1) == 30:
            text4 = "ZINC"
            value2 = value1+4
        elif int(value1) == 31:
            text4 = "GALLIUM"
            value2 = value1+8
        elif int(value1) == 32:
            text4 = "GERMANIUM"
            value2 = value1+7
        elif int(value1) == 33:
            text4 = "ARSENIC"
            value2 = value1+9
        elif int(value1) == 34:
            text4 = "SELENIUM"
            value2 = value1+11
        elif int(value1) == 35:
            text4 = "BROMINE"
            value2 = value1+10
        elif int(value1) == 36:
            text4 = "KRYPTON"
            value2 = value1+12
        elif int(value1) == 37:
            text4 = "RUBIDIUM"
            value2 = value1+11
        elif int(value1) == 38:
            text4 = "STRONTIUM"
            value2 = value1+12
        elif int(value1) == 39:
            text4 = "YTTRIUM"
            value2 = value1+11
        elif int(value1) == 40:
            text4 = "ZIRCONIUM"
            value2 = value1+10
        elif int(value1) == 41:
            text4 = "NIOBIUM"
            value2 = value1+11
        elif int(value1) == 42:
            text4 = "MOLYBDENUM"
            value2 = value1+14
        elif int(value1) == 43:
            text4 = "TECHNECIUM"
            value2 = value1+12
        elif int(value1) == 44:
            text4 = "RUTHENIUM"
            value2 = value1+14
        elif int(value1) == 45:
            text4 = "RHODIUM"
            value2 = value1+13
        elif int(value1) == 46:
            text4 = "PALLADIUM"
            value2 = value1+14
        elif int(value1) == 47:
            text4 = "ARGENTIUM/SILVER"
            value2 = value1+13
        elif int(value1) == 48:
            text4 = "CADMIUM"
            value2 = value1+18
        elif int(value1) == 49:
            text4 = "INDIUM"
            value2 = value1+17
        elif int(value1) == 50:
            text4 = "ZINN/TIN"
            value2 = value1+20
        elif int(value1) == 51:
            text4 = "ANTIMONY"
            value2 = value1+19
        elif int(value1) == 52:
            text4 = "TELLERIUM"
            value2 = value1+26
        elif int(value1) == 53:
            text4 = "IODINE"
            value2 = value1+21
        elif int(value1) == 54:
            text4 = "XENON"
            value2 = value1+24
        elif int(value1) == 55:
            text4 = "CAESIUM"
            value2 = value1+23
        elif int(value1) == 56:
            text4 = "BARIUM"
            value2 = value1+26
        elif int(value1) == 57:
            text4 = "LANTHAN"
            value2 = value1+25
        elif int(value1) == 58:
            text4 = "CERIUM"
            value2 = value1+24
        elif int(value1) == 59:
            text4 = "PRASEODYMIUM"
            value2 = value1+23
        elif int(value1) == 60:
            text4 = "NEODYMIUM"
            value2 = value1+22
        elif int(value1) == 61:
            text4 = "PROMETHIUM"
            value2 = value1+23
        elif int(value1) == 62:
            text4 = "SAMARIUM"
            value2 = value1+28
        elif int(value1) == 63:
            text4 = "EUROPIUM"
            value2 = value1+27
        elif int(value1) == 64:
            text4 = "GADOLINIUM"
            value2 = value1+30
        elif int(value1) == 65:
            text4 = "TERBIUM"
            value2 = value1+29
        elif int(value1) == 66:
            text4 = "DYSPROSIUM"
            value2 = value1+32
        elif int(value1) == 67:
            text4 = "HOLMIUM"
            value2 = value1+31
        elif int(value1) == 68:
            text4 = "ERBIUM"
            value2 = value1+30
        elif int(value1) == 69:
            text4 = "THULIUM"
            value2 = value1+31
        elif int(value1) == 70:
            text4 = "YTTERBIUM"
            value2 = value1+34
        elif int(value1) == 71:
            text4 = "LUTETIUM"
            value2 = value1+33
        elif int(value1) == 72:
            text4 = "HAFNIUM"
            value2 = value1+36
        elif int(value1) == 73:
            text4 = "TANTAL"
            value2 = value1+35
        elif int(value1) == 74:
            text4 = "WOLFRAM/TUNGSTEN"
            value2 = value1+36
        elif int(value1) == 75:
            text4 = "RHENIUM"
            value2 = value1+37
        elif int(value1) == 76:
            text4 = "OSMIUM"
            value2 = value1+40
        elif int(value1) == 77:
            text4 = "IRIDIUM"
            value2 = value1+39
        elif int(value1) == 78:
            text4 = "PLATIN"
            value2 = value1+39
        elif int(value1) == 79:
            text4 = "AURUM/GOLD"
            value2 = 118
        elif int(value1) == 80:
            text4 = "HYDRARGYRUM/MERCURY/QUECKSILBER"
            value2 = value1+42
        elif int(value1) == 81:
            text4 = "THALIUM"
            value2 = value1+43
        elif int(value1) == 82:
            text4 = "PLUMBUM/LEAD/BLEI"
            value2 = value1+44
        elif int(value1) == 83:
            text4 = "BISMUTH"
            value2 = value1+43
        elif int(value1) == 84:
            text4 = "POLONIUM"
            value2 = value1+40
        elif int(value1) == 85:
            text4 = "ASTATINE"
            value2 = value1+40
        elif int(value1) == 86:
            text4 = "RADON"
            value2 = value1+38
        elif int(value1) == 87:
            text4 = "FRANCIUM"
            value2 = value1+38
        elif int(value1) == 88:
            text4 = "RADIUM"
            value2 = value1+50
        elif int(value1) == 89:
            text4 = "ACTINIUM"
            value2 = value1+47
        elif int(value1) == 90:
            text4 = "THORIUM"
            value2 = value1+52
        elif int(value1) == 91:
            text4 = "PROTACTINIUM"
            value2 = value1+49
        elif int(value1) == 92:
            text4 = "URANIUM"
            value2 = value1+54
        elif int(value1) == 93:
            text4 = "NEPTUNIUM"
            value2 = value1+50
        elif int(value1) == 94:
            text4 = "PLUTONIUM"
            value2 = value1+50
        elif int(value1) == 95:
            text4 = "AMERICIUM"
            value2 = value1+51
        elif int(value1) == 96:
            text4 = "CURIUM"
            value2 = value1+51
        elif int(value1) == 97:
            text4 = "BERKELIUM"
            value2 = value1+53
        elif int(value1) == 98:
            text4 = "CALIFORNIUM"
            value2 = value1+53
        elif int(value1) == 99:
            text4 = "EINSTEINIUM"
            value2 = value1+54
        elif int(value1) == 100:
            text4 = "FERMIUM"
            value2 = value1+57
        elif int(value1) == 101:
            text4 = "MENDELEVIUM"
            value2 = value1+57
        elif int(value1) == 102:
            text4 = "NOBELIUM"
            value2 = value1+57
        elif int(value1) == 103:
            text4 = "LAWRENCIUM"
            value2 = value1+57
        elif int(value1) == 104:
            text4 = "RUTHERFORDIUM"
            value2 = value1+57
        elif int(value1) == 105:
            text4 = "DUBNIUM"
            value2 = value1+57
        elif int(value1) == 106:
            text4 = "SEABORGIUM"
            value2 = value1+57
        elif int(value1) == 107:
            text4 = "BOHRIUM"
            value2 = value1+55
        elif int(value1) == 108:
            text4 = "HASSIUM"
            value2 = value1+57
        elif int(value1) == 109:
            text4 = "MEITNERIUM"
            value2 = value1+57
        elif int(value1) == 110:
            text4 = "DARMSTADTIUM"
            value2 = value1+59
        elif int(value1) == 111:
            text4 = "ROENTGENIUM"
            value2 = value1+61
        elif int(value1) == 112:
            text4 = "COPERNICIUM"
            value2 = value1+65
        elif int(value1) == 113:
            text4 = "NIHONIUM"
            value2 = value1+75
        elif int(value1) == 114:
            text4 = "FLEROVIUM"
            value2 = value1+75
        elif int(value1) == 115:
            text4 = "MOSCOVIUM"
            value2 = value1+73
        elif int(value1) == 116:
            text4 = "LIVERMORIUM"
            value2 = value1+73
        elif int(value1) == 117:
            text4 = "TENNESSINE"
            value2 = value1+76
        elif int(value1) == 118:
            text4 = "OGANESSON"
            value2 = value1+76
        else:
            text4 = "-"

        #inner_circle = (value1+value2)*70/270+7

        text5 = font2.render(f'element: {text4}', True, (244,244,244))

        screen.blit(text1, (50, 50))
        screen.blit(text2, (50, 100))
        screen.blit(text3, (50, 150))
        screen.blit(text5, (50, 200))

        #inner_circle = value1*0.7

        for ball in balls:
            ball.update()
            ball.draw()

        for bax in balls3:
            #bax.x += random.randint(-2,2)
            #bax.y += random.randint(-2,2)
            bax.update()
            bax.draw()

        for baxx in balls2:
            if (x_half-baxx.x) > inner_circle or (x_half-baxx.x) < -inner_circle:
                x_half
            if (y_half-baxx.y) > inner_circle or (y_half-baxx.y) < -inner_circle:
                y_half
            baxx.update()
            baxx.draw()
    if modus == 1:
        if value1 < 59:
            text1 = font2.render(f'proton: ', True, (244,0,0))
            text2 = font3.render(f'up quarks: 2', True, (0,244,0))
            text3 = font3.render(f'down quarks: 1', True, (144,44,244))
            text5 = font3.render(f'gluons: 8', True, (104,44,144))
            screen.blit(text1, (50, 50))
            screen.blit(text2, (50, 100))
            screen.blit(text3, (50, 150))
            screen.blit(text5, (50, 200))
            pygame.draw.circle(screen, (244,0,0), (width/2,height/2),230)
            pygame.draw.circle(screen, (0,244,0), (width/2-170+random.randint(-7,7),height/2-70),30)
            pygame.draw.circle(screen, (0,244,0), (width/2+70+random.randint(-7,7),height/2-70),30)
            pygame.draw.circle(screen, (144,44,244), (width/2-100+random.randint(-7,7),height/2+70),30)
            
            #pygame.draw.circle(screen, (0,44,144), (width/2+random.randint(-70,70),height/2+random.randint(-70,70)),7)
        
        if value1 >= 59:
            text1 = font2.render(f'neutron: ', True, (170,170,170))
            text2 = font3.render(f'up quarks: 1', True, (0,244,0))
            text3 = font3.render(f'down quarks: 2', True, (144,44,244))
            text5 = font3.render(f'gluons: 8', True, (104,44,144))
            screen.blit(text1, (50, 50))
            screen.blit(text2, (50, 100))
            screen.blit(text3, (50, 150))
            screen.blit(text5, (50, 200))
            pygame.draw.circle(screen, (144,144,144), (width/2,height/2),230)
            pygame.draw.circle(screen, (0,244,0), (width/2-170+random.randint(-7,7),height/2-70),30)
            pygame.draw.circle(screen, (144,44,244), (width/2+70+random.randint(-7,7),height/2-70),30)
            pygame.draw.circle(screen, (144,44,244), (width/2-100+random.randint(-7,7),height/2+70),30)
            
            #pygame.draw.circle(screen, (0,44,144), (width/2+random.randint(-70,70),height/2+random.randint(-70,70)),7)

        if len(balls4) < 8:
            x = width/2-100+random.randint(-100, 100)
            y = height/2-20+random.randint(-100, 100)
            attraction_x = width/2#random.randint(10, width - 100)
            attraction_y = height/2#random.randint(10, height - 100)
            radius = 10
            balls4.append(Ball4(x, y, radius, (attraction_x, attraction_y)))

        for ball in balls4:
            ball.update()
            ball.draw(screen)
        
        clock.tick(60)

    if modus == 2:
        if modi == 1:
            #pygame.draw.circle(screen, (0,244,0), (x_half,y_half),70*value3*7/100)
            #if 10 < value3 < 37:
            screen.blit(image1, (width/2-40-value3*7/2,height/2-30-value3*7/2))
        text1 = font2.render(f'earth: r = 6371000 m', True, (0,244,0))
        text2 = font3.render(f'moon: r =  1737000 m', True, (0,44,244))
        text3 = font3.render(f'sun: r = 696340000 m', True, (244,44,44))
        # distance e_m =    384400000 m
        # distance e_s = 149597870000 m

        screen.blit(text1, (50, 50))
        screen.blit(text2, (50, 100))
        screen.blit(text3, (50, 150))
        if len(balls4) == 8:
            balls4 = []
        for ball in balls4:
            ball.radius = 17*value3*7/100
            if abs(ball.vx) < 0.1:# or abs(ball.vy) < 0.1:
                if modi == 1:
                    modi = 2
                else:
                    modi = 1
            #print(ball.vx)
        
        if len(balls4) < 1:
            x = width/2-200#+random.randint(-100, 100)
            y = height/2-120#+random.randint(-100, 100)
            attraction_x = width/2#random.randint(10, width - 100)
            attraction_y = height/2#random.randint(10, height - 100)
            radius = 17*value3*7/100
            balls4.append(Ball4(x, y, radius, (attraction_x, attraction_y)))
        
        for ball in balls4:
            ball.update()
            ball.draw(screen)
        if modi == 2:
            #pygame.draw.circle(screen, (0,244,0), (x_half,y_half),70*value3*7/100)
            #if 10 < value3 < 30:
            screen.blit(image1, (width/2-40-value3*7/2,height/2-30-value3*7/2))
        pygame.draw.circle(screen, (244,244,0), (x_half,height+y_half),10000/max(1,value3))
        #screen.blit(image2, (0,height-170-value3/10))
        clock.tick(60)
    if modus == 3:
        screen.blit(image, (10,10))

    pygame.draw.rect(screen, (104,144,104), slider_handle_rect2)
    #ballx += random.randint(-2,2)
    #bally += random.randint(-2,2)
    #pygame.draw.circle(screen, (0,244,0), (ballx,bally),7)

    #in1 = input("enter something: ")

    #pygame.draw.line(screen, (0,0,0),(0,0),(0,0))
    #pygame.draw.rect(screen, (0,0,0), (0,0,0,0))
    #pygame.draw.circle(screen, (0,0,0), (0,0),0)
    #pygame.draw.polygon(screen,(0,0,0),((0,0),(0,0),(0,0)),0)

    #text = font.render(f" {777}", True, (0,0,0))
    #screen.blit(text, (350, 350))

    pygame.display.flip()

pygame.quit()