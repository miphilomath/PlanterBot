from time import sleep
import RPi.GPIO as GPIO

"""
Make white led switch on till program executes and blink RGB led continuously with interval of 1s.
"""

# Using PWM to blink RGB LED Update: No use, useful only if same led to be used
# Pins assignment
red = 11
green = 13
blue = 15
white = 16

pins_list = (red, green, blue, white)

try:
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pins_list, GPIO.OUT)
	
	# Switching white led on
	GPIO.output(white, GPIO.HIGH)
	
	for times in range (0, 10):
		# Blink RGB led with interval of 1second
		GPIO.output(red, GPIO.HIGH)
		sleep(0.2)
		GPIO.output(red, GPIO.LOW)
		sleep(1)
	
		GPIO.output(green, GPIO.HIGH)
		sleep(0.2)
		GPIO.output(green, GPIO.LOW)
		sleep(1)
	
		GPIO.output(blue, GPIO.HIGH)
		sleep(0.2)
		GPIO.output(blue, GPIO.LOW)
		sleep(1)
	
	GPIO.cleanup((red, green, blue))
	# Switching White led off
	GPIO.output(white, GPIO.LOW)
	
	# Cleaning white led channel
	GPIO.cleanup(white)
except KeyboardInterrupt:
	GPIO.output(pins_list, GPIO.LOW)
#finally:
	GPIO.cleanup()

