"""
Module to control motors for motion using GPIO configuration.

Todo:
* Assign Motor connections to their corresponding pins
* Make a pin tuples used by motor to setup a channel, and contorl the motors.


"""
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Pins assignment, 1E and 2E being enable for the motor
# Power (+5V) on Pin 2
Motor1E = 33
Motor1A = 35
Motor1B = 37

Motor2A = 36
Motor2B = 38
Motor2E = 40

# Motor list as a tuple
motors_list = (Motor1E, Motor1A, Motor1B, Motor2E, Motor2A, Motor2B)

# Setting GPIO channels as output.
GPIO.setup(motors_list, GPIO.OUT)

left_pwm = GPIO.PWM(Motor1E, 100)
right_pwm = GPIO.PWM(Motor2E, 100)
left_pwm.start(25)
right_pwm.start(25)
 
print "Turning motor on"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
left_pwm.ChangeDutyCycle(100)
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
right_pwm.ChangeDutyCycle(100)
 
sleep(20)

left_pwm.stop()
right_pwm.stop()
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 
GPIO.cleanup()
