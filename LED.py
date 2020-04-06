from time import sleep
import RPi.GPIO as GPIO

"""
Make white led switch on till program executes and blink RGB Led continuously with interval of 1s.

Structure:

* Assign each led a pin number
* assign each led their corresponding GPIO by set mode, and setouput

* Clear the GPIO using GPIO.cleanup()

blink using PWM of GPIO https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/ but only useful only if same led to be used
"""


# Setting the GPIO pin number to their corresponding LED as global variable
red = 11
green = 13
blue = 15
white = 16

pins_list = (red, green, blue, white)

#Since GPIO pins are numbered using 2 conventions, BOARD and BCM, setting mode to BOARD convention to read the GPIO pins (set it as global)
GPIO.setmode(GPIO.BOARD)


def setup():
	"""
	to setup all the pins for blink to work properly
	"""
	try:
		print("Setting pins...")
		# Setting all led pins at once using tuples in more than one channel
		GPIO.setup(pins_list, GPIO.OUT)
	except KeyboardInterrupt:
		GPIO.output(pins_list, GPIO.LOW)
		GPIO.cleanup()

def blink(color, n):
	"""
	blink function to blink RGB LED with color "color" 'n' times.
	Call using blink(color_name)
	"""

	# If color is red, set pin to red_pin and so on
	# Will save the value present in the variable of color's value. i.e. if color = "red", and red = 2, then pin equals 2.
	#color_pin = vars()[color + "Pin"]		
	if color == "red":
		color_pin = red
	elif color == "green":
		color_pin = green
	elif color == "blue":
		color_pin = blue
	print(color_pin)

	try:
		# setting up the color pin for output
		GPIO.setup(color_pin, GPIO.OUT)

		for times in range(0, n):
			# Switching ON the LED, Setting this color pin to be HIGH i.e. passing 3.3V to turn on the LED
			# Wait for 0.2 seconds as delay
			# Switch off the led
			# Wait for 1s interval
			GPIO.output(color_pin, GPIO.HIGH)
			delay = 0.2	
			sleep(delay)
			GPIO.output(color_pin, GPIO.LOW)
			sleep(1)

		# Clearing GPIO block
		#print("Clearing...")
		GPIO.cleanup(color_pin)

	except KeyboardInterrupt:
		GPIO.output(color_pin, GPIO.LOW)
		GPIO.cleanup(color_pin)

def white_led(status):
	"""
	To switch ON and OFF the white LED depending on the status.
	If status == ON, switch on the LED until white_led(OFF) is not called.
	Or the program execution terminates.
	"""
	try:
		if status == "ON":
			# Switch on the led
			GPIO.setup(white, GPIO.OUT)
			GPIO.output(white, GPIO.HIGH)
		elif status == "OFF":
			# Switch off the led
			GPIO.output(white, GPIO.LOW)
			GPIO.cleanup(white)
	except KeyboardInterrupt:
		GPIO.output(white, GPIO.LOW)
		GPIO.cleanup(white)

if __name__=="__main__":
	"""
	Add the blink call in try, except and finally block
	"""
	try:
		white_led("ON")

		blink("blue", 5)

		white_led("OFF")

	except KeyboardInterrupt:
		GPIO.output(pins_list, GPIO.LOW)
		GPIO.cleanup()
