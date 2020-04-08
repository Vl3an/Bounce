import pygame 
import numpy as np
import time 
import random
#VARS 
w,h = 720,480 
res = w,h
speed = 70
alpha = 0.1
cubeSize = 5
cubeColor = (255,255,255)
all_sprites = pygame.sprite.Group()
window = pygame.display.set_mode(res)
g = np.array([0,9.81])
#CLASS

class Cube(pygame.sprite.Sprite):
    def __init__(self, pos = [i/2 for i in res],speed = [5,-5]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([cubeSize]*2)
        self.image.fill(cubeColor)
        self.rect = self.image.get_rect()
        #vars
        self.time = time.time()
        self.speed = np.array(speed,float)
        self.pos = np.array(pos,float)
        self.rect.center = pos
        self.hit = False
        #reference
        all_sprites.add(self)
        
    def __str__(self):
        return f'Cube Object : pos = {self.pos}, speed = {self.speed}'


    def update(self):
        pygame.draw.rect(window,(0,0,0),self.rect)
        dt = time.time() - self.time
        self.time = time.time()
        self.speed = self.speed + g*dt
        self.pos = self.pos + self.speed*dt*speed
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        if not self.hit:
            if self.pos[1] >= h:
                self.speed[1] = -self.speed[1]
                #self.pos[1] = h

                self.hit = True
            if self.pos[0] >= w:
                self.speed[0] = -self.speed[0]
                #self.pos[0] = w
                self.hit = True
            if self.pos[1] <= 0:
                self.speed[1] = -self.speed[1]
                #self.pos[1] = 0
                self.hit = True
            if self.pos[0] <= 0:
                self.speed[0] = -self.speed[0]
                #self.pos[0] = 0
                self.hit = True
        else:
            if not any([self.pos[1] >= h,self.pos[1] <= 0,self.pos[0] >= w,self.pos[0] <= 0]):
                self.hit = False
            
        #self.speed = self.speed*0.9999
        pygame.draw.line(window,[30]*3,self.pos + np.array([0,20]),self.pos + np.array([0,20]))        

class Object(pygame.sprite.Sprite):
    all_objects = pygame.sprite.Group()
    def __init__(self,color,width,height,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.color = color
        self.rect.center = pos
        all_sprites.add(self)
        Object.all_objects.add(self)

#SETTINGS
for _ in range(100):
    Cube([random.randint(0,w),random.randint(0,h/2)],[random.randint(-500,500)/100,random.randint(-500,500)/100])

#START
launched = True 
while launched:
    #INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    #MAIN
    all_sprites.update()
    
    all_sprites.draw(window)
    pygame.display.flip()
