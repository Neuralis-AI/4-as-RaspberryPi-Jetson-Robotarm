import RPi.GPIO as GPIO # Importeer het GPIO-aansturingspakket
import time # Importeer tijdpakket voor de wachttijden

grijperPIN = 17 #Board pin 11, BCM pin 17
bovenoPIN = 27 #Board pin 13, BCM pin 27
linksrPIN = 22 #Board pin 15, BCM pin 22
vooraPIN = 23 #Board pin 16, BCM pin 23

GPIO.setmode(GPIO.BCM) # zet aansturing volgens BCM pins
GPIO.setup(grijperPIN, GPIO.OUT) # schakel GPIO pin op output (standaard input)
GPIO.setup(bovenoPIN, GPIO.OUT)
GPIO.setup(linksrPIN, GPIO.OUT)
GPIO.setup(vooraPIN, GPIO.OUT)                                                                                                                                                                                                                  p = GPIO.PWM(grijperPIN, 50) #grijper
p2 = GPIO.PWM(bovenoPIN, 50) # boven/onder
p3 = GPIO.PWM(linksrPIN, 50) # links/rechts
p4 = GPIO.PWM(vooraPIN, 50) # voor/achter

p.start(5) # Startpositie grijper
p2.start(5) # Startpositie boven/onder
p3.start(5) # Startpositie links/rechts
p4.start(5) # Startpositie voor/achter

try: # Probeer
  while True: # Start script
    p.ChangeDutyCycle(5) # Zet grijper op positie 5 (dicht)
    p2.ChangeDutyCycle(5) # Zet boven/onder op positie 5
    p3.ChangeDutyCycle(5) # Zet links/rechts op positie 5
    p4.ChangeDutyCycle(5) # Zet voor/achter op positie 5
    time.sleep(2) # Wacht 2 seconden
    p2.ChangeDutyCycle(7) #Zet boven/onder op positie 7
    p2.ChangeDutyCycle(7) # Zet boven/onder op positie 7
    p3.ChangeDutyCycle(7) # Zet links/rechts op positie 7
    p4.ChangeDutyCycle(7) # Zet voor/achter op positie 7
    time.sleep(2) # Wacht 2 seconden
    p2.ChangeDutyCycle(5) # Zet boven/onder op positie 5
    p2.ChangeDutyCycle(5) # Zet boven/onder op positie 5
    p3.ChangeDutyCycle(5) # Zet links/rechts op positie 5
    p4.ChangeDutyCycle(5) # Zet voor/achter op positie 5
    time.sleep(3) # Wacht 5 sec
except KeyboardInterrupt: # Bij het stoppen van het script (met CTRL+C)

  p.ChangeDutyCycle(5) # Reset grijper naar startpositie
  p2.ChangeDutyCycle(5) # Reset boven/onder naar startpositie
  p3.ChangeDutyCycle(5) # Reset links/rechts naar startpositie
  p4.ChangeDutyCycle(5) # Reset voor/achter naar startpositie

  time.sleep(1) # Wacht 1 seconde tot alles gereset is

  p.stop() # Stop aansturing van grijper
  p2.stop() # Stop aansturing van boven/onder
  p3.stop() # Stop aansturing van links/rechts
  p4.stop() # Stop aansturing van voor/achter

  GPIO.cleanup() # Herstel GPIO's naar standaardwaarden                                                                                                                                                                                                                               
