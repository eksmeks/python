#si_3d_search_plus

import pygame
import sys
import math
from sympy import *

#gyro = pygame.image.load("gyro.png")

si_units = {

        # si units:

        'm**2*kg/s': 'J*s action ',
        'kg*m**2/s': 'J*s action ',
        'kg*m/s**2': 'N (newton) force ',
        'm*kg/s**2': 'N (newton) force ',
        'kg*m**2/s**2': 'J (joule) energy or enthalpy',
        'm**2*kg/s**2': 'J (joule) energy or enthalpy',
        'kg*m**2/s**3': 'W (watts) power',
        'm**2*kg/s**3': 'W (watts) power',
        'kg/m**3': 'ρ (rho) density',
        'kg/m**2': 'surface mass density σ or ρ',
        'kg/m': 'linear mass density μ (my)',
        'kg/s': 'ṁ mass flow',
        'kg/s**3': '[heat flux density] (W/m^2)',
        'kg/m*s': 'η [dynamic viscosity]',
        'm**2': 'A [surface, area]',
        'm**3': 'V [volume]',
        'm**3/s':'V̇ [volume flow]',
        'm/s': 'v [velocity]',
        'm/s**2': 'a,g acceleration',
        'm**2/s': 'ν kinematic viscosity',
        'kg/(m*s**2)': 'Pa pressure (N/m**2)',
        'm**2/(s*K)': 'c specific heat capacity (J/kg*K)',
        'm**2/(K*s)': 'c specific heat capacity (J/kg*K)',
        'kg/(m*s**2)': 'Pa [pressure] (N/m**2)',
        'kg/(s**2*m)': 'Pa [pressure] (N/m**2)',
        'm**2/(s*K)': 'c specific heat capacity (J/(kg*K))',
        'm**2/(K*s)': 'c specific heat capacity (J/(kg*K))',
        'kg/s**3': 'heat flux density (W/m^2) ',
        'kg/(s**3*K)': 'heat transfer coefficient α (W/(m**2*K))',
        'kg/(K*s**3)': 'heat transfer coefficient α (W/(m**2*K))',
        'kg*m/(s**3*K)': 'λ (W/(m*K)) ',
        'kg*m/(K*s**3)': 'λ (W/(m*K)) ',
        'm*kg/(s**3*K)': 'λ (W/(m*K)) ',
        'm*kg/(K*s**3)': 'λ (W/(m*K)) ',
        'K*s**3/(kg*m)': 'R_A heat resistance per _λ (m*K/W)',
        's**3*K/(kg*m)': 'R_A heat resistance per _λ (m*K/W)',
        'K*s**3/(m*kg)': 'R_A heat resistance per _λ (m*K/W)',
        's**3*K/(m*kg)': 'R_A heat resistance per _λ (m*K/W)',
        's**3*K/kg': 'R_A heat resistance _α (m**2*K/W)',
        'K*s**3/kg': 'R_A heat resistance _α (m**2*K/W)',
        'kg/(m*s**2)': 'h enthalpy (J/m**3), Pa pressure (kg/m*s**2)',
        'm**2/s**2': 'h enthalpy per mass (J/kg)',
        'kg*m**2/(s**2*K)': 'S entropy (J/K)',
        'm**2*kg/(s**2*K)': 'S entropy (J/K)',
        'kg*m**2/(K*s**2)': 'S entropy (J/K)',
        'm**2*kg/(K*s**2)': 'S entropy (J/K)',
        'kg/mol': 'molarity',
        'm**3/kg': 'specific volume',
        'kg*m**2/(s**2*A)':'Wb weber',
        'kg*m**2/(A*s**2)':'Wb weber',
        'm**2*kg/(s**2*A)':'Wb weber',
        'm**2*kg/(A*s**2)':'Wb weber',
        'kg*m**2/(s**2*A**2)':'H henry',
        'kg*m**2/(A**2*s**2)':'H henry',
        'm**2*kg/(s**2*A**2)':'H henry',
        'm**2*kg/(A**2*s**2)':'H henry',


        # mixed: -------------------------------------------------------------

        'N/m**2': 'Pa pressure (kg/m*s^2)',  
        'J/(kg*K)': 'c specific heat capacity (m^2/s*K)',  
        'J/(K*kg)': 'c specific heat capacity (m^2/s*K)',
        'J/(m**3)': 'h enthalpy per volume (kg/m*s^2)',
        'J/kg': 'h enthalpy per mass (m^2/s^2)',    
        'W/m**2': 'heat flux density (kg/s^3) ',  
        'W/(m**2*K)': 'heat transfer coefficient α (kg/s^3*K) ', 
        'W/(K*m**2)': 'heat transfer coefficient α (kg/s^3*K) ', 
        'W/(m*K)': 'λ (kg*m/s^3*K) ',  
        'W/(K*m)': 'λ (kg*m/s^3*K) ',  
        'K/W': 'R_A heat resistance per area',  
        'K*m/W': 'R_A heat resistance per _λ (s^3*K/kg*m)',  
        'm*K/W': 'R_A heat resistance per _λ (s^3*K/kg*m)',  
        'K*m**2/W': 'R_A heat resistance _α (s^3*K/kg)',  
        'm**2*K/W': 'R_A heat resistance _α (s^3*K/kg)',  
        'W*s': 'Q heat amount (kg*m^2/s^2)',  
        'W': 'Q̇ heat transfer per unit time or V*A power (kg*m^2/s^3)',  
        'J/K': 'S entropy (kg*m^2/s^2*K)',
        'V/m': 'E electric field strength',
        'A/m': 'B magnetic field strength',
        'C/kg': 'Gy absorbed dose',
        'H/m': 'µ agnetic permeability',
        'S/m': 'σ electrical conductivity',
        'V*s': 'Φ electric flux, kg*m^2/s^2*A',
        'A*s':'C coulomb, electric charge, kg*m^2/s^2*V,',
        'A/m**2':'electric flux density, kg/s^3*V,',
        'A/V':'1/Ω, siemens, S',
        'V/A':'Ω, electric resistance',
        'J**2':'kg^2*m^4/s^4',
        '1/J**2':'s^4/kg^2*m^4',
        'J*s':'action, kg*m^2/s ',
        's*J':'action, kg*m^2/s ',

        '':'',

        #______________________________________________________________________
        # formula signs:

        'N': 'kg*m/s^2 [force]',
        'J': 'kg*m^2/s^2 [energy or enthalpy]',
        'h': 'enthalpy per something',
        'H': 'enthalpy,(kg*m^2/^2) henry, m**2*kg/(A**2*s**2)',
        'W': 'kg*m^2/s^3 [power]',
        'ρ': 'kg/m^3 [density]',
        'ṁ': 'kg/s [mass flow]',
        'A': 'm^2 or ampere, electric current, kg*m^2/s^3*V, W/V',      
        'V': 'm^3 or volt, electric potential, kg*m^2/s^3*A, W/A',
        'V̇': 'm^3/s [volume flow]',
        'v': 'm/s [speed]',
        'a': 'm/s^2 [acceleration]',
        'ν': 'm^2/s [kinematic viscosity]',
        'η': 'kg/m*s [dynamic viscosity] (Ns/m^2)',
        'Pa': 'N/m^2 [pressure] (kg/m*s^2)',
        'c': 'J/kg*K [specific heat capacity] (m^2/s^2*K)',
        'λ': 'W/m*K (kg*m/s^3*K)',
        'α': 'W/m^2*K [heat transfer coefficient] (kg/s^3*K)',
        'Q': 'W*s heat amount, [energy] (kg*m^2/s^2)',
        'Q̇': 'W heat transfer per unit time [power] (kg*m^2/s^3)',
        'R_A': 'K/W heat resistance per area (K*s^3/kg*m^2)',
        'R_lambda': 'K*m/W heat resistance R_λ (K*s^3/kg*m)',
        'R_lambda': 'm*K/W heat resistance R_λ (K*s^3/kg*m)',
        'R_alpha': 'K*m**2/W heat resistance R_α (K*s^3/kg)',
        'R_alpha': 'm**2*K/W heat resistance R_α (K*s^3/kg)',
        'S': 'J/K entropy (kg*m^2/s^2*K), siemens, (V/A)[1/]',
        's': 'J/mol*K specific entropy (kg*m^2/s^2*K*mol)',
        'I': 'irradiance or heat flux density also kg/s^3 ',
        'E': 'V/m Volt per meter, the electrical field force',
        'B': 'T (tesla) magnetic field strength',
        'Gy': 'C/kg absorbed dose',
        'Wb': 'Φ magnetic flux',
        'µ': 'H/m magnetic permeability ',
        'σ': 'S/m electrical conductivity',
        'Φ': 'V*s electric flux',

    }

def search():
    global text_res
    # Define symbolic variables
    x, y, z = symbols('x y z')

    # Get the input fraction
    fraction = texti

    if fraction == "" or fraction == " " or fraction == "  " or fraction == "   " or fraction == "    " or fraction == "      ":
        text_res = "-"
        fraction = "1"

    if fraction != ("V." and "m." and "Q."):

        # Parse the fraction expression
        expr = sympify(fraction)

        # Simplify the fraction
        simplified_expr = str(simplify(expr))

        # Print the simplified fraction
        text_res = ""

        inp = simplified_expr

    else:
        inp=fraction

    if inp == "V.":
        inp = "V̇"

    if inp == "m.":
        inp = "ṁ"

    if inp == "Q.":
        inp = "Q̇"
        
    if inp == "rho":
        inp = "ρ"

    if inp == "ny":
        inp = "ν"
        
    if inp == "my":
        inp = "µ"

    if inp == "eta":
        inp = "η"

    if inp == "lambda_":
        inp = "λ"

    if inp == "alpha":
        inp = "α"

    if inp == "ohm":
        inp = "Ω"
    
    if inp == "phi":
        inp = "Φ"
    
    formula_sign = inp

    if formula_sign in si_units:
        si_unit = si_units[formula_sign]
        text_res += str(f"unit/sign for '{formula_sign}' \n is '{si_unit}'.")
    else:
        text_res += str("expression not found in the dictionary.")

pygame.init()
raise1 = 1.7 #1.7
raise2 = 1.2 #1.2
raiser = 2.6 #2.6
WIDTH, HEIGHT = int(820*raise1), int(630*raise2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("si unit grid")
clock = pygame.time.Clock()

# unit search
font2 = pygame.font.Font(None, int(17*(max(1,raise1-0.2))))
font1 = pygame.font.Font(None, 20)

input_box = pygame.Rect(int(500*raise1), 47, 0, 20)
color_inactive = ((0,100,0))
color_active = pygame.Color('dodgerblue')
color = color_inactive

# Variables for managing the input state
active = False
texti = ''
done = False

# si units
font = pygame.font.Font(None, 27)
a = 0
kg = 1
m = 1
s = 1
K = 0
A = 0
mol = 0

#3D
# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Grid settings
GRID_MIN, GRID_MAX = -3, 3   # Grid from -4 to 4 in each direction
SPACING = int(51*raise1) #73  # Distance between each node in pixels (smaller for isometric)
player_pos = [0, 0, 0]  # Start player at the origin of the grid

# Center of the screen
CENTER_X, CENTER_Y = WIDTH // 2-67, HEIGHT // 2

deg1 = 33#38#14#12 #24 40
deg2 = 30#50#46 #30 30
degz = 0.3#2#0.2 #0.2 0.3
degy = 1 # y+

def isometric_projection(x, y, z):
    # Rotate x and y by 30 degrees to avoid overlap
    #x_rot = x * math.cos(math.radians(60-deg2)) - y * math.cos(math.radians(deg2))
    #y_rot = x * math.sin(math.radians(68-deg1)) + y*(math.e*y**degy) * math.sin(math.radians(deg1)) - z * degz
    
    x_rot = x * math.cos(math.radians(30-deg2)) - y * math.cos(math.radians(deg2))
    y_rot = x * math.sin(math.radians(deg1)) + y*degy * math.sin(math.radians(deg1)) - z * degz
    
    # Scale by SPACING and center on screen
    x_iso = x_rot * SPACING + CENTER_X
    y_iso = y_rot * SPACING + CENTER_Y
    return int(x_iso), int(y_iso)

  #(-s,-m,kg)
special_points = {
    (0,1,1), 
    (-1,0,0), 
    (0,-1,0),
    (0,0,1),
    (2,0,1),
    (0,-2,0),
    (0,-3,0),
    (1,-3,0),
    (1,-1,1),
    (1,-1,0),
    (1,-2,0),
    (2,-1,0),
    (1,1,1),
    (1,-2,1),
    (1,0,1),
    (3,0,1),
    (3,-2,1),
    (0,3,1),
    (2,-2,0),
    (2,-2,1),
    (2,-1,1),
    (2,1,1),
    (2,-3,-1),
    (1,0,0),
    #(-3,0,-1),
    #(-3,1,-1),
    #(-3,2,-1),
    (0,-3,-1),
    (0,-2,1),
    (2,0,0)
}
   #(-s,-m,kg)
special_points_k = {
    (3,-1,1),
    (3,0,1),
    (-3,2,-1),
    (-3,1,-1),
    (-3,0,-1),
    (2,-2,0),
    (2,-2,1),
    (0,0,0)
}
  #(-s,-m,kg)
special_points_A = {
    (2,0,1),
    (-1,2,0),
    (-1,1,0),
    (2,-2,1),
    (0,-2,0),
    (-1,0,0),
    (-3,2,-1),
    (3,-3,1),
    (3,-2,1),
    (3,-1,1),
    (1,0,1),
    (-3,0,-1),
    (-3,3,-1),
    (0,2,0),
    (0,1,0),
    (2,-1,1),
    (3,0,1),
    (-1,0,-1),
    (-4,3,-1),
    (-4,2,-1)
}
  #(-s,-m,kg)
special_points_mol = {
    (-1,0,0),
    (0,3,0),
    (0,-3,0),
    (0,0,1),
    (2,-2,1),
    (-3,0,-1),
    (0,0,0)
}

default_color = WHITE
default_radius = max(3,3*raiser/2)
#special_color = (kg*7,m*7,s*7)
special_color = (70,200,20)
special_color_A = (140,40,117)
special_color_k = (10,10,100)
special_color_mol = (244,244,244)
special_radius = int(6*raiser)
special_radius_A = int(5*raiser)
special_radius_mol = int(7*raiser)
special_radius_k = int(3*raiser)
special_radius_k2 = int(4*raiser)

def draw_grid():
    for x in range(GRID_MIN-1, GRID_MAX + 1):
        for y in range(GRID_MIN, GRID_MAX + 1):
            for z in range(-1, 1 + 1):
                # Calculate 3D position and project to 2D
                pos_3d = (x, y, z)
                pos_2d = isometric_projection(*pos_3d)

                if pos_3d in special_points_mol:
                    node_color, node_radius = special_color_mol, special_radius_mol
                    pygame.draw.circle(screen, node_color, pos_2d, node_radius)
                if pos_3d in special_points:
                    node_color, node_radius = special_color, special_radius
                else:
                    node_color, node_radius = default_color, default_radius
                pygame.draw.circle(screen, node_color, pos_2d, node_radius)
                if pos_3d in special_points_A:
                    node_color, node_radius = special_color_A, special_radius_A
                    pygame.draw.circle(screen, node_color, pos_2d, node_radius)
                if pos_3d in special_points_k:
                    node_color, node_radius = special_color, special_radius_k2
                    pygame.draw.circle(screen, node_color, pos_2d, node_radius)
                    node_color, node_radius = special_color_k, special_radius_k
                # Draw the node with its color and radius
                    pygame.draw.circle(screen, node_color, pos_2d, node_radius)

                # Determine color for axis lines
                axis_color = RED

                # Draw lines to neighboring nodes for grid structure
                if x + 1 <= GRID_MAX:  # Line along x-axis
                    neighbor_2d = isometric_projection(x + 1, y, z)
                    line_color = axis_color if y == 0 and z == 0 else BLUE
                    pygame.draw.line(screen, line_color, pos_2d, neighbor_2d)

                if y + 1 <= GRID_MAX:  # Line along y-axis
                    neighbor_2d = isometric_projection(x, y + 1, z)
                    line_color = axis_color if x == 0 and z == 0 else BLUE
                    pygame.draw.line(screen, line_color, pos_2d, neighbor_2d)

                if z + 1 <= 1:  # Line along z-axis
                    neighbor_2d = isometric_projection(x, y, z + 1)
                    line_color = axis_color if x == 0 and y == 0 else BLUE
                    pygame.draw.line(screen, line_color, pos_2d, neighbor_2d)


# Draw the player at its position on the grid
def draw_player():
    player_2d = isometric_projection(*player_pos)
    pygame.draw.circle(screen, RED, player_2d, int(min(9,6*raiser**2-1)))
    pygame.draw.circle(screen, (0,0,0), player_2d, int(min(7,6*raiser**2-2)))
    pygame.draw.circle(screen, RED, player_2d, int(min(6,6*raiser-1)))

text_res = " "

# BUTTONS

buttontext = "kg"+"\n"+"\n"+"m"+"\n"+"\n"+"s"+"\n"+"\n"+"K"+"\n"+"\n"+"A"+"\n"+"\n"+"mol"
button_color = (77,77,77)

spacer = int(8*raise1)
area = int(17*raise1)
x1 = int(753*raise1)
x2 = int(773*raise1)
y1 = int(117*raise2)

button_rect1 = pygame.Rect(x1, y1-spacer, area, area)  
button_rect2 = pygame.Rect(x1, y1+spacer*2,area, area)
button_rect3 = pygame.Rect(x1, y1+spacer*5,area, area)
button_rect4 = pygame.Rect(x1, y1+spacer*8,area, area)
button_rect5 = pygame.Rect(x1, y1+spacer*11,area, area)
button_rect6 = pygame.Rect(x1, y1+spacer*14,area, area)
button_rect7 = pygame.Rect(x2, y1-spacer,area, area)
button_rect8 = pygame.Rect(x2, y1+spacer*2,area, area)
button_rect9 = pygame.Rect(x2, y1+spacer*5,area, area)
button_rect10 = pygame.Rect(x2, y1+spacer*8,area, area)
button_rect11 = pygame.Rect(x2, y1+spacer*11,area, area)
button_rect12 = pygame.Rect(x2, y1+spacer*14,area, area)

button_rectx1 = pygame.Rect(x1-7, y1-spacer-7,area*3, area*8.7)
button_rectx2 = pygame.Rect(x1-5, y1-spacer-5,area*2.7, area*8.3)
button_rectx3 = pygame.Rect(x1-7, y1+spacer*8-7,area*3, area*4.5)
button_rectx4 = pygame.Rect(x1-5, y1+spacer*8-5,area*2.7, area*4.3)

def draw_buttons():
    pygame.draw.rect(screen, (0,144,0), button_rectx1)
    pygame.draw.rect(screen, (0,0,0), button_rectx2)
    pygame.draw.rect(screen, (144,144,144), button_rectx3)
    pygame.draw.rect(screen, (0,0,0), button_rectx4)

    pygame.draw.rect(screen, button_color, button_rect1)
    pygame.draw.rect(screen, button_color, button_rect2)
    pygame.draw.rect(screen, button_color, button_rect3)
    pygame.draw.rect(screen, button_color, button_rect4)
    pygame.draw.rect(screen, button_color, button_rect5)
    pygame.draw.rect(screen, button_color, button_rect6)
    pygame.draw.rect(screen, button_color, button_rect7)
    pygame.draw.rect(screen, button_color, button_rect8)
    pygame.draw.rect(screen, button_color, button_rect9)
    pygame.draw.rect(screen, button_color, button_rect10)
    pygame.draw.rect(screen, button_color, button_rect11)
    pygame.draw.rect(screen, button_color, button_rect12)
    

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

            if button_rect1.collidepoint(event.pos):
                player_pos[2] = max(-1, player_pos[2] - 1) # kg -
                a = " "
            if button_rect2.collidepoint(event.pos):
                player_pos[1] = min(GRID_MAX, player_pos[1] + 1) # m - 
                a = " " 
            if button_rect3.collidepoint(event.pos):
                player_pos[0] = min(GRID_MAX, player_pos[0] + 1) # right s-
                a = " "
            if button_rect4.collidepoint(event.pos):
                K -= 1
                A = 0
                a = " "
            if button_rect5.collidepoint(event.pos):
                A -= 1
                K = 0
                a = " "
            if button_rect6.collidepoint(event.pos):
                mol -= 1
                a = " "
            if button_rect7.collidepoint(event.pos):
                player_pos[2] = min(1, player_pos[2] + 1) # kg +
                a = " "
            if button_rect8.collidepoint(event.pos):
                player_pos[1] = max(GRID_MIN, player_pos[1] - 1) # up m+
                a = " "
            if button_rect9.collidepoint(event.pos):
                player_pos[0] = max(GRID_MIN-1, player_pos[0] - 1) # left s+
                a = " "
            if button_rect10.collidepoint(event.pos):
                K += 1
                A = 0
                a = " "
            if button_rect11.collidepoint(event.pos):
                A += 1
                K = 0
                a = " "
            if button_rect12.collidepoint(event.pos):
                mol += 1
                a = " "
            if K > 1:
                K = 1
                a = " "
            if K < -1:
                K = -1
                a = " "
            if A > 2:
                A = 2
                a = " "
            if A < -2:
                A = -2
                a = " "
            if mol < -1:
                mol = -1
                a = " "
            
        # Handle keyboard events when the box is active
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    #print(texti)  # Enter key submits the text (prints it here)
                    fraction = texti
                    search()
                    texti = ''  # Clear the input after submitting
                elif event.key == pygame.K_BACKSPACE:
                    texti = texti[:-1]  # Remove last character on Backspace
                else:
                    texti += event.unicode  # Add the typed character to the text
    #Si
    screen.fill((0,0,0))
    txt_color = 1
    if kg == 0 and m == 0 and s == -2 and K == 0 and A == 0 and mol == 0:
        a = "angular acceleration"
    if kg == 0 and m == -1 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "per length, line relation, dioptrie dpt"
        a += "\n"
        a += " -> A/m"
    if kg == 0 and m == -2 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "per area, surface relation"
        a += "\n"
        a += " -> A/m^2"
    if kg == 0 and m == -3 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "per volume, cubic relation"
        a += "\n"
        a += "number of molecules per normvolume of ideal gas: 2.686780111*10^25 *1/m^3"
    if kg == 0 and m == 0 and s == 0 and K == 0 and A == 0 and mol == -1:
        a = "particles per mol, avogadro constant = 6.02214076×10^23/mol"
    if kg == 0 and m == -3 and s == 0 and K == 0 and A == 0 and mol == 1:
        a = "substance concentration c"
    if kg == 0 and m == 0 and s == 0 and K == 0 and A == 0 and mol == 1:
        a = "amount of substance, mol"
    if kg == 1 and m == 0 and s == 0 and K == 0 and A == 0 and mol == -1:
        a = "molarity, m/M" 
    if kg == 1 and m == 0 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "kilogram, weight measure"
    if kg == 1 and m == -1 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "μ, linear mass density"
    if kg == 0 and m == 1 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "meter, length measure"
    if kg == 0 and m == 0 and s == 1 and K == 0 and A == 0 and mol == 0:
        a = "second, time measure"
    if kg == 0 and m == 0 and s == 0 and K == 1 and A == 0 and mol == 0:
        a = "Kelvin, temperature measure"
    if kg == 0 and m == 2 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "area, A"
    if kg == 0 and m == 3 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "volume, V"
    if kg == 0 and m == 3 and s == -1 and K == 0 and A == 0 and mol == 0:
        a = "volume flow, V_dot"
    if kg == 0 and m == 1 and s == -2 and K == 0 and A == 0 and mol == 0:
        a = "acceleration, a"
    if kg == 0 and m == 1 and s == -1 and K == 0 and A == 0 and mol == 0:
        a = "velocity, v, speed of light c = 299792458 m/s"
    if kg == 0 and m == 2 and s == -1 and K == 0 and A == 0 and mol == 0:
        a = "viscosity (kin), ny"
    if kg == 1 and m == 1 and s == -1  and K == 0 and A == 0 and mol == 0:
        a = "impulse, N*s"
    if kg == 1 and m == 2 and s == -1  and K == 0 and A == 0 and mol == 0:
        a = "angular momentum, N*m*s, action, (m*v*s), J/Hz"
        a += "\n"
        a += "planck h = 6.62607015e-34 J·s"
    if kg == 1 and m == -1 and s == -1 and K == 0 and A == 0 and mol == 0:
        a = "viscosity (dyn), η, Pa*s, N*s/m^2, "
    if kg == 1 and m == 0 and s == -1 and K == 0 and A == 0 and mol == 0:
        a = "mass flow, m_dot"
    if kg == 1 and m == 1 and s == -3 and K == -1 and A == 0 and mol == 0:
        a = "thermal conductivity coefficient, lambda λ, W/m*K"
    if kg == 1 and m == 0 and s == -3 and K == -1 and A == 0 and mol == 0:
        a = "heat transfer coefficient, alpha α, W/m^2*K"
        a += "\n"
        a += "stefan-boltzmann: 5.67*10^-8 W/m^2*K^4"
    if kg == 1 and m == 0 and s == -3 and K == 0 and A == 0 and mol == 0:
        a = "heat flux density, q_dot, W/m^2, (poynting vector)"
        a += "\n"
        a += "1 met = 58 W/m^2 (heat emission of human body surface)"
    if kg == 1 and m == 2 and s == -3 and K == 0 and A == 0 and mol == 0:
        a = "power, W, Q_dot, m*c_p*dT, A*V"
        a += "\n"
        a += "1 W = 683 lumen [bei 555nm,grünes Licht](candela = lumen/4*pi)"
    if kg == 1 and m == -3 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "density, ρ, mass per volume"
    if kg == -1 and m == 3 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "spec volume, v"
    if kg == -1 and m == -2 and s == 3 and K == 1 and A == 0 and mol == 0:
        a = "heat resistance, K/W"
    if kg == -1 and m == -2 and s == 3 and K == 0 and A == 0 and mol == 0:
        a = "-> s^3*K/kg*m^2"
        a += "\n"
        a += "-> s^3*A^2/kg*m^2"
        txt_color = 2
    if kg == -1 and m == -1 and s == 3 and K == 1 and A == 0 and mol == 0:
        a = "thermal conductivity resistance (durchgang), m*K/W, 1/λ, R_λ"
    if kg == -1 and m == -1 and s == 3 and K == 0 and A == 0 and mol == 0:
        a = "-> s^3*K/kg*m"
        txt_color = 2
    if kg == -1 and m == 0 and s == 3 and K == 1 and A == 0 and mol == 0:
        a = "heat transfer resistance (übergang), m^2*K/W, 1/α, R_α"
        a += "\n"
        a += "1 clo = 0.155 m^2*K/W (human clothing)"
    if kg == -1 and m == 0 and s == 3 and K == 0 and A == 0 and mol == 0:
        a = "-> s^3*K/kg"
        txt_color = 2
    if kg == 0 and m == 2 and s == -2 and K == -1 and A == 0 and mol == 0:
        a = "spec heat capacity, c_p, specific entropy s, R (gasconstant), J/kg*K"
    if kg == 1 and m == 2 and s == -2 and K == -1 and A == 0 and mol == -1:
        a = "molar heat capacity, J/mol*K" 
    if kg == 1 and m == 2 and s == -2 and K == -1 and A == 0 and mol == 0:
        a = "entropy, S, J/K, boltzmann: 1.380649*10^-23 J/K"
    if kg == 0 and m == 2 and s == -2 and K == 0 and A == 0 and mol == 0:
        a = "spec enthalpy, h, Hn, J/kg"
        a += "\n"
        a += "sievert Sv, energy dose Gy"
    if kg == 1 and m == 2 and s == -2 and K == 0 and A == 0 and mol == 0:
        a = "energy, work, heat, enthalpy, torque, J"
        a += "\n"
        a += "momentum, N*m, W*s, Pa*m^3, 6.242*10^18 eV, SKE, cal/4.19"
    if kg == 1 and m == 1 and s == -2 and K == 0 and A == 0 and mol == 0:
        a = "force, N"
    if kg == 1 and m == -1 and s == -2 and K == 0 and A == 0 and mol == 0:
        a = "pressure, N/m^2, Pa, bar"
        a += "\n"
        a += "spec enthalpy, h, Hn, J/m^3"
    if kg == 1 and m == 0 and s == -2 and K == 0 and A == 0 and mol == 0:
        a = "radiation energy flux, J/m^2"
        a += "\n"
        a += "surface energy, water(20°C) = 0.072 J/m^2"
    if kg == -1 and m == 3 and s == -2 and K == 0 and A == 0 and mol == 0:
        a = "gravitational force, G, N*m^2/kg^2"
    if kg == 0 and m == 0 and s == -1 and K == 0 and A == 0 and mol == 0:
        a = "frequency, Hz"
    if kg == 1 and m == 2 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "moment of inertia"
    if kg == 0 and m == 0 and s == 0 and K == 0 and A == 1 and mol == 0:
        a = "ampere, electrical current, kg*m^2/s^3*V"
    if kg == 0 and m == 2 and s == 0 and K == 0 and A == 1 and mol == 0:
        a = "bohr magnetron, magnetic moment of an electron"
        a += "\n"
        a += "9.2740100657*10^-24 J/T"
    if kg == 0 and m == 0 and s == 1 and K == 0 and A == 1 and mol == -1:
        a = "faraday constant F = e*NA = 96485,33212 C/mol" 
    if kg == -1 and m == -2 and s == 3 and K == 0 and A == 2 and mol == 0:
        a = "electrical conductance, siemens, S = A/V = 1/Ω"
        a += "\n"
        a += "conductance quant G0 = 7.748091729e-5 S"
    if kg == -1 and m == -3 and s == 3 and K == 0 and A == 0 and mol == 0:
        a = "-> s^3*A*2/kg*m^3"
        txt_color = 2
    if kg == -1 and m == -3 and s == 3 and K == 0 and A == 2 and mol == 0:
        a = "electrical conductivity, S/m, F/m*s, 1/Ω*m"
        a += "\n"
    #if kg == -1 and m == -4 and s == 3 and K == 0 and A == 2 and mol == 0:
        a += "specific conductance (of a solution), k = S/m^2, A^2/W*m, 1/Ω*m^2"
    if kg == 1 and m == 2 and s == -3 and K == 0 and A == -2 and mol == 0:
        a = "electrical resistance, ohm Ω, W/A^2"
        a += "\n"
        a += "wave resistance of vacuum Zw0 = μ0*c = 376.730313412 Ω"
    if kg == 1 and m == 3 and s == -3 and K == 0 and A == -2 and mol == 0:
        a = "resistivity, specific resistance, Ω*m, W*m/A^2"
    if kg == 1 and m == 3 and s == -3 and K == 0 and A == 0 and mol == 0:
        a = "-> kg*m^3/s^3*A^2"
        txt_color = 2
    if kg == 1 and m == 2 and s == -3 and K == 0 and A == -1 and mol == 0:
        a = "volt, electricity potencial, W/A"
    if kg == 1 and m == 1 and s == -3 and K == 0 and A == -1 and mol == 0:
        a = "electric field strength E, V/m, W/m*A, N/C" 
    if kg == 1 and m == 1 and s == -3 and K == 0 and A == 0 and mol == 0:
        a = "-> kg*m/s^3*A" 
        a += "\n"
        a += "-> kg*m/s^3*K" 
        txt_color = 2
    if kg == 0 and m == 0 and s == 1 and K == 0 and A == 1 and mol == 0:
        a = "coulomb, electrical charge, A*s, kg*m^2/s^2*V"
        a += "\n"
        a += "elementary charge e = 1.602176634×10^−19 C"
    if kg == 1 and m == 0 and s == -1 and K == 0 and A == -1 and mol == 0:
        a = "electrochemical equivalent, kg/C"
    if kg == 1 and m == 2 and s == -2 and K == 0 and A == -1 and mol == 0:
        a = "magnetic flux, weber Wb, V*s, W*s/A"
    if kg == 1 and m == 0 and s == -2 and K == 0 and A == -1 and mol == 0:
        a = "magnetic flux density, tesla, V*s/m^2, Wb/m^2, N/m*A "
    if kg == 1 and m == 0 and s == -3 and K == 0 and A == -1 and mol == 0:
        a = "gyromagnetic relation of the electron, m^2/Wb*s, 1/T*s"
        a += "\n"
        a += "Gamma_e = 1.76085962784*10^11 1/T*s"
        #screen.blit(gyro,(27,HEIGHT-(177*raise2)))
    if kg == 1 and m == 2 and s == -2 and K == 0 and A == -2 and mol == 0:
        a = "inductance, henry H, Wb/A, W*s/A^2"
    if kg == 1 and m == 1 and s == -2 and K == 0 and A == -2 and mol == 0:
        a = "magnetic permeability H/m, Wb/A*m, W*s/A^2*m, V*s/A*m"
        a += "\n"
        a += "magnetic field constant μ0 ​= 4π×10^−7 H/m = 1.25663706×10^−6 kg*m/s^2*A^2"
    if kg == -1 and m == 0 and s == 3 and K == 0 and A == 0 and mol == 0:
        a = "-> s^3*A^2/mol*kg" 
        a += "\n"
        a += "-> s^3*K/kg"
        txt_color = 2
    if kg == -1 and m == 0 and s == 3 and K == 0 and A == 2 and mol == -1:
        a = "molar conductivity, Λ = S*m^2/mol" 
    if kg == 0 and m == 3 and s == 0 and K == 0 and A == 0 and mol == -1:
        a = "molar volume, 0.022413969545 m^3/mol for gases at STP"
    if kg == 0 and m == -2 and s == 0 and K == 0 and A == 1 and mol == 0:
        a = "electric current density S"    
    if kg == 0 and m == -2 and s == 1 and K == 0 and A == 1 and mol == 0:
        a = "electric flux density D, C/m^2"    
    if kg == 0 and m == -2 and s == 1 and K == 0 and A == 0 and mol == 0:
        a = "-> A*s/m^2"  
        txt_color = 2 
    if kg == 0 and m == -1 and s == 1 and K == 0 and A == 1 and mol == 0:
        a = "linear electric charge density λ, C/m"    
    if kg == 0 and m == -1 and s == 1 and K == 0 and A == 0 and mol == 0:
        a = "-> A*s/m"  
        txt_color = 2 
    if kg == 0 and m == -1 and s == 0 and K == 0 and A == 1 and mol == 0:
        a = "magnetic field strength H"  
    if kg == -1 and m == -2 and s == 4 and K == 0 and A == 2 and mol == 0:
        a = "electric capacity, Farad, A*s/V, C/V, s/Ω"    
    if kg == -1 and m == -2 and s == 4 and K == 0 and A == 0 and mol == 0:
        a = "-> s^4*A^2/kg*m^2"
        txt_color = 2
    if kg == -1 and m == -3 and s == 4 and K == 0 and A == 2 and mol == 0:
        a = "electric permittivity, εo = 8.854*10^-12 F/m"  
    if kg == -1 and m == -3 and s == 4 and K == 0 and A == 0 and mol == 0:
        a = "-> s^4*A^2/kg*m^3"
        txt_color = 2  
    if kg == -1 and m == 0 and s == 1 and K == 0 and A == 1 and mol == 0:
        a = "specific charge of the electron = -1.75882000838*10^11 C/kg " 
        a += "\n"
        a += "-e/m_e charge per mass"
    if kg == -1 and m == 0 and s == 1 and K == 0 and A == 0 and mol == 0:
        a = "-> A*s/kg"
        txt_color = 2 

    
    # Seebeck-Koeffizient: V/K, kg⋅m2​/s3⋅A⋅K

    """
    if kg == 0 and m == 0 and s == 0 and K == 0 and A == 0 and mol == 0:
        a = "" 
        a += "\n"
        a += ""
    """
    # every si unit is described through E = h*f = m*v^2 
    # m = h*f/c^2              
    # h = 6.62607015×10^−34 J⋅s  [kg*m^2/s] planck
    # c = 3*10^8 [m/s]
    # f = 1.3582855*10^50 [1/s] 
    # compton frequenz: 1.3582855*10^50 1/s
    #                   9.19*10^9 1/s CÄSIUM 
    # 1kg = 6.62607015×10^−34*1.3582855*10^50/9*10^16
    if txt_color == 1:
        text = font.render(f" {a}", True, (0,244,0))
    if txt_color == 2:
        text = font2.render(f" {a}", True, (40,20,170))
    screen.blit(text, (int(70*raise1), int(570*raise2)))

    text = font1.render(text_res, True, (0,244,0))
    screen.blit(text, (int(500*raise1), int(87*raise2)))

    formula_up = ""
    formula_down = ""
    if kg>0:
        if abs(kg) == 1:
            formula_up += str("kg ")
        else:
            formula_up += str("kg^"+str(abs(kg))+" ")
    if kg<0:
        if abs(kg) == 1:
            formula_down += str("kg ")
        else:
            formula_down += str("kg^"+str(abs(kg))+" ")
    if m>0:
        if abs(m) == 1:
            formula_up += str("m ")
        else:
            formula_up += str("m^"+str(abs(m))+" ")
    if m<0:
        if abs(m) == 1:
            formula_down += str("m ")
        else:
            formula_down += str("m^"+str(abs(m))+" ")
    if s>0:
        if abs(s) == 1:
            formula_up += str("s ")
        else:
            formula_up += str("s^"+str(abs(s))+" ")
    if s<0:
        if abs(s) == 1:
            formula_down += str("s ")
        else:
            formula_down += str("s^"+str(abs(s))+" ")
    if K>0:
        if abs(K) == 1:
            formula_up += str("K ")
        else:
            formula_up += str("K^"+str(abs(K))+" ")
    if K<0:
        if abs(K) == 1:
            formula_down += str("K ")
        else:
            formula_down += str("K^"+str(abs(K))+" ")
    if A>0:
        if abs(A) == 1:
            formula_up += str("A ")
        else:
            formula_up += str("A^"+str(abs(A))+" ")
    if A<0:
        if abs(A) == 1:
            formula_down += str("A ")
        else:
            formula_down += str("A^"+str(abs(A))+" ")
    if mol>0:
        if abs(mol) == 1:
            formula_up += str("mol ")
        else:
            formula_up += str("mol^"+str(abs(mol))+" ")
    if mol<0:
        if abs(mol) == 1:
            formula_down += str("mol ")
        else:
            formula_down += str("mol^"+str(abs(mol))+" ")
    if kg <= 0 and m <= 0 and s <= 0 and K <= 0 and A <= 0 and mol <= 0:
        if kg != 0 or m != 0 or s != 0 or K != 0 or A != 0 or mol != 0:
            formula_up = "1"
    # DRAW FORMULA
    text = font.render(formula_up, True, (0,244,0))
    screen.blit(text, (int(70*raise1), int(60*raise2)))
    pygame.draw.line(screen, (0,244,0),(int(70*raise1),int(87*raise2)),(int((70+10*(len(formula_up)/2+len(formula_down)/2))*raise1),int(87*raise2)))
    text = font.render(formula_down, True, (0,244,0))
    screen.blit(text, (int(70*raise1), int(100*raise2)))
    # K LINES RIGHT CORNER
    k1 = int(530*raise2)
    k2 = int(630*raise1)+70
    pygame.draw.line(screen, (0,244,0),(k2,k1),(k2,k1-66))
    if K == -1:
        pygame.draw.circle(screen, (40,40,170), (k2,k1), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (k2,k1), 5)
    if K == 0:
        pygame.draw.circle(screen, (40,40,170), (k2,k1-33), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (k2,k1-33), 5)
    if K == 1:
        pygame.draw.circle(screen, (40,40,170), (k2,k1-66), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (k2,k1-66), 5)
    # mol LINES RIGHT CORNER
    mol1 = int(530*raise2)
    mol2 = int(665*raise1)+70
    pygame.draw.line(screen, (40,244,70),(mol2,mol1),(mol2,mol1-66))
    if mol == -1:
        pygame.draw.circle(screen, (40,40,170), (mol2,mol1), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (mol2,mol1), 5)
    if mol == 0:
        pygame.draw.circle(screen, (40,40,170), (mol2,mol1-33), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (mol2,mol1-33), 5)
    if mol == 1:
        pygame.draw.circle(screen, (40,40,170), (mol2,mol1-66), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (mol2,mol1-66), 5)
    # A LINES RIGHT CORNER
    a1 = int(530*raise2)
    a2 = int(700*raise1)+70
    pygame.draw.line(screen, (37,204,40),(a2,a1+33),(a2,a1-99))
    if A == -2:
        pygame.draw.circle(screen, (40,40,170), (a2,a1+33), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (a2,a1+33), 5)
    if A == -1:
        pygame.draw.circle(screen, (40,40,170), (a2,a1), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (a2,a1), 5)
    if A == 0:
        pygame.draw.circle(screen, (40,40,170), (a2,a1-33), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (a2,a1-33), 5)
    if A == 1:
        pygame.draw.circle(screen, (40,40,170), (a2,a1-66), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (a2,a1-66), 5)
    if A == 2:
        pygame.draw.circle(screen, (40,40,170), (a2,a1-99), 5)
    else:
        pygame.draw.circle(screen, (244,244,244), (a2,a1-99), 5)

    #3D
    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] = max(GRID_MIN-1, player_pos[0] - 1)
        a = " "
    if keys[pygame.K_RIGHT]:
        player_pos[0] = min(GRID_MAX, player_pos[0] + 1)
        a = " "
    if keys[pygame.K_UP]:
        player_pos[1] = max(GRID_MIN, player_pos[1] - 1)
        a = " "
    if keys[pygame.K_DOWN]:
        player_pos[1] = min(GRID_MAX, player_pos[1] + 1)
        a = " "
    if keys[pygame.K_PERIOD]:
        player_pos[2] = max(-1, player_pos[2] - 1)
        a = " "
    if keys[pygame.K_COMMA]:
        player_pos[2] = min(1, player_pos[2] + 1)
        a = " "
    if keys[pygame.K_h]:
        A += 1
        K = 0
        a = " "
    if keys[pygame.K_j]:
        A -= 1
        K = 0
        a = " "
    if A > 2:
        A = 2
        a = " "
    if A < -2:
        A = -2
        a = " "
    if keys[pygame.K_n]:
        mol += 1
        a = " "
    if keys[pygame.K_m]:
        mol -= 1
        a = " "
    if mol > 1:
        mol = 1
        a = " "
    if mol < -1:
        mol = -1
        a = " "
    if keys[pygame.K_k]:
        K += 1
        A = 0
        a = " "
    if keys[pygame.K_l]:
        K -= 1
        A = 0
        a = " "
    if K > 1:
        K = 1
        a = " "
    if K < -1:
        K = -1
        a = " "
    if keys[pygame.K_z]:
        degy += 0.3
    if keys[pygame.K_u]:
        degy -= 0.3
        if degy < 0:
            degy = 0
    if keys[pygame.K_t]:
        raiser += 0.4
        default_radius = max(3,3*raiser/2)
        special_radius = int(6*raiser)
        special_radius_A = int(5*raiser)
        special_radius_mol = int(7*raiser)
        special_radius_k = int(3*raiser)
    if keys[pygame.K_g]:
        raiser -= 0.4
        default_radius = max(3,3*raiser/2)
        special_radius = int(6*raiser)
        special_radius_A = int(5*raiser)
        special_radius_mol = int(7*raiser)
        special_radius_k = int(3*raiser)
    if keys[pygame.K_r]:
        SPACING += 2
    if keys[pygame.K_f]:
        SPACING -= 2    
    if keys[pygame.K_w]:
        deg1 += 1
    if keys[pygame.K_s]:
        deg1 -= 1
    if keys[pygame.K_q]:
        deg2 += 2
    if keys[pygame.K_a]:
        deg2 -= 2
    if keys[pygame.K_e]:
        degz += 0.1
    if keys[pygame.K_d]:
        degz -= 0.1
        print(deg1,deg2,degz)
    if keys[pygame.K_i]:
        print("[up]     = m + "+"\n"+"[down]   = m -"+"\n"+"[left]   = s + "+"\n"+"[right]  = s - "+"\n"+"[,]      = kg +"+"\n"+"[.]      = kg -"+"\n"+"[K]      = K +"+"\n"+"[L]      = K -"+"\n"+"[q]   = shrink horizontal"+"\n"+"[a]   = expand horizontal"+"\n"+"[w]   = rotate up"+"\n"+"[s]   = rotate down"+"\n"+"[e]   = expand vertical"+"\n"+"[d]   = shrink vertical")
    if keys[pygame.K_o]:
        deg1 = 38#14#12 #24 40
        deg2 = 30#50#46 #30 30
        degz = 0.3#2#0.2 #0.2 0.3
        degy = 1 # y+
        player_pos[0] = 0
        player_pos[1] = 0
        player_pos[2] = 0
        kg = 0
        m = 0
        s = 0
        K = 0
        A = 0
        mol = 0
        raiser = 2.6
        default_radius = max(3,3*raiser/2)
        special_radius = int(6*raiser)
        special_radius_A = int(5*raiser)
        special_radius_mol = int(7*raiser)
        special_radius_k = int(3*raiser)

    s = -player_pos[0]
    m = -player_pos[1]
    kg = player_pos[2]

    # Draw grid and player
    draw_grid()
    draw_player()

    # Render the text in the input box
    txt_surface = font2.render(texti, True, (0,200,0))

    # BUTTONS
    txt_buttons = font2.render("-      +", True, (0,200,0))
    screen.blit(txt_buttons, (int(757*raise1), int(83*raise2)))
    txt2_buttons = font2.render(buttontext, True, (0,200,0))
    screen.blit(txt2_buttons, (int(719*raise1), int(111*raise2)))
    
    # Resize the input box if necessary
    width = max(400, txt_surface.get_width() + 10)
    input_box.w = width
    
    # Draw the input box
    pygame.draw.rect(screen, color, input_box, 2)

    draw_buttons()
    
    # Blit the text to the screen
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    # Update display
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()


### CONFIGURATION AND CONTROL ###
'''

[up]     = m +
[down]   = m -
[left]   = s + 
[right]  = s - 
[,]      = kg +
[.]      = kg -
[k]      = K +
[L]      = K -
[h]      = A +
[j]      = A -
[n]      = mol +
[m]      = mol -

[q]   = turn horizontal +
[a]   = turn horizontal -
[w]   = rotate up
[s]   = rotate down
[e]   = expand vertical
[d]   = shrink vertical
[r]   = zoom in
[f]   = zoom out
[t]   = grow bubbles 
[g]   = shrink bubbles 
[z]   = isometric y +
[u]   = isometric y -

'''