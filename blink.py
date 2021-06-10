# Blink an onboard led

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("USR1", GPIO.OUT)

while True:
  GPIO.output("USR1", GPIO.HIGH)
  time.sleep(1)
  GPIO.output("USR1", GPIO.LOW)
  time.sleep(1)
