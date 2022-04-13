import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)

while True:
	entrada = GPIO.input(40)
	print(entrada)
	time.sleep(1)
