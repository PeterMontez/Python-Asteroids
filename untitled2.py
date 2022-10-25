import ast
import pygame
import math
import random

def updatebullets():
    for i in bullets:
        if i[4] < 80: 
            i[0] += i[2]
            i[1] += i[3]
            i[4] += 1
            if i[0] > xsize:
                i[0] = i[0] - xsize
                i[4] += xsize/edgepenetration
            if i[1] > ysize:
                i[1] = i[1] - ysize
                i[4] += ysize/edgepenetration
            if i[0] < 0:
                i[0] = xsize - i[0]
                i[4] += xsize/edgepenetration
            if i[1] < 0:
                i[1] = ysize - i[1]
                i[4] += ysize/edgepenetration
            pygame.draw.circle(win, (255,255,255), (i[0], i[1]), 5.0, width=0)

        else:
            bullets.remove(i)

def updateasts():
    for i in l_ast:
        i[0] += i[2]
        i[1] += i[3]
        if i[0] > xsize:
            i[0] = i[0] - xsize
        if i[1] > ysize:
            i[1] = i[1] - ysize
        if i[0] < 0:
            i[0] = xsize - i[0]
        if i[1] < 0:
            i[1] = ysize - i[1]
        draw_ast(i[0], i[1], 50.0)

def spawn_asts(level):
    for i in range(int((level+1)/2)+4):
        ypos = random.randint(0,ysize)
        if bool(random.getrandbits(1)):
            xpos = random.randint(0, int((xsize/4)))
        else:
            xpos = random.randint(int((xsize/2*1.5)), xsize)

        yspd = (random.randint(int(ast_speedlimit*10/5),int(ast_speedlimit/2*10)))/10
        xspd = (random.randint(0, int(ast_speedlimit*10/9)))/10

        if bool(random.getrandbits(1)):
            yspd = -yspd
        if bool(random.getrandbits(1)):
            xspd = -xspd

        l_ast.append([xpos, ypos, xspd, yspd])

def draw_ast(x, y, s):
    pygame.draw.circle(win, (255,255,255), (x, y), s, width=10)

def ship_collision(ship_x, ship_y):
    for i in l_ast:
        dist = abs((((i[0] - ship_x)**2) + ((i[1] - ship_y)**2))**(1/2))
        if dist < 50.0:
            print("BATEU")

pygame.init()

xsize = 900
ysize = 900

win = pygame.display.set_mode((xsize,ysize))

pygame.display.set_caption("First Game")

x = xsize/2
y = ysize/2
radius = 15
angle = 180
rotspd = 70
xvel = 0
yvel = 0
accel = 3
speedlimit = 15
decell = 7
bltspd = 20
edgepenetration = 18
start = 1
ast_speedlimit = 8

s_ast = []
m_ast = []
l_ast = []

level = 0

bullets = []


run = True
while run:
    pygame.time.delay(16)
    #pygame.time.delay(1000)

    win.fill((0,0,0))

    if start == 1:
        spawn_asts(level)
        start = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                incx = ((math.sin(math.radians(angle)))*bltspd)
                incy = ((math.cos(math.radians(angle)))*bltspd)
                bullets.append([x, y, incx, incy, 0])
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        angle += rotspd/10
        
    if keys[pygame.K_RIGHT]:
        angle -= rotspd/10
    
    if keys[pygame.K_UP]:
        if abs(yvel) < speedlimit:
            yvel += (math.cos(math.radians(angle)))*accel/10
        elif yvel > 0 and (math.cos(math.radians(angle)))*accel/10 < 0:
            yvel += (math.cos(math.radians(angle)))*accel/10
        elif yvel < 0 and (math.cos(math.radians(angle)))*accel/10 > 0:
            yvel += (math.cos(math.radians(angle)))*accel/10
        
        if abs(xvel) < speedlimit:
            xvel += (math.sin(math.radians(angle)))*accel/10
        elif xvel > 0 and (math.sin(math.radians(angle)))*accel/10 < 0:
            xvel += (math.sin(math.radians(angle)))*accel/10
        elif xvel < 0 and (math.sin(math.radians(angle)))*accel/10 > 0:
            xvel += (math.sin(math.radians(angle)))*accel/10

    else:
        yvel = yvel/(1+(decell/1000))
        xvel = xvel/(1+(decell/1000))
    
    if angle < 0:
        angle += 360
    elif angle >= 360:
        angle -= 360
        
    x = x + xvel
    y = y + yvel

    if x > xsize:
        x = x - xsize
    if y > ysize:
        y = y - ysize
    if x < 0:
        x = xsize - x
    if y < 0:
        y = ysize - y
    
    anglep2 = angle + 135
    anglep3 = angle + 135 + 90
    
    if anglep2 >= 360:
        anglep2 -= 360
        
    if anglep3 >= 360:
        anglep3 -= 360
    
    point1 = (((math.sin(math.radians(angle)))*radius)+x,((math.cos(math.radians(angle)))*radius)+y)
    point2 = (((math.sin(math.radians(anglep2)))*radius)+x,((math.cos(math.radians(anglep2)))*radius)+y)
    point3 = (((math.sin(math.radians(anglep3)))*radius)+x,((math.cos(math.radians(anglep3)))*radius)+y)
    pos = [point1, point2, point3]
    
    midfire = (((math.sin(math.radians(angle)))*(radius-40))+x,((math.cos(math.radians(angle)))*(radius-40))+y)
    pointfire = (((math.sin(math.radians(angle)))*(radius-30))+x,((math.cos(math.radians(angle)))*(radius-30))+y)

    pygame.draw.polygon(win, (0,255,0), pos, width= 2)

    if keys[pygame.K_UP]:
        pygame.draw.line(win, (255,127,0), midfire, pointfire, width=5)

    updatebullets()
    updateasts()
    ship_collision(x, y)

    pygame.display.update()
pygame.quit()