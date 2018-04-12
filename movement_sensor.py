import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
ALERT = 17

print "calibration in progress"


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ALERT,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def settle():
	GPIO.output(TRIG, False)
	print "Waiting For Sensor To Settle"
	time.sleep(2)


def ping(shouldSettle):
	#print "Sending Trig signal"
	GPIO.output(TRIG, True)

	time.sleep(0.00001)
	GPIO.output(TRIG, False)

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
		settle()	
	
	return distance


calibrationDistance = (ping(1) + ping(1) + ping(1))
GPIO.output(ALERT, True)
time.sleep(1)
GPIO.output(ALERT, False)
time.sleep(1)
GPIO.output(ALERT, True)
time.sleep(1)
GPIO.output(ALERT, False)

calibrationDistance = calibrationDistance / 3
print "Calibration Distance: ",calibrationDistance,"cm"

tolerance = .10
print "Acceptable tolerance: ",tolerance
threshold = calibrationDistance * tolerance
print "Threshold: ", threshold

for i in range(100):
	current = ping(0)
	diff = calibrationDistance - current
	#print "Current Distance: ", current," Diff: ",diff
	 
	if abs(diff) > threshold:
		print "ALERT ALERT ALERT"
		GPIO.output(ALERT, True)
		time.sleep(1)
		GPIO.output(ALERT, False)	
	
	time.sleep(250.0/1000)




GPIO.cleanup()
