#brüche_raten

import random
import time
import pygame

start_time = time.time()
points = 0
endpoints = 0
p10 = False
p20 = False

print()
print("target precision of 5 decimal places :) ")
print()
'''
while True:
    start_time = time.time()
    print()
    a = random.randint(1,100)
    b = random.randint(1,10)
    print("what is ",a,"/",b," equal to?")
    inp = input("enter decimal:  ")
    if b < 11:
        limi = 0.00007
    else:
        limi = 0.007
    if abs(a/b - float(inp)) < limi:
        print("well done!  its ", a/b)
        brain_time = int(time.time() - start_time)
        print("brain time: ",brain_time," seconds")
        if b == 1 or b == 2:
            if points > 10:
                points += 0.7/brain_time
            else:    
                points += 4/brain_time
        else:
            if points > 10:
                points += 2/brain_time
            else:
                points += 10/brain_time
        print("your points: ",points)
    else:
        print("not quite, try again! its ",a/b)
        brain_time = int(time.time() - start_time)
        print("brain time: ",brain_time," seconds")
        points -= 1
        print("your points: ",points)
    
    if points > 10 and p10 == False:
        print()
        print("N   N  i   CCCc  EEEE   !")
        print("NN  N  i  C      Eee    !")
        print("N N N  i  C      E       ")
        print("N  NN  i   CCCc  EEEEE  !")
        print()
        p10 = True

    if points > 20 and p20 == False:
        print()
        print("H   H  aAAa  RRRr   DDDd  cCCc  oOOo   RRRr   EEEE")
        print("H   H  A  A  R   R  D  D  C     O   O  R   R  Eeee")
        print("HHHHH  AAAA  RRRr   D  D  C     0   O  RRRr   E")
        print("H   H  A  A  R   R  DDD   CCCc   OOO   R   R  EEEE") 
        print()
        p20 = True
    #print()
    #time.sleep(1)
'''

pygame.init()

width, height = 670, 440
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("input")

font4 = pygame.font.Font(None, 23)
font3 = pygame.font.Font(None, 37)
font2 = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 20)

input_box = pygame.Rect(100, 100, 400, 50)
color_inactive = ((0,100,0))
color_active = pygame.Color('dodgerblue')
color = color_inactive

active = False
texti = ''
texti2 = '0'
texti3 = ''
texti4 = ''
done = False
run = False
a = random.randint(2,100)
b = random.randint(2,10)
while b == 10:
    b = random.randint(2,10)
labelab = font1.render(str("a < 100"+"\n"+"b < 20"), True, (0,200,0))  # White text    
labelab_rect = labelab.get_rect(topleft=(537, 117))

label = font1.render("", True, (0,200,0))  # White text
label_rect = label.get_rect(center=(120, 70))

start_time = time.time()
mode = 1
quest = 1
total_time = 0
wrong = False
wrong2 = False

with open("brueche_highscore.txt", 'r') as file:
    old_highscore = file.read()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if quest < 8:
                    texti2 = ""
                    texti3 = ""
                    texti4 = ""
                    quest = 1
                    print("quest:",quest)
                    brain_time = 0
                    points = 0
                    start_time = time.time()
                    with open("brueche_highscore.txt", 'r') as file:
                        old_highscore = file.read()
            if active:
                if event.key == pygame.K_RETURN:
                    quest += 1
                    if quest >= 10:
                        quest = 1
                        texti2 = ""
                        texti3 = ""
                        texti4 = ""
                        brain_time = 0
                        points = 0
                        start_time = time.time()
                        with open("brueche_highscore.txt", 'r') as file:
                            old_highscore = file.read()
                    if len(texti) < 1:
                        texti = "1"                # Enter key submits the text (prints it here)
                    if "," in texti:
                        texti = "1"
                        wrong = True
                    if "r" in texti:
                        texti = "1"
                        wrong = True
                    if len(texti) > 0:
                        if texti[-1] == "0":
                            wrong2 = True
                    print(texti," <~ your answer")
                    texti2 = texti
                    texti4 = texti
                    texti = ''  # Clear the input after submitting
                    run = True
                elif event.key == pygame.K_BACKSPACE:
                    texti = texti[:-1]  # Remove last character on Backspace
                else:
                    texti += event.unicode  # Add the typed character to the text
    screen.fill((0,0,0))
    if run == True and quest < 9:
        if b < 11:
            limi = 0.00007
        else:
            limi = 0.007
        texti3 = ""
        if wrong == True:
            texti3 += str("please enter digits with (.) not (,)")
            wrong = False
        if wrong2 == True:
            texti3 += str("thats trivial..")
            print("trivial..")
            #wrong2 = False
        if mode == 1 and "/" not in texti2:
            texti3 += str("thats not a valid quotient!")
            texti2 = "1"
        elif mode == 1 and "/" in texti2:
            texti2 = str(eval(texti2))
        elif mode == 0 and "/" in texti2: 
            texti3 += str("you should do it yourself!")
            texti2 = "1"
        if abs(a/b - float((texti2))) < limi:
            texti3 = str("well done! ")
            texti3 += str("\n")
            texti3 += str("\n")
            if mode == 0:
                texti3 += str(texti4+" <~ your answer ")
            else:
                texti3 += str(texti4+" = "+texti2+" <~ your answer ")
            texti3 += str("\n")
            texti3 += str(str(a)+"/"+str(b)+" = "+str(a/b))
            print(str(str(a)+"/"+str(b)+" = "+str(a/b)))
            brain_time = int(time.time() - start_time)
            if brain_time == 0:
                brain_time = 100
            if wrong2 == True:
                points += 0
            else:
                points += 7
            texti3 += str("\n")
            texti3 += str("brain time: "+str(brain_time)+" seconds")
            if b == 1 or b == 2 or b == 10:
                points += 7/brain_time
            else:
                if wrong2 == True:
                    points += 2
                elif b > 12:
                    points += 97/brain_time
                else:
                    points += 37/brain_time
            texti3 += str("\n")
            texti3 += str("your points: "+str(points))
        else:
            texti3 += str("\n")
            texti3 += str("not quite, try again! ")
            texti3 += str("\n")
            texti3 += str("\n")
            if mode == 0:
                texti3 += str(texti4+" <~ your answer ")
            else:
                texti3 += str(texti4+" = "+texti2+" <~ your answer ")
            texti3 += str("\n")
            texti3 += str(str(a)+"/"+str(b)+" = "+str(a/b))
            print(str(str(a)+"/"+str(b)+" = "+str(a/b)))
            brain_time = int(time.time() - start_time)
            texti3 += str("\n")
            texti3 += str("brain time: "+str(brain_time)+" seconds")
            points -= 1
            texti3 += str("\n")
            texti3 += str("your points: "+str(points))
        print("points: ",points)
        print("brain_time: ",brain_time)
        print()
        print("quest:",quest)
        if quest == 8:
            endpoints = points
            print("endpoints:",points)
        if quest == 1:
            points = 0
            texti3 = ""
        if wrong2 == True:
            wrong2 = False
        if quest < 8:
            a = random.randint(1,100)
            if random.randint(0,7) == 7 and mode == 0:
                b = random.randint(2,20)
            else:
                b = random.randint(2,11)
            while (a/b)%1 == 0 or b == 10 or (a%2 and b == 2):  # or b not in primes:
                a = random.randint(1,100)
                if random.randint(2,7) == 7:
                    b = random.randint(2,20)
                else:
                    b = random.randint(2,11)
            start_time = time.time()
        run = False
        if random.randint(1,7) < 4:
            mode = 0
        else:
            mode = 1
        #quest += 1
    if quest == 9:
        screen.fill((0,0,0))
        score_text = ""
        filename = "brueche_highscore.txt"
        # 67.37784576534577
        with open(filename, 'r') as file:
            file_content = file.read()
            highscore = file_content
        if float(file_content) < endpoints:
            highscore = endpoints
            input_text = str(endpoints)
            with open(filename, "w") as file:
                file.write(input_text)
        score_text += ("\n"+"total points: "+str(round(endpoints,7))+"\n"+
                    "\n"+"new highscore: "+str(round(float(highscore),7))+" points "+"\n"+
                    "\n"+"old highscore: "+str(round(float(old_highscore),7))+" points "+"\n"+"\n"+"\n"+"\n"+"  press [r] to restart")
        label = font3.render(score_text, True, (0,200,0))  # White text    
        label_rect = label.get_rect(topleft=(37, 47))
        screen.blit(label, label_rect)
    else:
        if quest != 8:
            brain_time_new = int(time.time() - start_time)
            if mode == 0:
                label = font2.render(str("what is "+str(a)+"/"+str(b)+" equal to?   sec: "+str(brain_time_new)), True, (0,200,0))  # White text
            else:
                label = font2.render(str("which a/b equal "+str(round(a/b,7))+"   sec: "+str(brain_time_new)), True, (0,200,0))  # White text    
            label_rect = label.get_rect(topleft=(37, 47))
            screen.blit(label, label_rect)
            if mode != 0:
                screen.blit(labelab, labelab_rect)
            if len(str(texti)) < 6:
                txt_surface = font2.render(texti, True, (200,0,0)) 
            elif len(str(texti)) == 6:
                txt_surface = font2.render(texti, True, (120,120,0)) 
            elif len(str(texti)) == 7:
                txt_surface = font2.render(texti, True, (70,170,20)) 
            else:
                txt_surface = font2.render(texti, True, (0,200,0)) 
            
            width2 = max(400, txt_surface.get_width() + 10)
            input_box.w = width2
            
            pygame.draw.rect(screen, color, input_box, 2)
            
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            
            labelq = font4.render(str("question:"+"\n"+"    "+str(quest)+"/7"), True, (0,200,0))  # White text    
            labelq_rect = labelq.get_rect(topleft=(537, 177))
            screen.blit(labelq, labelq_rect)

        txt_surface2 = font3.render(texti3, True, (0,200,0))
        screen.blit(txt_surface2, (70, 200))
        
    pygame.display.flip()

pygame.quit()

'''
HIGHSCORE:

quest: 1
2.125  <~ your answer
17/8 = 2.125
points:  19.333333333333336
brain_time:  3

quest: 2
27.33333  <~ your answer
82/3 = 27.333333333333332
points:  29.179487179487182
brain_time:  13

quest: 3
2.166666  <~ your answer
13/6 = 2.1666666666666665
points:  43.57948717948718
brain_time:  5

quest: 4
27/2  <~ your answer
81/6 = 13.5
points:  57.97948717948718
brain_time:  5

quest: 5
5/7  <~ your answer
5/7 = 0.7142857142857143
points:  68.34312354312354
brain_time:  11

quest: 6
10/6  <~ your answer
5/3 = 1.6666666666666667
points:  81.50979020979021
brain_time:  6

quest: 7
26/3  <~ your answer
52/6 = 8.666666666666666
points:  92.20979020979021
brain_time:  10 

old: 69.8652015
old: 89.345
'''