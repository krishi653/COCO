from gpiozero import Servo
from time import sleep

servo = Servo(21)

try:
	while True:
		servo.min()
		sleep(0.5)
		servo.mid()
		sleep(0.5)
		servo.max()
		sleep(0.5)
except KeyboardInterrupt:
	print("Program stopped")
