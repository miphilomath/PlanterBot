# To test the motor and its motion
"""
Module to control motors for motion using GPIO configuration.
Speed changes with duty cycle.

Todo:
* Assign Motor connections to their corresponding pins
* Make a pin tuples used by motor to setup a channel, and contorl the motors.
* Make forward, reverse function
* Make right/left function as right(Angle)
"""
import RPi.GPIO as GPIO
from time import sleep

# Pins assignment, 1E and 2E being enable for the motor
# Power (+5V) on Pin 2
# Right Wheel
Motor1E = 33
Motor1A = 35
Motor1B = 37

# Left Wheel
Motor2A = 36
Motor2B = 38
Motor2E = 40

# Motor list as a tuple
motors_list = (Motor1E, Motor1A, Motor1B, Motor2E, Motor2A, Motor2B)

try:
	# GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	# Setting GPIO channels as output.
	GPIO.setup(motors_list, GPIO.OUT)
	
	left_pwm = GPIO.PWM(Motor2E, 100)
	right_pwm = GPIO.PWM(Motor1E, 100)
	left_pwm.start(25)
	right_pwm.start(25)
	 
	print "Turning motor on"
	# Left Motor
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	left_pwm.ChangeDutyCycle(30)

	# Right wheel
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	right_pwm.ChangeDutyCycle(30)
	
	sleep(5)
	
	left_pwm.stop()
	right_pwm.stop()
	print "Stopping motor"
	GPIO.output(Motor2E,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.LOW)

	GPIO.cleanup()
except KeyboardInterrupt:
	GPIO.output(motors_list, GPIO.LOW)
	GPIO.cleanup()

#-----------------------------------------------------------------------------
	
def right(speed):
	"""
	Moves the right wheel with specified speed as its duty cycle.
	"""

def left(speed):
	"""
	Moves the left wheel with specified speed as its duty cycle.
	"""

def forward(speed):
	"""
	Forward moves the bot with specified speed as duty cycle.
	Move both the wheels at same speed.
	"""

def reverse(speed):
	""" 
	Reverse the Bot with specified speed as duty cycle.
	"""

def rotate(angle):
	"""
	Rotate the bot in static position with specified angle.
	Speed of both right and left wheel will be different.
	
	Update: Rotate the bot while moving, and slowly turning before the turn.
	rotate(speed, angle)
	"""

