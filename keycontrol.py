import keyboard
import time
import sys, termios, tty, os
import RPi.GPIO as GPIO
import pigpio

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

grijperPIN = 17 # Board pin 11, BCM pin 17
bovenoPIN = 27 # Board pin 13, BCM pin 27
linksrPIN = 22 # Board pin 15, BCM pin 22
vooraPIN = 23 # Board pin 16, BCM pin 23

pwm = pigpio.pi()
pwm.set_mode(grijperPIN, pigpio.OUTPUT) # schakel GPIO pin op output (standaard input)
pwm.set_mode(bovenoPIN, pigpio.OUTPUT)
pwm.set_mode(linksrPIN, pigpio.OUTPUT)
pwm.set_mode(vooraPIN, pigpio.OUTPUT)

pwm.set_PWM_frequency( grijperPIN, 50 ) # grijper
pwm.set_PWM_frequency( bovenoPIN, 50 ) # boven/onder
pwm.set_PWM_frequency( linksrPIN, 50 ) # links/rechts
pwm.set_PWM_frequency( vooraPIN, 50 ) # voor/achter

pwm.set_servo_pulsewidth( grijperPIN, 500 ) ; # Zet grijper op positie 0 (dicht)
pwm.set_servo_pulsewidth( bovenoPIN, 500 ) ; # Zet boven/onder op positie 0 (helemaal boven)
pwm.set_servo_pulsewidth( linksrPIN, 500 ) ; # Zet links/rechts op positie 0 (helemaal links)
pwm.set_servo_pulsewidth( vooraPIN, 500 ) ; # Zet voor/achter op positie 0 (helemaal vooruit)

# In volgende variabelen worden de posities van elke servo bijgehouden
# Deze positionering zit logisch in elkaar: 500 is helemaal links, 1500 is het midden en 2500 is rechts 
grijper = 500
bovenonder = 500
linksrechts = 500
voorachter = 500

try: # Probeer
    while True: # Luister vanaf nu naar keyboard voor beweging
        pwm.set_servo_pulsewidth( grijperPIN, grijper ) ; # Zet grijper op inhoud van variabele "grijper"
        pwm.set_servo_pulsewidth( bovenoPIN, bovenonder ) ; # Zet boven/onder op op inhoud van variabele
        pwm.set_servo_pulsewidth( linksrPIN, linksrechts ) ; # Zet links/rechts op inhoud van variabele
        pwm.set_servo_pulsewidth( vooraPIN, voorachter ) ; # Zet voor/achter op inhoud van variabele

        char = getch() # Met deze functie kijken we welke toets ingedrukt is

        if (char == "a"): # Als "A" ingedrukt is
            if (linksrechts < 2500): # En wanneer links/rechts lager is dan 2500 (het maximum)
                linksrechts += 500 # Tel 500 op bij de vorige waarde van links/rechts (1 stap)
                pwm.set_servo_pulsewidth( linksrPIN, linksrechts ) ; # Zet linksrechts op de nieuwe inhoud (+ 1 stap) en beweeg de arm hier naartoe

        if (char == "d"): # Als "d" ingedrukt is
            if (linksrechts > 500): # En wanneer links/rechts hoger is dan 500 (het minimum)
                linksrechts -= 500 # trek 500 af van de vorige waarde van links/rechts (1 stap)
                pwm.set_servo_pulsewidth( linksrPIN, linksrechts ) ; # Zet linksrechts op de nieuwe inhoud (- 1 stap) en beweeg de arm hier naartoe

        if (char == "q"):
            if (grijper < 2500):
                grijper += 500
                pwm.set_servo_pulsewidth( grijperPIN, grijper ) ; # Zet grijper op inhoud van variabele "grijper"

        if (char == "e"):
            if (grijper > 500):
                grijper -= 500
                pwm.set_servo_pulsewidth( grijperPIN, grijper ) ; # Zet grijper op inhoud van variabele "grijper"

        if (char == "w"):
            if (voorachter < 2500):
                voorachter += 500
                pwm.set_servo_pulsewidth( vooraPIN, voorachter ) ; # Zet vooraachter op inhoud van variabele "voorachter"

        if (char == "s"):
            if (voorachter > 500):
                voorachter -= 500
                pwm.set_servo_pulsewidth( vooraPIN, voorachter ) ; # Zet voorachter op inhoud van variabele "voorachter"

        if (char == "r"):
            if (bovenonder < 2500):
                bovenonder += 500
                pwm.set_servo_pulsewidth( bovenoPIN, bovenonder ) ; # Zet bovenonder op inhoud van variabele "bovenonder"

        if (char == "f"):
            if (bovenonder > 500):
                bovenonder -= 500
                pwm.set_servo_pulsewidth( bovenoPIN, bovenonder ) ; # Zet bovenonder op inhoud van variabele "bovenonder"

        else:
            if (char == "p"):
                GPIO.cleanup() # Schakel alle GPIO pins uit
                exit() # stop het script

except KeyboardInterrupt: # Bij het stoppen van het script (met CTRL+C)
    GPIO.cleanup() # Herstel GPIO's naar standaardwaarden
