
import sys
import warnings
import time
from threading import Timer
import RPi.GPIO as GPIO

MOTO_PIN_1 = 11
MOTO_PIN_2 = 13
MOTO_PIN_3 = 15
MOTO_PIN_4 = 16

def init():
	GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MOTO_PIN_1, GPIO.OUT)
        GPIO.setup(MOTO_PIN_2, GPIO.OUT)
        GPIO.setup(MOTO_PIN_3, GPIO.OUT)
        GPIO.setup(MOTO_PIN_4, GPIO.OUT)


def deinit():
	GPIO.cleanup()

def _left_forward():
	GPIO.output(MOTO_PIN_1, GPIO.LOW)
	GPIO.output(MOTO_PIN_2, GPIO.HIGH)

def _left_stop():
	GPIO.output(MOTO_PIN_1, GPIO.LOW)
	GPIO.output(MOTO_PIN_2, GPIO.LOW)

def _left_backward():
	GPIO.output(MOTO_PIN_1, GPIO.HIGH)
	GPIO.output(MOTO_PIN_2, GPIO.LOW)


def _right_forward():
	GPIO.output(MOTO_PIN_3, GPIO.LOW)
	GPIO.output(MOTO_PIN_4, GPIO.HIGH)

def _right_stop():
	GPIO.output(MOTO_PIN_3, GPIO.LOW)
	GPIO.output(MOTO_PIN_4, GPIO.LOW)

def _right_backward():
	GPIO.output(MOTO_PIN_3, GPIO.HIGH)
	GPIO.output(MOTO_PIN_4, GPIO.LOW)

def forward(step):
	print "move forward"
	init()
	_left_forward()
	_right_forward()
	time.sleep(step)
	deinit()

def backward(step):
	print "move backward"
	init()
	_left_backward()
	_right_backward()
	time.sleep(step)
	deinit()

def pivot_left(step):
	print "turn left"
	init()
	_left_backward()
	_right_forward()
	time.sleep(step)
	deinit()

def pivot_right(step):
	print "turn right"
	init()
	_left_forward()
	_right_backward()
	time.sleep(step)
	deinit()

def turn_left(step):
	print "turn left"
	init()
	_left_stop()
	_right_forward()
	time.sleep(step)
	deinit()

def turn_right(step):
	print "turn right"
	init()
	_left_forward()
	_right_stop()
	time.sleep(step)
	deinit()

def key_input(event):
	print 'key_input:', event.char
	key_press = event.char
	sleep_time = 0.030
	if key_press.lower() == 'w':
		forward(sleep_time)
	elif key_press.lower() == 's':
		backward(sleep_time)
	elif key_press.lower() == 'a':
		turn_left(sleep_time)
	elif key_press.lower() == 'd':
		turn_right(sleep_time)

def main_loop():
	while True:
		key_press = raw_input()
		print("input: ", key_press)
		sleep_time = 0.150
		if key_press.lower() == 'w':
			forward(sleep_time)
		elif key_press.lower() == 's':
			backward(sleep_time)
		elif key_press.lower() == 'a':
			turn_left(sleep_time)
		elif key_press.lower() == 'd':
			turn_right(sleep_time)
		elif key_press.lower() == 'q':
			pivot_left(sleep_time)
		elif key_press.lower() == 'e':
			pivot_right(sleep_time)
		elif key_press.lower() == "z":
			break
		else:
			pass
def auto_run():
	while True:
		sleep_time = 0.450
		backward(sleep_time)
		forward(sleep_time)
	#turn_left(sleep_time)
	#turn_right(sleep_time)
	#pivot_left(sleep_time)
	#pivot_right(sleep_time)

#auto_run()
main_loop()
