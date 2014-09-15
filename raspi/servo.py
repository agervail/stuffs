__author__ = 'agervail'

from RPIO import PWM
import time

def set_servo_angle(servo, pin, angle):
  angle = max(min(180, angle), 0)
  t = round(angle * (200.0 / 180.0) + 50) * 10
  servo.set_servo(pin, t)

servo = PWM.Servo()

i = 0
coef = 1

while True:
  set_servo_angle(servo, 4, i)
  #print i
  i += 10 * coef
  if i >= 180 or i <= 0:
    coef *= -1
  time.sleep(0.5)
