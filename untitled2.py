import pygame
import math

def updatebullets():
    for i in bullets:
        if i[4] < 80: 
            i[0] += i[2]
            i[1] += i[3]
            i[4] += 1
            if i[0] > xsize:
                i[0] = i[0] - xsize
                i[4] += 50
            if i[1] > ysize:
                i[1] = i[1] - ysize
                i[4] += 50
            if i[0] < 0:
                i[0] = xsize - i[0]
                i[4] += 50
            if i[1] < 0:
                i[1] = ysize - i[1]
                i[4] += 50
            pygame.draw.circle(win, (255,255,255), (i[0], i[1]), 5.0, width=0)

        else:
            bullets.remove(i)


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
speedlimit = 20
decell = 7
bltspd = 20

bullets = []

run = True
while run:
    pygame.time.delay(16)

    win.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                incx = ((math.sin(math.radians(angle)))*bltspd)
                incy = ((math.cos(math.radians(angle)))*bltspd)
                print(incx, incy)
                bullets.append([x, y, incx, incy, 0])
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        angle += rotspd/10
        
    if keys[pygame.K_RIGHT]:
        angle -= rotspd/10
    
    if keys[pygame.K_UP]: #and yvel > -speedlimit:
        yvel += (math.cos(math.radians(angle)))*accel/10
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

    pygame.display.update()
pygame.quit()