#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time

grijperPIN = 17 #Board pin 11, BCM pin 17
bovenoPIN = 27 #Board pin 13, BCM pin 27
linksrPIN = 22 #Board pin 15, BCM pin 22
vooraPIN = 23 #Board pin 16, BCM pin 23

pwm = pigpio.pi()
pwm.set_mode(grijperPIN, pigpio.OUTPUT) # schakel GPIO pin op output (standaard input)
pwm.set_mode(bovenoPIN, pigpio.OUTPUT)
pwm.set_mode(linksrPIN, pigpio.OUTPUT)
pwm.set_mode(vooraPIN, pigpio.OUTPUT)
                                                                                                                        
pwm.set_PWM_frequency( grijperPIN, 50 ) # grijper
pwm.set_PWM_frequency( bovenoPIN, 50 ) # boven/onder
pwm.set_PWM_frequency( linksrPIN, 50 ) # links/rechts
pwm.set_PWM_frequency( vooraPIN, 50 ) # voor/achter

print( "0 graden" )
pwm.set_servo_pulsewidth( grijperPIN, 500 ) ; # Zet grijper op positie 0 (dicht)
pwm.set_servo_pulsewidth( bovenoPIN, 500 ) ;
pwm.set_servo_pulsewidth( linksrPIN, 500 ) ;
pwm.set_servo_pulsewidth( vooraPIN, 500 ) ;
time.sleep( 3 )

print( "90 graden" )
pwm.set_servo_pulsewidth( grijperPIN, 1500 ) ; # Zet grijper op positie 1 (halfopen)
pwm.set_servo_pulsewidth( bovenoPIN, 1500 ) ;
pwm.set_servo_pulsewidth( linksrPIN, 1500 ) ;
pwm.set_servo_pulsewidth( vooraPIN, 1500 ) ;
time.sleep( 3 )

print( "180 graden" )
pwm.set_servo_pulsewidth( grijperPIN, 2500 ) ; # Zet grijper op positie 2 (open)
pwm.set_servo_pulsewidth( bovenoPIN, 2500 ) ;
pwm.set_servo_pulsewidth( linksrPIN, 2500 ) ;
pwm.set_servo_pulsewidth( vooraPIN, 2500 ) ;
time.sleep( 3 )

# servo's uitschakelen
pwm.set_PWM_dutycycle(grijperPIN, 0) # Reset grijper naar startpositie
pwm.set_PWM_dutycycle(bovenoPIN, 0) # Reset boven/onder naar startpositie
pwm.set_PWM_dutycycle(linksrPIN, 0) # Reset links/rechts naar startpositie
pwm.set_PWM_dutycycle(vooraPIN, 0) # Reset voor/achter naar startpositie

pwm.set_PWM_frequency( grijperPIN, 0 )
pwm.set_PWM_frequency( bovenoPIN, 0 )
pwm.set_PWM_frequency( linksrPIN, 0 )
pwm.set_PWM_frequency( vooraPIN, 0 )
