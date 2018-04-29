import RPi.GPIO as GPIO
import time
import requests
from datetime import datetime


GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
ALERT = 17
start = datetime.now()
print "calibration in progress"


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ALERT,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def settle(settleTime):
    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(settleTime)

def formatDateAndTime(aDateAndTime):

    format = '%Y-%m-%d_%H:%M:%S'

    return (aDateAndTime.strftime(format))


def ping(shouldSettle):
    
    #print "Sending Trig signal"
    GPIO.output(TRIG, True)

    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = 0
    pulse_end = 0
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    #print "Received Echo signal"

    pulse_duration = pulse_end - pulse_start

    #print "Pulse Duration: ", pulse_duration

    distance = pulse_duration * 34300

    distance = distance / 2

    distance = round(distance, 2)

    if shouldSettle > 0 :
        settle(shouldSettle)

    return distance


calibrationDistance = (ping(1) + ping(1) + ping(1))

#toggle = False
#for i in range(10):
#    toggle = not toggle
#    GPIO.output(ALERT, toggle)
#    time.sleep(500.0/1000)

#GPIO.output(ALERT, False)



calibrationDistance = calibrationDistance / 3
print "Calibration Distance: ",calibrationDistance,"cm"

tolerance = .10
print "Acceptable tolerance: ",tolerance
threshold = calibrationDistance * tolerance
print "Threshold: ", threshold

print "Calibration Complete, taking measurements"

measurements = []



for i in range(10):
    current = ping(0)
    diff = calibrationDistance - current
    print "Current Distance: ", current," Diff: ",diff

    #if abs(diff) > threshold:
    #    print "ALERT ALERT ALERT"
    #    GPIO.output(ALERT, True)
    #    time.sleep(1)
    #    GPIO.output(ALERT, False)

    now = datetime.now()

    measurements.append({"timeStamp":formatDateAndTime(now), "measurement": current})

    time.sleep(1)	

stop = datetime.now()



print "Measurements complete"


content = {"start":formatDateAndTime(start),"stop":formatDateAndTime(stop),"items":measurements}


api_token = 'your_api_token'
api_url_base = 'http://eskimo:8080/sensor/'

headers = {'Content-Type': 'application/json'}
response = requests.post(api_url_base, headers=headers, json=content)

GPIO.cleanup()