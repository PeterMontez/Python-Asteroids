import pygame
import math

print(math.cos(math.radians(1)))

pygame.init()

xsize = 750
ysize = 750

win = pygame.display.set_mode((xsize,ysize))

pygame.display.set_caption("First Game")

x = xsize/2
y = ysize/2
radius = 15
angle = 0
rotspd = 70
width = 40
height = 40
xvel = 0
yvel = 0
accel = 3
speedlimit = 20
decell = 7

run = True
while run:
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    # if keys[pygame.K_LEFT] and xvel > -speedlimit:
    #     xvel -= accel/10
    # else:
    #     xvel = xvel/(1+(decell/1000))
    
    if keys[pygame.K_LEFT]:
        angle += rotspd/10
        
    if keys[pygame.K_RIGHT]:
        angle -= rotspd/10
    
    # if keys[pygame.K_RIGHT] and xvel < speedlimit:
    #     xvel += accel/10
    # else:
    #     xvel = xvel/(1+(decell/1000))
    if keys[pygame.K_UP] and yvel > -speedlimit:
        yvel -= accel/10
    else:
        yvel = yvel/(1+(decell/1000))
    if keys[pygame.K_DOWN] and yvel < speedlimit:
        yvel += accel/10
    else:
        yvel = yvel/(1+(decell/1000))
    
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
    
    point1 = (((math.sin(math.radians(angle)))*radius)+50,((math.cos(math.radians(angle)))*radius)+50)
    point2 = (((math.sin(math.radians(anglep2)))*radius)+50,((math.cos(math.radians(anglep2)))*radius)+50)
    point3 = (((math.sin(math.radians(anglep3)))*radius)+50,((math.cos(math.radians(anglep3)))*radius)+50)
    
    position = (point1, point2)
    

    win.fill((0,0,0))
    pygame.draw.line(win, (0,255,0), point1, point2)
    pygame.draw.line(win, (0,255,0), point2, point3)
    pygame.draw.line(win, (0,255,0), point3, point1)
    pygame.display.update()
pygame.quit()