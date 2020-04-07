import RPi.GPIO as GPIO
import time
import sys
import pygame
from pygame.locals import *
#from unicurses import *

rf = 18  #pin12
rb = 23  #pin16

lf = 4  #pin 7
lb = 17  #pin 11

frf = 24  #18
frb = 25  #22

flf = 27  #13
flb = 22  #15

brf = 20  #rightForward
brb = 21  #rightBackwards

blf = 19  #rightForward
blb = 26  #rightBackwards

GPIO.setmode(GPIO.BCM)

GPIO.setup(rf,GPIO.OUT)
GPIO.setup(rb,GPIO.OUT)
GPIO.setup(lf,GPIO.OUT)
GPIO.setup(lb,GPIO.OUT)

GPIO.output(rf,GPIO.LOW)
GPIO.output(rb,GPIO.LOW)
GPIO.output(lf,GPIO.LOW)
GPIO.output(lb,GPIO.LOW)

rightForward = GPIO.PWM(rf, 1000)
rightBackward = GPIO.PWM(rb, 1000)
leftForward = GPIO.PWM(lf, 1000)
leftBackward = GPIO.PWM(lb, 1000)


GPIO.setup(frf,GPIO.OUT)
GPIO.setup(frb,GPIO.OUT)
GPIO.setup(flf,GPIO.OUT)
GPIO.setup(flb,GPIO.OUT)
GPIO.setup(brf,GPIO.OUT)
GPIO.setup(brb,GPIO.OUT)
GPIO.setup(blf,GPIO.OUT)
GPIO.setup(blb,GPIO.OUT)

GPIO.output(frf,GPIO.LOW)
GPIO.output(frb,GPIO.LOW)
GPIO.output(flf,GPIO.LOW)
GPIO.output(flb,GPIO.LOW)
GPIO.output(brf,GPIO.LOW)
GPIO.output(brb,GPIO.LOW)
GPIO.output(blf,GPIO.LOW)
GPIO.output(blb,GPIO.LOW)

frontRF = GPIO.PWM(frf, 1000)
frontRB = GPIO.PWM(frb, 1000)
frontLF = GPIO.PWM(flf, 1000)
frontLB = GPIO.PWM(flb, 1000)
backRF = GPIO.PWM(brf, 1000)
backRB = GPIO.PWM(brb, 1000)
backLF = GPIO.PWM(blf, 1000)
backLB = GPIO.PWM(blb, 1000)



duty = 100;
noseDuty = 100;

def backward():
    stop()
    rightBackward.start(duty)
    leftBackward.start(duty)

def forward():
    stop()
    rightForward.start(duty)
    leftForward.start(duty)

def right():
    stop()
    rightForward.start(duty)
    leftBackward.start(duty)
    
def left():
    stop()
    leftForward.start(duty)
    rightBackward.start(duty)
    
def stop():
    rightForward.stop()
    rightBackward.stop()
    leftForward.stop()
    leftBackward.stop()
    
    
    
    
    
    
def fLBackward():
    fLStop()
    frontLB.start(noseDuty)

def fLForward():
    fLStop()
    frontLF.start(noseDuty)
    
def fLStop():
    frontLF.stop()
    frontLB.stop()
    
    
    
def fRBackward():
    fRStop()
    frontRB.start(noseDuty)

def fRForward():
    fRStop()
    frontRF.start(noseDuty)

def fRStop():
    frontRF.stop()
    frontRB.stop()
    
    
    
    
def bLBackward():
    bLStop()
    backLB.start(noseDuty)

def bLForward():
    bLStop()
    backLF.start(noseDuty)

def bLStop():
    backLF.stop()
    backLB.stop()
    
    
    
    
    
def bRBackward():
    bRStop()
    backRB.start(noseDuty)

def bRForward():
    bRStop()
    backRF.start(noseDuty)

def bRStop():
    backRF.stop()
    backRB.stop()
    
   
   
    
    
def fAllBackward():
    fAllStop()
    frontRB.start(noseDuty)
    frontLB.start(noseDuty)

def fAllForward():
    fAllStop()
    frontRF.start(noseDuty)
    frontLF.start(noseDuty)
    
def fAllStop():
    frontRF.stop()
    frontRB.stop()
    frontLF.stop()
    frontLB.stop()
    
    
    
    
def bAllBackward():
    bAllStop()
    backRB.start(noseDuty)
    backLB.start(noseDuty)

def bAllForward():
    fAllStop()
    backRF.start(noseDuty)
    backLF.start(noseDuty)
    
def bAllStop():
    backRF.stop()
    backRB.stop()
    backLF.stop()
    backLB.stop()
    
    
    
    
def allStop():
    bAllStop()
    fAllStop()
    
    
    
 
 
def motorControl():
    if x[pygame.K_UP]:
        forward()
    elif x[pygame.K_LEFT]:
        left()
    elif x[pygame.K_RIGHT]:
        right()
    elif x[pygame.K_DOWN]:
        backward()
    else:
        stop()
        
def noseControl():
    if x[pygame.K_q]:
        fLForward()
    elif x[pygame.K_w]:
        fLBackward()
    elif x[pygame.K_e]:
        fRForward()
    elif x[pygame.K_r]:
        fRBackward()
        
    elif x[pygame.K_a]:
        bLForward()
    elif x[pygame.K_s]:
        bLBackward()
    elif x[pygame.K_d]:
        bRForward()
    elif x[pygame.K_f]:
        bRBackward()
        
    elif x[pygame.K_z]:
        fAllForward()
    elif x[pygame.K_x]:
        fAllBackward()
    elif x[pygame.K_c]:
        bAllForward()
    elif x[pygame.K_v]:
        bAllBackward()
    else:
        allStop()
        
        
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Hack Rover")


running = True;
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GPIO.cleanup()
            sys.exit()
            
        elif event.type == KEYDOWN and event.key == K_1:
            duty = 10
        elif event.type == KEYDOWN and event.key == K_2:
            duty = 20
        elif event.type == KEYDOWN and event.key == K_3:
            duty = 30
        elif event.type == KEYDOWN and event.key == K_4:
            duty = 40
        elif event.type == KEYDOWN and event.key == K_5:
            duty = 50
        elif event.type == KEYDOWN and event.key == K_6:
            duty = 60
        elif event.type == KEYDOWN and event.key == K_7:
            duty = 70
        elif event.type == KEYDOWN and event.key == K_8:
            duty = 80
        elif event.type == KEYDOWN and event.key == K_9:
            duty = 90
        elif event.type == KEYDOWN and event.key == K_0:
            duty = 100

        
    
    x = pygame.key.get_pressed()
    
    if x[pygame.K_UP]:
        forward()
        noseControl()
    elif x[pygame.K_LEFT]:
        left()
        noseControl()
    elif x[pygame.K_RIGHT]:
        right()
        noseControl()
    elif x[pygame.K_DOWN]:
        backward()
        noseControl()
        
    elif x[pygame.K_q]:
        fLForward()
        motorControl()
    elif x[pygame.K_w]:
        fLBackward()
        motorControl()
    elif x[pygame.K_e]:
        fRForward()
        motorControl()
    elif x[pygame.K_r]:
        fRBackward()
        motorControl()
        
    elif x[pygame.K_a]:
        bLForward()
        motorControl()
    elif x[pygame.K_s]:
        bLBackward()
        motorControl()
    elif x[pygame.K_d]:
        bRForward()
        motorControl()
    elif x[pygame.K_f]:
        bRBackward()
        motorControl()
        
    elif x[pygame.K_z]:
        fAllForward()
        motorControl()
    elif x[pygame.K_x]:
        fAllBackward()
        motorControl()
    elif x[pygame.K_c]:
        bAllForward()
        motorControl()
    elif x[pygame.K_v]:
        bAllBackward()
        motorControl()
    else:
        allStop()
        stop()
        
        
    time.sleep(0.1)
