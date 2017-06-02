import RPi.GPIO as GPIO
from time import sleep
pin = 23
GPIO.cleanup()
GPIO.setwarnings(False)

class Pi(object):
	"""raspberry pi Internet stuff"""
	
	def __init__(self):
                GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin, GPIO.OUT)
		#initialize low
		GPIO.output(pin, GPIO.LOW)
	
#	def tiltUP(self,value) true or false to write to pin is the value
	def tiltUP(self, value):
    		print "going up!"
    		GPIO.output(pin, GPIO.HIGH)
    		sleep(1)
    		GPIO.output(pin, GPIO.LOW)
    		sleep(1)
    		GPIO.output(pin, GPIO.HIGH)

GPIO.cleanup()
