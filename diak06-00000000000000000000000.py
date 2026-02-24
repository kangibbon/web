from neoled import setpixel, clearmatrix
from machine import Pin, Timer
from time import ticks_ms as ora
from machine import ADC
from machine import Pin, PWM
import time
 







KL1ido = Timer(0)

BGláb = Pin(8, Pin. IN, Pin. PULL_UP)
JGláb = Pin (7, Pin. IN, Pin. PULL_UP)


def BGomb(): return not BGláb.value()
def JGomb(): return not JGláb.value()

BGelozo = BGomb(); JGelozo = JGomb();
figyelem = 1
szabad = 2
felkeszul = 3
tilos = 4

piros = (20,0,0)
sarga = (20,10,0)
zold = (0,20,3)
sotet = (0,0,1)

sebszorzo = 5


def KL1kirajzol():
    if KL1allapot == tilos:
        #e
        clearmatrix((0,0,0),1)
        setpixel( (2,0), piros)
        setpixel( (2,1), piros )
        setpixel( (2,2), piros )
        setpixel( (2,3), piros )
        #kozepso izzo
        setpixel( (2,4), piros )
        setpixel( (2,5), piros )
        setpixel( (2,6), piros )
        setpixel( (2,7), piros )
        setpixel( (2,4), piros )
        setpixel( (3,0), piros )
        setpixel( (4,0), piros )
        setpixel( (5,0), piros )
        setpixel( (3,7), piros )
        setpixel( (4,7), piros )
        setpixel( (5,7), piros )
        setpixel( (3,3), piros )
        setpixel( (4,3), piros )
        setpixel( (2,5), piros, True)
        
                
    elif KL1allapot == figyelem:
        #F
        
        clearmatrix((0,0,0),1)
        setpixel( (2,0), piros )
        setpixel( (2,1), piros )
        setpixel( (2,2), piros )
        setpixel( (2,3), piros )
        #kozepso izzo
        setpixel( (2,4), piros )
        setpixel( (2,5), piros )
        setpixel( (2,6), piros )
        setpixel( (3,0), piros )
        setpixel( (4,0), piros )
        setpixel( (5,0), piros )
        setpixel( (3,3), piros )
        setpixel( (4,3), piros )
        setpixel( (2,7), piros, True)
        
        
    
    elif KL1allapot == szabad:
        #I
        clearmatrix((0,0,0),1)
        setpixel( (2,0), piros )
        setpixel( (2,2), piros )
        setpixel( (2,3), piros )
        #kozepso izzo
        setpixel( (2,4), piros )
        setpixel( (2,5), piros )
        setpixel( (2,6), piros )
        #also izzo
        setpixel( (2,4), piros )
        setpixel( (2,5), piros )
        setpixel( (2,6), piros )
        setpixel( (2,7), piros, True)
    
    elif KL1allapot == felkeszul:
        #C
        clearmatrix((0,0,0),1)
        setpixel( (3,0), piros )
        setpixel( (2,1), piros )
        setpixel( (4,0), piros )
        setpixel( (5,0), piros )        
        setpixel( (2,3), piros )
        #kozepso izzo
        setpixel( (2,4), piros )
        setpixel( (2,5), piros )
        setpixel( (2,6), piros )
        setpixel( (2,2), piros )
        #also izzo
        setpixel( (4,7), piros )
        setpixel( (5,7), piros )
        setpixel( (3,7), piros, True)
        
 
 
 
 
 
 
def KL1idolejart(t):
        
    global KL1allapot
    
        
    if KL1allapot==figyelem:
            KL1allapot = tilos
            KL1kirajzol()
            KL1ido.init(mode=Timer.ONE_SHOT, period=400*sebszorzo, callback=KL1idolejart)
            
    elif KL1allapot==szabad:
            KL1allapot=figyelem
            KL1kirajzol()
            KL1ido.init(mode=Timer.ONE_SHOT, period=400*sebszorzo, callback=KL1idolejart)
            
        
    elif KL1allapot==felkeszul:
        KL1allapot = szabad
        KL1kirajzol()
        KL1ido.init(mode=Timer.ONE_SHOT, period=400*sebszorzo, callback=KL1idolejart)
        
    elif KL1allapot==tilos:
        KL1allapot = felkeszul
        KL1kirajzol()
        KL1ido.init(mode=Timer.ONE_SHOT, period=400*sebszorzo, callback=KL1idolejart)
        
        
KL1allapot = figyelem
KL1kirajzol()
KL1ido.init(mode=Timer.ONE_SHOT, period=400*sebszorzo, callback=KL1idolejart)

H = 20
adatokx = []
adatoky = []

while True:
    joystickx = ADC(0, atten=ADC.ATTN_11DB)
    adatokx.append(joystickx.read_uv()/1000000),
    dbx = len(adatokx)
    if dbx > H:
        adatokx.pop(0)
        dbx = len(adatokx)
    
    atlagx = sum(adatokx)/dbx
    
# -- Y koordinátán a joystick adatai
    joysticky = ADC(1, atten=ADC.ATTN_11DB)
    adatoky.append(joysticky.read_uv()/1000000),
    dby = len(adatoky)
    if dby > H:
        adatoky.pop(0)
        dby = len(adatoky)
    
    atlagy = sum(adatoky)/dby
    sebszorzo = int(20*atlagx)
   
   
   
   
   
   
   


