import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
waitTime = .001
step = 25
direction = 23



               
GPIO.setup(direction, GPIO.OUT)
GPIO.setup(step, GPIO.OUT)
GPIO.output(direction, True)
GPIO.setup(21, GPIO.IN)

home = GPIO.input(21)


stepCounter = 0

while home == 0:
        #turning on and off forces one step
        print home
        GPIO.output(step, True)
        GPIO.output(step, False)
        sleep(waitTime)
        home = GPIO.input(21)
