import RPi.GPIO as GPIO

__author__ = 'Dani'

def setup(ports):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for row in ports:
        for port in row:
            GPIO.setup(port, GPIO.OUT)
    

def output(port, value):
    GPIO.output(port, value)
