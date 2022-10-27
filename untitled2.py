import ast
from pickle import FALSE
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
        draw_ast(i[0], i[1], i[4])

    for i in m_ast:
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
        draw_ast(i[0], i[1], i[4])

    for i in s_ast:
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
        draw_ast(i[0], i[1], i[4])
    

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

        l_ast.append([xpos, ypos, xspd, yspd, gerar_ast('L')])


def spawn_asts_v2(x, y, s):
    if s == 'L':
        for i in range (2):
            yspd = (random.randint(0,int(ast_speedlimit*0.7*10)))/10
            xspd = (random.randint(0, int(ast_speedlimit*0.5*10)))/10

            if bool(random.getrandbits(1)):
                yspd = -yspd
            if bool(random.getrandbits(1)):
                xspd = -xspd

            m_ast.append([x, y, xspd, yspd, gerar_ast('M')])

    elif s == 'M':
        for i in range (2):
            yspd = (random.randint(0,int(ast_speedlimit*10)))/10
            xspd = (random.randint(0, int(ast_speedlimit*0.7*10)))/10

            if bool(random.getrandbits(1)):
                yspd = -yspd
            if bool(random.getrandbits(1)):
                xspd = -xspd
            
            s_ast.append([x, y, xspd, yspd, gerar_ast('S')])


def gerar_ast(s):
    if s == 'L':
        coordenadas = []
        for k in range(8):
            for i in range(1):
                alphas = [random.uniform(0, 45), random.uniform(45, 90), random.uniform(90, 135), random.uniform(135, 180), random.uniform(180, 225), random.uniform(225, 270), random.uniform(270, 315), random.uniform(315, 360)]
                d = random.uniform(l_size*0.9, l_size*1.1)
                i = d * math.cos(math.radians(alphas[k]))
                j = d * math.sin(math.radians(alphas[k]))
                coordenadas.append((i, j))
        return coordenadas

    elif s == 'M':
        coordenadas = []
        for k in range(8):
            for i in range(1):
                alphas = [random.uniform(0, 45), random.uniform(45, 90), random.uniform(90, 135), random.uniform(135, 180), random.uniform(180, 225), random.uniform(225, 270), random.uniform(270, 315), random.uniform(315, 360)]
                d = random.uniform(m_size*0.9, m_size*1.1)
                i = d * math.cos(math.radians(alphas[k]))
                j = d * math.sin(math.radians(alphas[k]))
                coordenadas.append((i, j))
        return coordenadas

    elif s == 'S':
        coordenadas = []
        for k in range(8):
            for i in range(1):
                alphas = [random.uniform(0, 45), random.uniform(45, 90), random.uniform(90, 135), random.uniform(135, 180), random.uniform(180, 225), random.uniform(225, 270), random.uniform(270, 315), random.uniform(315, 360)]
                d = random.uniform(s_size*0.9, s_size*1.1)
                i = d * math.cos(math.radians(alphas[k]))
                j = d * math.sin(math.radians(alphas[k]))
                coordenadas.append((i, j))
        return coordenadas


def draw_ast(x, y, s):
    pos_ast = []
    for i in s:
        pos_ast.append(((i[0]+x),(i[1]+y)))

    pygame.draw.polygon(win, (255,255,255), pos_ast, width=2)


def ship_collision(ship_x, ship_y):
    for i in l_ast:
        dist = abs((((i[0] - ship_x)**2) + ((i[1] - ship_y)**2))**(1/2))
        if dist < l_size*1.15:
            return False
    for i in m_ast:
        dist = abs((((i[0] - ship_x)**2) + ((i[1] - ship_y)**2))**(1/2))
        if dist < m_size*1.15:
            return False  
    for i in s_ast:
        dist = abs((((i[0] - ship_x)**2) + ((i[1] - ship_y)**2))**(1/2))
        if dist < s_size*1.15:
            return False
    return True


def bullet_collision():
    global score
    for bullet in bullets:
        for ast in l_ast:
            dist = abs((((ast[0] - bullet[0])**2) + ((ast[1] - bullet[1])**2))**(1/2))
            if dist < l_size:
                spawn_asts_v2(ast[0], ast[1], 'L')
                l_ast.remove(ast)
                score += 100
                try:
                    bullets.remove(bullet)
                except:
                    pass

        for ast in m_ast:
            dist = abs((((ast[0] - bullet[0])**2) + ((ast[1] - bullet[1])**2))**(1/2))
            if dist < m_size:
                spawn_asts_v2(ast[0], ast[1], 'M')
                m_ast.remove(ast)
                score += 150
                try:
                    bullets.remove(bullet)
                except:
                    pass

        for ast in s_ast:
            dist = abs((((ast[0] - bullet[0])**2) + ((ast[1] - bullet[1])**2))**(1/2))
            if dist < s_size:
                s_ast.remove(ast)
                score += 220
                try:
                    bullets.remove(bullet)
                except:
                    pass


def leveluptest(): 
    if (len(l_ast) == 0) and (len(m_ast) == 0) and (len(s_ast) == 0):
        global  level, start
        level += 1
        start = 1


def draw_ship():
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


def teleport():
    return [(random.randint(0,xsize)), (random.randint(0,ysize))]


pygame.init()

xsize = 900
ysize = 900

win = pygame.display.set_mode((xsize,ysize))

pygame.display.set_caption("Asteroids")

x = xsize/2
y = ysize/2
radius = ysize/60
angle = 180
rotspd = 120
xvel = 0
yvel = 0  
accel = 3
speedlimit = 15
decell = 7
bltspd = 20
edgepenetration = 18
start = 1 
ast_speedlimit = 6
score = 0
l_size = ysize/18
m_size = ysize/30
s_size = ysize/60
lives = 3
ticker = 0

fonte = pygame.freetype.Font("fonte.ttf", 100)

s_ast = []
m_ast = []
l_ast = []

level = 0

bullets = []


run = True
while run:
    pygame.time.delay(16)

    win.fill((0,0,0))
    fonte.render_to(win, (50, 50), str(score) , (255, 255, 255))

    if ticker != 0:
        ticker -= 1

    if start == 1:
        x = xsize/2
        y = ysize/2
        xvel = 0
        yvel = 0
        spawn_asts(level)
        start = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ticker == 0:
                incx = ((math.sin(math.radians(angle)))*bltspd)
                incy = ((math.cos(math.radians(angle)))*bltspd)
                bullets.append([x, y, incx, incy, 0])

            if event.key == pygame.K_DOWN:
                newpos = teleport()
                ticker = 60
                x = newpos[0]
                y = newpos[1]

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        angle += rotspd/20
        
    if keys[pygame.K_RIGHT]:
        angle -= rotspd/20
    
    if keys[pygame.K_UP]:
        if abs(yvel) < speedlimit:
            yvel += (math.cos(math.radians(angle)))*accel/20
        elif yvel > 0 and (math.cos(math.radians(angle)))*accel/20 < 0:
            yvel += (math.cos(math.radians(angle)))*accel/20
        elif yvel < 0 and (math.cos(math.radians(angle)))*accel/20 > 0:
            yvel += (math.cos(math.radians(angle)))*accel/20
        
        if abs(xvel) < speedlimit:
            xvel += (math.sin(math.radians(angle)))*accel/20
        elif xvel > 0 and (math.sin(math.radians(angle)))*accel/20 < 0:
            xvel += (math.sin(math.radians(angle)))*accel/20
        elif xvel < 0 and (math.sin(math.radians(angle)))*accel/20 > 0:
            xvel += (math.sin(math.radians(angle)))*accel/20

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

    if not run:
        break

    if ticker == 0:
        draw_ship()
        run = ship_collision(x, y)

    updatebullets()
    updateasts()
    bullet_collision()
    leveluptest()

    pygame.display.update()
pygame.quit()