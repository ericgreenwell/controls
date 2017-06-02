#!usr/bin/env python

from flask import Flask, render_template, Response,flash,request, redirect, url_for, make_response
import motors
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #set up GPIO
GPIO.setwarnings(False)

# Raspberry pi camera module (reqires picamera package)
from camera_pi import Camera

app = Flask(__name__) #set up flask server
app.secret_key=os.urandom(24)

motor_object = motors.Pi() #create motor object


############# routes ############
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/video_feed')
def video_feed():
        return Response(gen(Camera()),
                        mimetype = 'multipart/x-mixed-replace; boundary=frame')

#recieve which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/move/<direction>', methods =['POST'])
def reroute(direction):
	      
        move = int(direction)
        if move == 1:
                motor_object.tiltUP(1)
        else:
                print "you've accomplished nothing"
        
	response = make_response(redirect(url_for('index')))
	return(response)

############# utils ###########
def gen(camera):
        """video streaming function"""
        while True:
                frame = camera.get_frame()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
############# main ############
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True) #set up the server in debug mode to the port 5000

############# EOF ##############
