import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("verlet balls")

#define lists
xloc = []
yloc = []
xbef = []
ybef = []
rad = []
Red = []
Green = []
Blue = []

def collision(a, b):
    coldist = math.sqrt((xloc[a]-xloc[b])*(xloc[a]-xloc[b]) + (yloc[a]-yloc[b])*(yloc[a]-yloc[b]))
    r1 = rad[a]
    r2 = rad[b]
    x1 = xloc[a]
    x2 = xloc[b]
    y1 = yloc[a]
    y2 = yloc[b]
    if r1 + r2 > coldist:
        dist2 = ((coldist - r1)-r2)*((r1*r1)/((r1*r1)+(r2*r2)))
        dist1 = ((coldist - r1)-r2)*((r2*r2)/((r1*r1)+(r2*r2)))
        xloc[a] = x1+(((x2-x1)/coldist)*dist1)
        yloc[a] = y1+(((y2-y1)/coldist)*dist1)
        xloc[b] = x2+(((x1-x2)/coldist)*dist2)
        yloc[b] = y2+(((y1-y2)/coldist)*dist2)

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = pygame.mouse.get_pos()
                
                add_rad = random.randint(37, 60)
                rad.append(add_rad)
                if y_pos > HEIGHT - add_rad:
                    y_pos = HEIGHT - add_rad
                if y_pos < add_rad:
                    y_pos = add_rad
                if x_pos < add_rad:
                    x_pos = add_rad
                if x_pos > WIDTH - add_rad:
                    x_pos = WIDTH - add_rad
                xloc.append(x_pos)
                yloc.append(y_pos)
                xbef.append(x_pos)
                ybef.append(y_pos)
                Red.append(random.randint(100, 255))
                Blue.append(random.randint(100, 255))
                Green.append(random.randint(100, 255))
        
        #rendering circles
        WIN.fill((0, 0, 0))
        if len(Red) > 0:
            for i in range(len(yloc)):
                pygame.draw.circle(WIN, [Red[i], Green[i], Blue[i]], [xloc[i],yloc[i]], rad[i])


        #physics
        for i in range(len(yloc)):
            Xc = xloc[i]
            Yc = yloc[i]
            savex = xloc[i]
            savey = yloc[i]
            Xp = xbef[i]
            Yp = ybef[i]
            
            Yc = Yc + 0.0004
            Yc = Yc + (Yc - Yp)
            Xc = Xc + (Xc -Xp)
            
            #border
            if Yc > HEIGHT - rad[i]:
                Yc = HEIGHT - rad[i]
                Xc = Xc + (-0.0004 * (Xc-Xp))
            if Xc < rad[i]:
                Xc = rad[i]
            if Xc > WIDTH - rad[i]:
                Xc = WIDTH - rad[i]
            if Yc < rad[i]:
                Yc = rad[i]

            yloc[i] = Yc
            xloc[i] = Xc
            xbef[i] = savex
            ybef[i] = savey
        
        #collision
        for i in range(len(yloc)):
                for j in range(len(yloc)):
                        if j != i:
                            collision(i, j)
                

        pygame.display.update()
    
    print("balls: ", len(yloc))
    pygame.quit()


if __name__ == "__main__":
    main()