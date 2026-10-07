#atomizer_scalar_7

import pygame
import random
import os

pygame.init()

width, height = 900,700
image = pygame.image.load(os.path.join("universe_filament.png"))
imagi = pygame.image.load(os.path.join("milky_way.png"))
image1 = pygame.image.load(os.path.join("full_earth.png"))
image2 = pygame.image.load(os.path.join("sun1.png"))
image3 = pygame.image.load(os.path.join("moon.png"))
image_ra = pygame.image.load(os.path.join("radioactive.png"))
image = pygame.transform.scale(image, (width-20, height-20))  # Resize the image
imagi = pygame.transform.scale(imagi, (width-20, height-20))  # Resize the image
image1 = pygame.transform.scale(image1, (700, 700))
image2 = pygame.transform.scale(image2, (900, 900))
image3 = pygame.transform.scale(image3, (47, 47))
image_ra = pygame.transform.scale(image_ra, (27, 27))
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
speed = 0.1
ball_color = (0,244,0)

inner_circle = 70

class Ball:                                 ### ELEKTRONS ###
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
        if modus == 4:
            if ((x_half-self.x)**2+(y_half-self.y)**2)**0.5 > inner_circle:
                self.vx *= -1
                self.vy *= -1
        else:
            if self.x < 0 or self.x > width:
                self.vx *= -1
            if self.y < 0 or self.y > height:
                self.vy *= -1
        if modus == 0:
            attraction_point = (width//2,height//2)
            # Calculate the attraction force
            ax, ay = attraction_point
            dx = ax - self.x
            dy = ay - self.y
            dist = max((dx**2 + dy**2)**0.5, 1)  # Prevent division by zero
            force = 0.01  # Adjust this value for stronger or weaker attraction
            
            # Acceleration proportional to the force
            ax = (force * dx) / dist
            ay = (force * dy) / dist

            # Update velocity
            self.vx += ax
            self.vy += ay

            # Update position
            self.x += self.vx
            self.y += self.vy

    def draw(self):
        pygame.draw.circle(screen, ball_color, (int(self.x), int(self.y)), int(self.radius))
        photon = random.randint(0,100)
        if photon == 1:
            pygame.draw.line(screen, (207,144,20),(int(self.x), int(self.y)),(int(width/2),int(height/2)))

balls2 = []
balls3 = []
balls5 = []
balls6 = []
balls7 = []
speed2 = 0.1
speed3 = 0.04
ball_color2 = (244,0,0)
ball_color3 = (144,144,144)
ball_color_u = (0,177,0)
ball_color_d = (0,0,233)

x_half = width/2
y_half = height/2

class Ball2:                            ### PROTONS ###
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
        if modus == 4:
            if ((x_half-self.x)**2+(y_half-self.y)**2)**0.5 > 27:
                self.vx *= -1
                self.vy *= -1
        else:    
            if ((x_half-self.x)**2+(y_half-self.y)**2)**0.5 > inner_circle:
                self.vx *= -1
                self.vy *= -1

    def draw(self):
        if modus == 0:
            fact = max(value3**2/270-10,0.7)#value3*7/270
        else:
            fact = value3*7/270#(value3**2*7/270+value3*7/270)/2
        pygame.draw.circle(screen, ball_color2, (int(self.x), int(self.y)), int(self.radius)*fact)
        pygame.draw.circle(screen, ball_color_u, (int(self.x-4*fact), int(self.y-3*fact)), int(self.radius/3)*fact)
        pygame.draw.circle(screen, ball_color_u, (int(self.x+4*fact), int(self.y-3*fact)), int(self.radius/3)*fact)
        pygame.draw.circle(screen, ball_color_d, (int(self.x), int(self.y+4*fact)), int(self.radius/4)*fact)

class Ball3:                                    ### NEUTRONS ###
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
        if modus == 4:
            if ((x_half-self.x)**2+(y_half-self.y)**2)**0.5 > 27:
                self.vx *= -1
                self.vy *= -1
        else:
            if ((x_half-self.x)**2+(y_half-self.y)**2)**0.5 > 70:
                self.vx *= -1
                self.vy *= -1

    def draw(self):
        if modus == 0:
            fact = max(value3**2/270-10,0.7)#value3*7/270
        else:
            fact = value3*7/270
        pygame.draw.circle(screen, ball_color3, (int(self.x), int(self.y)), int(self.radius)*fact)
        pygame.draw.circle(screen, ball_color_u, (int(self.x-4*fact), int(self.y-3*fact)), int(self.radius/3)*fact)
        pygame.draw.circle(screen, ball_color_d, (int(self.x+4*fact), int(self.y-3*fact)), int(self.radius/4)*fact)
        pygame.draw.circle(screen, ball_color_d, (int(self.x), int(self.y+4*fact)), int(self.radius/4)*fact)

modi = 1
global siner,sinc
siner = 1
sinc = 1
# Ball class
class Ball4:                                                ### GLUONS/MOON ###
    def __init__(self, x, y, radius, attraction_point):
        self.x = x # x
        self.y = x # y
        self.radius = radius
        self.attraction_point = attraction_point
        self.vx = random.randint(1,10)/10 # 1
        self.vy = random.randint(1,10)/10 # 0.7

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
        global siner,sinc
        if modus == 2:
            pygame.draw.circle(screen, (40,40,40), (int(self.x), int(self.y)), self.radius)
        else:
            if random.randint(0,4) == 0:
                siner += sinc
            if siner > 20:
                siner -= 1
                sinc *=-1
            if siner < 0:
                siner += 1
                sinc *=-1
            pygame.draw.circle(screen, (0,40,144), (int(self.x), int(self.y)), self.radius-2+siner//4)
        # Draw attraction point
        #pygame.draw.circle(screen, WHITE, (int(self.attraction_point[0]), int(self.attraction_point[1])), 3)
speed4 = 0.11
# Create 8 balls with random positions and attraction points
balls4 = []
for _ in range(8):
    x = width/2-100+random.randint(-100, 100)
    y = height/2-20+random.randint(-100, 100)
    attraction_x = width/2#random.randint(10, width - 100)
    attraction_y = height/2#random.randint(10, height - 100)
    radius = 10
    balls4.append(Ball4(x, y, radius, (attraction_x, attraction_y)))

class Ball5:                                    ### PROTONS H2O ###
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.growing = True
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)+random.randint(-1,1)
        self.lining = True
    
    def update(self):
        global speed4
        self.x += self.vx*speed4
        self.y += self.vy*speed4 #self.vy+self.vy*trash_1 #+random.randint(0,2)
        if self.x < 0 or self.x > width:
            self.vx *= -1
        if self.y < 0 or self.y > height:
            self.vy *= -1

    def draw(self):
        fact = value3*7/270

        pygame.draw.line(screen, (0,233,0),(int(self.x), int(self.y)),(width/2+random.randint(-7,7),height/2+random.randint(-7,7)))

        pygame.draw.circle(screen, (0,233,0), (int(self.x), int(self.y)), int(self.radius)*fact*2)
        pygame.draw.circle(screen, (0,0,0), (int(self.x), int(self.y)), int(self.radius)*fact*2-2)

        pygame.draw.circle(screen, ball_color2, (int(self.x), int(self.y)), int(self.radius)*fact)
        pygame.draw.circle(screen, ball_color_u, (int(self.x-4*fact), int(self.y-3*fact)), int(self.radius/3)*fact)
        pygame.draw.circle(screen, ball_color_u, (int(self.x+4*fact), int(self.y-3*fact)), int(self.radius/4)*fact)
        pygame.draw.circle(screen, ball_color_d, (int(self.x), int(self.y+4*fact)), int(self.radius/4)*fact)

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
mol_mode = 1

e_conf = 0
n_conf = 0
p_conf = 0

clock = pygame.time.Clock()
density_own = 0
capa = 0

e_rect1 = pygame.Rect(202,103,12,14)
e_rect2 = pygame.Rect(225,103,12,14)

n_rect1 = pygame.Rect(202,153,12,14)
n_rect2 = pygame.Rect(225,153,12,14)

text77 = "-"
text11 = "-"
radioactive = False
decay_rect = pygame.Rect(50,300,90,20)
decay = 3
change = False
old_n = 0
ttt = 0

specialis = [(1,0),(1,1),(2,1),(2,2),(3,3),(3,4),(4,5),(5,5),
            (5,6),(6,6),(6,7),(7,7),(7,8),(8,8),(8,9),(8,10),
            (9,10),(10,10),(10,11),(10,12),(11,12),(12,13),(12,14),(13,14),
            (14,14),(14,15),(14,16),(15,16),(16,16),(16,17),(16,18),(16,20),
            (17,18),(17,20),(18,18),(18,20),(18,22),(19,20),(19,22),(20,22),
            (20,23),(20,24),(21,24),(22,24),(22,25),(22,26),(22,27),(22,28),
            (23,28),(24,28),(24,29),(24,30),(25,30),(26,28),(26,30),(26,31),
            (26,32),(27,32),(28,32),(28,30),(28,33),(28,34),(28,36),(29,36),
            (29,34),(30,34),(30,36),(30,37),(30,38),(31,38),(31,40),(32,40),
            (32,38),(32,41),(32,42),(33,42),(34,42),(34,40),(34,43),(34,44),
            (35,44),(35,46),(36,44),(36,46),(36,47),(36,48),(36,50),(37,48),
            (38,46),(38,48),(38,49),(38,50),(39,50),(40,50),(40,51),(40,52),
            (40,54),(41,52),(42,50),(42,52),(42,53),(42,54),(42,55),(42,56),(43,55),
            (44,52),(44,54),(44,55),(44,56),(44,57),(44,58),(44,60),(45,58),
            (46,58),(46,56),(46,59),(46,60),(46,62),(46,64),(47,62),(47,60),
            (48,62),(48,63),(48,64),(49,64),(50,62),(50,64),(50,65),(50,66),
            (50,67),(50,68),(50,69),(50,70),(50,72),(50,74),(51,72),(51,70),
            (52,70),(52,72),(52,73),(52,74),(53,74),(54,72),(54,74),(54,75),
            (54,76),(54,77),(54,78),(55,78),(56,78),(56,79),(56,80),(56,81),
            (56,82),(57,82),(58,82),(59,82),(60,82),(60,83),(60,85),(60,86),
            (60,88),(62,82),(62,87),(62,88),(62,90),(62,92),(63,88),(63,90),
            (64,90),(64,91),(64,92),(64,93),(64,94),(65,94),(66,94),(66,90),
            (66,92),(66,95),(66,96),(66,98),(67,98),(68,98),(68,94),(68,96),
            (68,99),(68,100),(68,102),(69,100),(70,100),(70,98),(70,101),(70,102),
            (70,103),(70,104),(70,106),(71,104),(72,104),(72,105),(72,106),(72,107),
            (72,108),(73,108),(75,110),(76,111),(76,112),(76,113),(76,114),(76,116),
            (77,116),(77,114),(78,114),(78,116),(78,117),(78,118),(78,120),(79,118),
            (80,118),(80,116),(80,119),(80,120),(80,121),(80,122),(80,124),(81,124),
            (81,122),(82,124),(82,125),(82,126),(83,126)] #,(),(),(),(),(),(),(),()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mx,my = mouse_pos[0],mouse_pos[1]
            print(mx,my)
            if decay_rect.collidepoint(event.pos):
                #print(old_n)
                old_n = dn2
                if decay == 1 or ttt == 2: 
                    old_n = old_n-1
                    #e_conf += 1
                    #n_conf -= 1 # int(2+value1/118)
                    #-(1.77*value1-17+0.008*(value1+40)**2)/(2*value1)
                    p_conf += 1
                    change = True
                if decay == 0 or ttt == 1:
                    old_n = old_n+1
                    #e_conf -= 1
                    #n_conf += 1 #int(2+value1/118)
                    p_conf -= 1 
                    change = True
                if decay == 2 or ttt == 3:
                    old_n = old_n-2
                    #n_conf -= 4
                    p_conf -= 2
                    change = True
                text11 = ""
            print(value1,value2,old_n,p_conf,n_conf)
            if slider_handle_rect1.collidepoint(event.pos):
                dragging1 = True
                e_conf = 0
                n_conf = 0
                p_conf = 0
            if slider_handle_rect2.collidepoint(event.pos):
                dragging2 = True
                e_conf = 0
                n_conf = 0
                p_conf = 0
            if e_rect1.collidepoint(event.pos):
                e_conf -= 1
            if e_rect2.collidepoint(event.pos):
                e_conf += 1
            if n_rect1.collidepoint(event.pos):
                n_conf -= 1
            if n_rect2.collidepoint(event.pos):
                n_conf += 1
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if modus == 2:
                image1 = pygame.image.load(os.path.join("full_earth.png"))
                #image1 = pygame.transform.smoothscale(image1, (70+value3*7,70+value3*7))
                image1 = pygame.transform.scale(image1, (70+value3*7,70+value3*7))
                #image2 = pygame.image.load(os.path.join("sun1.png"))
                #image2 = pygame.transform.scale(image2, (10000/max(1,value3),10000/max(1,value3)))
                #image2 = pygame.transform.scale(image2, (600+value3*27,600+value3*27)) #700+value3*17,700+value3*17
            
            value1 = (118 -(slider_handle_rect1.y - slider_bar_rect1.top) / (slider_bar_rect1.height - slider_handle_rect1.height) * 118)
            value3 = (100 -(slider_handle_rect2.y - slider_bar_rect2.top) / (slider_bar_rect2.height - slider_handle_rect2.height) * 100)
            balls = []
            balls2 = []
            balls3 = []
            if modus == 4:
                speed = value1/20
                speed2 = value1/170
                speed3 = value1/170
                speed4 = value1/170
            else:
                speed2 = 0.1
                speed3 = 0.04
                speed = 1
                speed4 = 0.11
                t = 1
                if modus == 0:
                    if p_conf != 0:
                        print(p_conf,old_n,n_conf)
                        if p_conf < 0:
                            while t < old_n+n_conf-p_conf:
                                balls3.append(Ball3(width/2, height/2, 12))
                                t += 1
                        else:
                            while t < old_n+n_conf+p_conf:
                                balls3.append(Ball3(width/2, height/2, 12))
                                t += 1
                    else:
                        while t < value2+n_conf:
                            balls3.append(Ball3(width/2, height/2, 12))
                            t += 1
                else:
                    while t < value2:
                        balls3.append(Ball3(width/2, height/2, 12))
                        t += 1
                t = 1
                
                if modus == 4:
                    while t < 8:
                        balls.append(Ball(random.randint(0, width), random.randint(0, height), random.randint(4,7)))
                        balls2.append(Ball2(width/2, height/2, 12))
                        t += 1
                else:
                    t = 1
                    if modus == 0:
                        while t < value1+e_conf:
                            balls.append(Ball(random.randint(0, width), random.randint(0, height), random.randint(4,7)))
                            t += 1
                    else:
                        while t < value1:
                            balls.append(Ball(random.randint(0, width), random.randint(0, height), random.randint(4,7)))
                            t += 1
                    t = 1    
                    while t < value1+p_conf:
                        balls2.append(Ball2(width/2, height/2, 12))
                        t += 1
            dragging1 = False
            dragging2 = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            print(event.w,event.h)
        elif event.type == pygame.MOUSEMOTION:
            if modus == 4:
                if modus == 4:
                    speed = value1/20
                    speed2 = value1/170
                    speed3 = value1/170
                    speed4 = value1/170
                else:
                    speed2 = 0.1
                    speed3 = 0.04
                    speed = 1
                    speed4 = 0.11
                temp = value1
                density_own = ((-0.0037*(temp+7.7)**2+1000)+(-0.00007*(7.7*temp)**2+1000))/2
                if 1<=temp<=2 or 6<=temp<=7:
                    density_own = 999.84
                if 2<=temp<=3 or 5<=temp<=6:
                    density_own = 999.89
                if 3<=temp<=4 or 4<=temp<=5:
                    density_own = 999.9
                if temp == 4:
                    density_own = 999.93
                if 100<temp<103:
                    density_own = ((-0.0037*(100+7.7)**2+1000)+(-0.00007*(7.7*100)**2+1000))/2

                if 0<=temp<=39:  
                    capa = 0.0000067*(temp-50)**4+4178.7
                elif 39<=temp<=42:
                    capa = ((0.0114*(temp-43)**2+4179)+(0.0000067*(temp-50)**4+4178.7))/2
                elif 42<temp<100: 
                    capa = 0.0114*(temp-43)**2+4179
                elif 100<temp<103:
                    capa = 0.0114*(100-43)**2+4179
                else:
                    capa = 0.0114*(temp-43)**2+4179
                #if temp == 0:
                #    capa = 2090    
            if dragging1:
                mouse_y = event.pos[1]
                handle_y = max(slider_bar_rect1.top, min(mouse_y, slider_bar_rect1.bottom - slider_handle_rect1.height))
                slider_handle_rect1.y = handle_y
            if dragging2:
                mouse_y = event.pos[1]
                handle_y = max(slider_bar_rect2.top, min(mouse_y, slider_bar_rect2.bottom - slider_handle_rect2.height))
                slider_handle_rect2.y = handle_y
                if modus == 2:
                    image1 = pygame.image.load(os.path.join("full_earth.png"))
                    #image2 = pygame.image.load(os.path.join("sun1.png"))
                    image1 = pygame.transform.scale(image1, (70+value3*7,70+value3*7))
                    #image2 = pygame.transform.scale(image2, (600+value3*27,600+value3*27))
                    #lol = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                value3 += 2
            if event.key == pygame.K_DOWN:
                value3 -= 2
            if event.key == pygame.K_RIGHT:
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
            if event.key == pygame.K_LEFT:
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
            if event.key == pygame.K_m:
                balls = []
                balls2 = []
                balls3 = []
                balls5 = []
                mol_mode += 1
                if mol_mode >2:
                    mol_mode = 1 

    screen.fill((0,0,0))
    if modus == 2 or modus == 3 or modus == 5:
        starstripes = True
    else:
        starstripes = False
    if starstripes == True:
        randy = random.randint(0,200)
        if randy < 4:
            ssx = random.randint(0,width-200)
            ssy = random.randint(0,height)
            ssx2 = 70#*random.randint(0,20)
            ssy2 = 20#*random.randint(0,20)
            pygame.draw.line(screen, (244,244,244),(ssx,ssy),(ssx+ssx2,ssy-ssy2))

    # SLIDERS
    if modus != 2:
        pygame.draw.rect(screen, (44,44,44), slider_bar_rect1)
        pygame.draw.rect(screen, (244,0,0), slider_handle_rect1)
    pygame.draw.rect(screen, (44,44,44), slider_bar_rect2)
    pygame.draw.rect(screen, (104,144,104), slider_handle_rect2)
    #pygame.draw.rect(screen, (104,144,104), decay_rect)

    if dragging1 == True:
        value1 = (118 - (slider_handle_rect1.y - slider_bar_rect1.top) / (slider_bar_rect1.height - slider_handle_rect1.height) * 118)
    if dragging2 == True:
        value3 = 100 - (slider_handle_rect2.y - slider_bar_rect2.top) / (slider_bar_rect2.height - slider_handle_rect2.height) * 100
    if value3 > 77:
        modus = 1               # quarks
        for ball in balls4:
            ball.radius = 7
    elif 27 < value3 <= 37:     # molecules
        modus = 4        
    elif 7 <= value3 <= 27:     # sonne mond erde
        modus = 2
    elif 2 <= value3 <= 7:      # milky way
        modus = 5
    elif value3 < 2: #7         # filament
        modus = 3
    else:
        modus = 0
    if modus == 0:              # atoms
        if radioactive == True:
            if text11 != "stable":
                #if text77 == "radioactive":
                screen.blit(image_ra, (50,250))
        pygame.draw.polygon(screen,(0,77,0),((202,110),(215,117),(215,103)),0)
        pygame.draw.polygon(screen,(0,77,0),((237,110),(225,117),(225,103)),0)
        pygame.draw.polygon(screen,(44,44,44),((202,160),(215,167),(215,153)),0)
        pygame.draw.polygon(screen,(44,44,44),((237,160),(225,167),(225,153)),0)
        text1 = font2.render(f'protons: {int(value1)+p_conf}', True, (244,0,0))
        text2 = font3.render(f'electrons: {int(value1+e_conf)}', True, (0,244,0))
        text3 = font3.render(f'neutrons: {int(value2+n_conf)}', True, (144,144,144))
        text77 = "solid"
        text11 = "stable"
        if int(value1+p_conf) == 0:
            text4 = "-"
            value2 = 0
        if int(value1+p_conf) == 1:
            if n_conf == 0:
                text4 = "PROTIUM/HYDROGENIUM"
            elif n_conf == 1:
                text4 = "DEUTERIUM"
            elif n_conf == 2:
                text4 = "TRITIUM"
            else:
                text4 = "HYDROGENIUM"
            text77 = "gas"
            value2 = value1-1
        elif int(value1+p_conf) == 2:
            text4 = "HELIUM"
            value2 = value1
            text77 = "gas"
        elif int(value1+p_conf) == 3:
            text4 = "LITHIUM"
            value2 = value1+1
        elif int(value1+p_conf) == 4:
            text4 = "BERYLLIUM"
            value2 = value1+1
        elif int(value1+p_conf) == 5:
            text4 = "BORON"
            value2 = value1+1
        elif int(value1+p_conf) == 6:
            text4 = "CARBON/KOHLENSTOFF"
            value2 = value1
        elif int(value1+p_conf) == 7:
            text4 = "NITROGENIUM/STICKSTOFF"
            value2 = value1
            text77 = "gas"
        elif int(value1+p_conf) == 8:
            text4 = "OXYGENIUM/SAUERSTOFF"
            value2 = value1
            text77 = "gas"
        elif int(value1+p_conf) == 9:
            text4 = "FLOUR"
            value2 = value1+1
            text77 = "gas"
        elif int(value1+p_conf) == 10:
            text4 = "NEON"
            value2 = value1
            text77 = "gas"
        elif int(value1+p_conf) == 11:
            text4 = "SODIUM/NATRIUM"
            value2 = value1+1
        elif int(value1+p_conf) == 12:
            text4 = "MAGNESIUM"
            value2 = value1
        elif int(value1+p_conf) == 13:
            text4 = "ALUMINIUM"
            value2 = value1+1
        elif int(value1+p_conf) == 14:
            text4 = "SILIZIUM/SILICON"
            value2 = value1
        elif int(value1+p_conf) == 15:
            text4 = "PHOSPHOROUS"
            value2 = value1+1
        elif int(value1+p_conf) == 16:
            text4 = "SULFUR"
            value2 = value1
        elif int(value1+p_conf) == 17:
            text4 = "CHLORINE"
            value2 = value1+1
            text77 = "gas"
        elif int(value1+p_conf) == 18:
            text4 = "ARGON"
            value2 = value1+4
            text77 = "gas"
        elif int(value1+p_conf) == 19:
            text4 = "KALIUM/POTASSIUM"
            value2 = value1+1
        elif int(value1+p_conf) == 20:
            text4 = "CALCIUM"
            value2 = value1
        elif int(value1+p_conf) == 21:
            text4 = "SCANDIUM"    
            value2 = value1+3
        elif int(value1+p_conf) == 22:
            text4 = "TITANIUM"
            value2 = value1+2
        elif int(value1+p_conf) == 23:
            text4 = "VANADIUM"
            value2 = value1+5
        elif int(value1+p_conf) == 24:
            text4 = "CHROMIUM"
            value2 = value1+4
        elif int(value1+p_conf) == 25:
            text4 = "MANGANESE"
            value2 = value1+5    
        elif int(value1+p_conf) == 26:
            text4 = "FERRUM"
            value2 = value1+4
        elif int(value1+p_conf) == 27:
            text4 = "COBALT"
            value2 = value1+5
        elif int(value1+p_conf) == 28:
            text4 = "NICKEL"
            value2 = value1+2
        elif int(value1+p_conf) == 29:
            text4 = "CUPRUM/COPPER/KUPFER"
            value2 = value1+5
        elif int(value1+p_conf) == 30:
            text4 = "ZINC"
            value2 = value1+4
        elif int(value1+p_conf) == 31:
            text4 = "GALLIUM"
            value2 = value1+8
        elif int(value1+p_conf) == 32:
            text4 = "GERMANIUM"
            value2 = value1+7
        elif int(value1+p_conf) == 33:
            text4 = "ARSENIC"
            value2 = value1+9
        elif int(value1+p_conf) == 34:
            text4 = "SELENIUM"
            value2 = value1+10
        elif int(value1+p_conf) == 35:
            text4 = "BROMINE"
            value2 = value1+10
            text77 = "liquid"
        elif int(value1+p_conf) == 36:
            text4 = "KRYPTON"
            value2 = value1+12
            text77 = "gas"
        elif int(value1+p_conf) == 37:
            text4 = "RUBIDIUM"
            value2 = value1+11
        elif int(value1+p_conf) == 38:
            text4 = "STRONTIUM"
            value2 = value1+12
        elif int(value1+p_conf) == 39:
            text4 = "YTTRIUM"
            value2 = value1+11
        elif int(value1+p_conf) == 40:
            text4 = "ZIRCONIUM"
            value2 = value1+10
        elif int(value1+p_conf) == 41:
            text4 = "NIOBIUM"
            value2 = value1+11
        elif int(value1+p_conf) == 42:
            text4 = "MOLYBDENUM"
            value2 = value1+14
        elif int(value1+p_conf) == 43:
            text4 = "TECHNECIUM"
            value2 = value1+12
            text11 = "β- decay"
        elif int(value1+p_conf) == 44:
            text4 = "RUTHENIUM"
            value2 = value1+14
        elif int(value1+p_conf) == 45:
            text4 = "RHODIUM"
            value2 = value1+13
        elif int(value1+p_conf) == 46:
            text4 = "PALLADIUM"
            value2 = value1+14
        elif int(value1+p_conf) == 47:
            text4 = "ARGENTIUM/SILVER"
            value2 = value1+13
        elif int(value1+p_conf) == 48:
            text4 = "CADMIUM"
            value2 = value1+14
        elif int(value1+p_conf) == 49:
            text4 = "INDIUM"
            value2 = value1+17
        elif int(value1+p_conf) == 50:
            text4 = "ZINN/TIN/STANNUM"
            value2 = value1+20
        elif int(value1+p_conf) == 51:
            text4 = "ANTIMONY"
            value2 = value1+19
        elif int(value1+p_conf) == 52:
            text4 = "TELLURIUM"
            value2 = value1+26
        elif int(value1+p_conf) == 53:
            text4 = "IODINE"
            value2 = value1+21
        elif int(value1+p_conf) == 54:
            text4 = "XENON"
            value2 = value1+24
            text77 = "gas"
        elif int(value1+p_conf) == 55:
            text4 = "CAESIUM"
            value2 = value1+23
        elif int(value1+p_conf) == 56:
            text4 = "BARIUM"
            value2 = value1+26
        elif int(value1+p_conf) == 57:
            text4 = "LANTHAN"
            value2 = value1+25
        elif int(value1+p_conf) == 58:
            text4 = "CERIUM"
            value2 = value1+24
        elif int(value1+p_conf) == 59:
            text4 = "PRASEODYMIUM"
            value2 = value1+23
        elif int(value1+p_conf) == 60:
            text4 = "NEODYMIUM"
            value2 = value1+22
        elif int(value1+p_conf) == 61:
            text4 = "PROMETHIUM"
            value2 = value1+23
        elif int(value1+p_conf) == 62:
            text4 = "SAMARIUM"
            value2 = value1+28
        elif int(value1+p_conf) == 63:
            text4 = "EUROPIUM"
            value2 = value1+27
        elif int(value1+p_conf) == 64:
            text4 = "GADOLINIUM"
            value2 = value1+30
        elif int(value1+p_conf) == 65:
            text4 = "TERBIUM"
            value2 = value1+29
        elif int(value1+p_conf) == 66:
            text4 = "DYSPROSIUM"
            value2 = value1+32
        elif int(value1+p_conf) == 67:
            text4 = "HOLMIUM"
            value2 = value1+31
        elif int(value1+p_conf) == 68:
            text4 = "ERBIUM"
            value2 = value1+30
        elif int(value1+p_conf) == 69:
            text4 = "THULIUM"
            value2 = value1+31
        elif int(value1+p_conf) == 70:
            text4 = "YTTERBIUM"
            value2 = value1+34
        elif int(value1+p_conf) == 71:
            text4 = "LUTETIUM"
            value2 = value1+33
        elif int(value1+p_conf) == 72:
            text4 = "HAFNIUM"
            value2 = value1+36
        elif int(value1+p_conf) == 73:
            text4 = "TANTAL"
            value2 = value1+35
        elif int(value1+p_conf) == 74:
            text4 = "WOLFRAM/TUNGSTEN"
            value2 = value1+36
            text11 = "α decay"
        elif int(value1+p_conf) == 75:
            text4 = "RHENIUM"
            value2 = value1+37
            text11 = "β- decay"
            if n_conf != -2:
                text77 = "radioactive"
        elif int(value1+p_conf) == 76:
            text4 = "OSMIUM"
            value2 = value1+40
        elif int(value1+p_conf) == 77:
            text4 = "IRIDIUM"
            value2 = value1+39
        elif int(value1+p_conf) == 78:
            text4 = "PLATIN"
            value2 = value1+39
        elif int(value1+p_conf) == 79:
            text4 = "AURUM/GOLD"
            value2 = 118
        elif int(value1+p_conf) == 80:
            text4 = "HYDRARGYRUM/MERCURY/QUECKSILBER"
            value2 = value1+42
            text77 = "liquid"
        elif int(value1+p_conf) == 81:
            text4 = "THALIUM"
            value2 = value1+43
        elif int(value1+p_conf) == 82:
            text4 = "PLUMBUM/LEAD/BLEI"
            value2 = value1+44
        elif int(value1+p_conf) == 83:
            text4 = "BISMUTH"
            value2 = value1+43
        elif int(value1+p_conf) == 84:
            text4 = "POLONIUM"
            value2 = value1+40
        elif int(value1+p_conf) == 85:
            text4 = "ASTATINE"
            value2 = value1+40
        elif int(value1+p_conf) == 86:
            text4 = "RADON"
            value2 = value1+38
            text77 = "gas"
        elif int(value1+p_conf) == 87:
            text4 = "FRANCIUM"
            value2 = value1+38
        elif int(value1+p_conf) == 88:
            text4 = "RADIUM"
            value2 = value1+50
        elif int(value1+p_conf) == 89:
            text4 = "ACTINIUM"
            value2 = value1+47
        elif int(value1+p_conf) == 90:
            text4 = "THORIUM"
            value2 = value1+52
        elif int(value1+p_conf) == 91:
            text4 = "PROTACTINIUM"
            value2 = value1+49
        elif int(value1+p_conf) == 92:
            text4 = "URANIUM"
            value2 = value1+54
        elif int(value1+p_conf) == 93:
            text4 = "NEPTUNIUM"
            value2 = value1+50
        elif int(value1+p_conf) == 94:
            text4 = "PLUTONIUM"
            value2 = value1+50
        elif int(value1+p_conf) == 95:
            text4 = "AMERICIUM"
            value2 = value1+51
        elif int(value1+p_conf) == 96:
            text4 = "CURIUM"
            value2 = value1+51
        elif int(value1+p_conf) == 97:
            text4 = "BERKELIUM"
            value2 = value1+53
        elif int(value1+p_conf) == 98:
            text4 = "CALIFORNIUM"
            value2 = value1+53
        elif int(value1+p_conf) == 99:
            text4 = "EINSTEINIUM"
            value2 = value1+54
        elif int(value1+p_conf) == 100:
            text4 = "FERMIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 101:
            text4 = "MENDELEVIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 102:
            text4 = "NOBELIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 103:
            text4 = "LAWRENCIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 104:
            text4 = "RUTHERFORDIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 105:
            text4 = "DUBNIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 106:
            text4 = "SEABORGIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 107:
            text4 = "BOHRIUM"
            value2 = value1+55
        elif int(value1+p_conf) == 108:
            text4 = "HASSIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 109:
            text4 = "MEITNERIUM"
            value2 = value1+57
        elif int(value1+p_conf) == 110:
            text4 = "DARMSTADTIUM"
            value2 = value1+59
        elif int(value1+p_conf) == 111:
            text4 = "ROENTGENIUM"
            value2 = value1+61
        elif int(value1+p_conf) == 112:
            text4 = "COPERNICIUM"
            value2 = value1+65
        elif int(value1+p_conf) == 113:
            text4 = "NIHONIUM"
            value2 = value1+75
        elif int(value1+p_conf) == 114:
            text4 = "FLEROVIUM"
            value2 = value1+75
        elif int(value1+p_conf) == 115:
            text4 = "MOSCOVIUM"
            value2 = value1+73
        elif int(value1+p_conf) == 116:
            text4 = "LIVERMORIUM"
            value2 = value1+73
        elif int(value1+p_conf) == 117:
            text4 = "TENNESSINE"
            value2 = value1+76
        elif int(value1+p_conf) == 118:
            text4 = "OGANESSON"
            value2 = value1+76
        else:
            text4 = "-"

        if p_conf != 0:
            #text4 += " ISOTOPE" 
            value2 = old_n
            if change == True:
                n_conf = value2-old_n
                change = False
            
        #if change == True:
        #    n_conf = old_n-value2
        #    change = False

        dn1 = int(value1+p_conf)
        #dn2 = int(value2+p_conf)+n_conf
        dn2 = int(value2)+n_conf
        dnx = (dn1,dn2)

        if e_conf < 0:
            text4 += " KATION"
        if e_conf > 0:
            text4 += " ANION"
        if n_conf != 0:  # and dnx not in specialis:
            text4 += " ISOTOPE"

        if int(value1+p_conf) >= 84 or int(value1+p_conf) == 43 or int(value1+p_conf) == 61:
            text77 = "radioactive"
            radioactive = True
        else:
            radioactive = False 

        if dnx in specialis:
            text11 = "stable"
            ttt = 0
            radioactive = False
        else:
            decay = 3
            #text77 = "radioactive"
            radioactive = True
            if n_conf < 0:
                text11 = "β+ decay"
                ttt = 1
                decay = 0
                text77 = "radioactive"
            if n_conf > 0:
                text11 = "β− decay"
                ttt = 2
                decay = 1
                text77 = "radioactive"
            if value1 > 83 or value1 == 74:
                if n_conf == 0:
                    ttt = 3
                    text11 = "α decay"
                    decay = 2
                    text77 = "radioactive"
        if dnx == (18,21) or dnx == (28,31) or dnx == (29,35) or dnx == (30,35) or dnx == (75,112) or dnx == (43,55) or dnx == (61,84):
            text11 = "β- decay"
            ttt = 2
            text77 = "radioactive"

        # Ar, Ni, Cu, Zn, Tc, Pm, W

        # beta- : n -> p + e- + antineutrino
        # beta+ : p -> n + e+ + neutrino
        # alpha : helium (2 proton, 2 neutron)
        
        #inner_circle = (value1+value2)*70/270+7

        text5 = font2.render(f'element: {text4}', True, (244,244,244))
        if text77 == "gas":
            t7c = (77,11,11)
        elif text77 == "liquid":
            t7c = (66,66,177)
        elif text77 == "radioactive":
            radioactive = True
            t7c = (44,44,44)
        else:
            t7c = (11,77,11)
            radioactive = False
        #if text77 != "radioactive":
        text77 = font3.render(f'{text77}', True, t7c)

        if ttt == 0:
            text11 = font3.render(f'{text11}', True, (77,77,77))
            radioactive = False
        elif ttt == 2:
            radioactive = True
            #text11 = font3.render(f'{text11}', True, (101,147,11))
            text11 = font3.render(f'{text11}', True, (11,77,111))
        elif ttt == 1:
            radioactive = True
            text11 = font3.render(f'{text11}', True, (11,77,111))
        elif ttt == 3:
            radioactive = True
            text11 = font3.render(f'{text11}', True, (229,190,1))

        screen.blit(text1, (50, 50))
        screen.blit(text2, (50, 100))
        screen.blit(text3, (50, 150))
        screen.blit(text5, (50, 200))
        screen.blit(text11, (50, 300))
        #if value1 < 84 and int(value1+p_conf) not in [75,43,61]:
        #   if text77 != "radioactive":
        if radioactive == False:    
            screen.blit(text77, (50, 250))
        #else:
        #    screen.blit(text77, (50, 350))
        #inner_circle = value1*0.7

        for ball in balls:
            ball.update()
            ball.draw()

        xxx = random.randint(0,1)
        if xxx == 0:
            for bax in balls3:
                #bax.x += random.randint(-2,2)
                #bax.y += random.randint(-2,2)
                bax.update()
                bax.draw()
            for baxx in balls2:
                #if (x_half-baxx.x) > inner_circle or (x_half-baxx.x) < -inner_circle:
                #    baxx.x = x_half
                #if (y_half-baxx.y) > inner_circle or (y_half-baxx.y) < -inner_circle:
                #    baxx.y = y_half 
                baxx.update()
                baxx.draw()
        else:
            for bax in balls2:
                bax.update()
                bax.draw()
            for baxx in balls3:
                baxx.update()
                baxx.draw()
    if modus == 1:
        if value1 >= 59: 
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
        
        if value1 < 59:
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
        #if modi == 1:
            #pygame.draw.circle(screen, (0,244,0), (x_half,y_half),70*value3*7/100)
            #if 10 < value3 < 37:
        screen.blit(image1, (width/2-40-value3*7/2,height/2-30-value3*7/2))
        screen.blit(image2, (0,value3*77/2))
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
            #if abs(ball.vx) < 0.1:# or abs(ball.vy) < 0.1:
            #    if modi == 1:
            #        modi = 2
            #    else:
            #        modi = 1
            if ball.vx > 0:
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
            #ball.draw(screen)
            screen.blit(image3, (ball.x-23,ball.y-23))

        if modi == 2:
            #pygame.draw.circle(screen, (0,244,0), (x_half,y_half),70*value3*7/100)
            #if 10 < value3 < 30:
            screen.blit(image1, (width/2-40-value3*7/2,height/2-30-value3*7/2))
        screen.blit(image2, (0,value3*77/2))
        #pygame.draw.circle(screen, (244,144,0), (x_half,height+y_half),10000/max(1,value3)) # SUN?
        #screen.blit(image2, (0,height-170-value3/10))
        clock.tick(60)
    if modus == 3:
        screen.blit(image, (10,10))
    if modus == 5:
        screen.blit(imagi, (10,10))

    if modus == 4:
        temp = int(value1*100)/100

        if mol_mode == 1:
            text1 = font2.render(f'water: H2O', True, (20,20,233))
            text4 = font3.render(f'electrons: 10', True, (0,233,0))
            text2 = font3.render(f'up quarks: 28', True, (233,0,0))
            text3 = font3.render(f'down quarks: 26', True, (144,44,244))
            text5 = font3.render(f'gluons: 144', True, (104,44,144))

            text8 = font3.render(f'enthalpy of crystallization: 334 kJ/kg', True, (44,44,44)) # 6 kJ/mol 420
            text9 = font3.render(f'enthalpy of vaporization: 2257 kJ/kg', True, (44,44,44)) # 2501
            text10 = font3.render(f'molar mass: 18.015 g/mol', True, (44,44,44)) # 2501
            # 1000g = 1000g*6.02214076×10^23*mol/18 mol*g
            
            density = int(density_own*100)/100  
            if temp == 0:
                text6 = font3.render(f'density({temp}°C): {density} kg/m^3 ~> ice: 917 kg/m^3', True, (144,144,144))
            elif 100 < temp < 103:
                text6 = font3.render(f'density(100°C): {density} kg/m^3 ~> vapor: 0.589 kg/m^3', True, (144,144,144))
            else:
                text6 = font3.render(f'density({temp}°C): {density} kg/m^3', True, (144,144,144))
            # verdampfunsenthalpie: 2257 kJ/kg enthalpy of vaporization/condensation
            # schmelzenthalpie: 334 kJ/kg enthalpy of fusion 
            capa = int(capa*100)/100
            if temp == 0:
                text7 = font3.render(f'heat capacity({temp}°C): {capa} J/kg*K ~> ice: 2090 J/kg*K', True, (144,144,144))
            elif 100 < temp < 103:
                text7 = font3.render(f'heat capacity(100°C): {capa} J/kg*K ~> vapor: 1870 J/kg*K', True, (144,144,144))    
            else:
                text7 = font3.render(f'heat capacity({temp}°C): {capa} J/kg*K', True, (144,144,144))
        if mol_mode == 2:
            #text4 = "CARBON/KOHLENSTOFF"
            value2 = value1

            text1 = font2.render(f'methane: CH4', True, (20,20,233))
            text4 = font3.render(f'electrons: 10', True, (0,233,0))
            text2 = font3.render(f'up quarks: 26', True, (233,0,0))
            text3 = font3.render(f'down quarks: 22', True, (144,44,244))
            text5 = font3.render(f'gluons: 128', True, (104,44,144))

            text8 = font3.render(f'enthalpy of crystallization: -58.6 kJ/kg', True, (44,44,44)) # 6 kJ/mol 420
            text9 = font3.render(f'enthalpy of vaporization: 510.5 kJ/kg', True, (44,44,44)) # 2501
            text10 = font3.render(f'molar mass: 16.043 g/mol', True, (44,44,44)) # 2501
            # 1000g = 1000g*6.02214076×10^23*mol/18 mol*g
            
        screen.blit(text1, (50, 50))
        screen.blit(text4, (50, 100))
        screen.blit(text2, (50, 150))
        screen.blit(text3, (50, 200))
        screen.blit(text5, (50, 250))
        if mol_mode == 1:
            screen.blit(text6, (50, height-70))
            screen.blit(text7, (50, height-120))
        screen.blit(text8, (50, height-177))
        screen.blit(text9, (50, height-227))
        screen.blit(text10, (50, height-277))

        if mol_mode == 1:
            if len(balls) < 6: # ELECTRONS O
                balls.append(Ball(width/2, height/2, 3))
            if len(balls2) < 8: # PROTONS at CORE
                balls2.append(Ball2(width/2, height/2, 12))
            if len(balls3) < 8: # NEUTRONS
                balls3.append(Ball3(width/2, height/2, 12))

            if len(balls5) < 2: # PROTONS H2
                balls5.append(Ball5(width*3/4, height*3/4, 12))
        else:
            if len(balls) < 2: # ELECTRONS O
                balls.append(Ball(width/2, height/2, 3))
            if len(balls2) < 6: # PROTONS at CORE
                balls2.append(Ball2(width/2, height/2, 12))
            if len(balls3) < 6: # NEUTRONS
                balls3.append(Ball3(width/2, height/2, 12))
            if len(balls5) < 4: # PROTONS H4
                balls5.append(Ball5(width*3/4, height*3/4, 12))
        
        for ball in balls:
            ball.update()
            ball.draw()

        for ball in balls2:
            ball.update()
            ball.draw()

        for ball in balls3:
            ball.update()
            ball.draw()

        for ball in balls5:
            ball.update()
            ball.draw()
        
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
