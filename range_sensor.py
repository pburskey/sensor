import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

print "Sending Trig signal"
GPIO.output(TRIG, True)

time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

print "Received Echo signal"
pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 34300

distance = distance / 2

distance = round(distance, 2)

print "Distance:",distance,"cm"

GPIO.cleanup()
