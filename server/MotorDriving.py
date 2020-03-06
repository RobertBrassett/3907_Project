from time import sleep
import RPi.GPIO as gpio
#import smbus2

#left motor
motor_left1 = 3 #pin 2 on L293D
motor_left2 = 5 #pin 7 on L293D
#right motor
motor_right1 = 7 #pin 10 on L293D
motor_right2 = 8 #pin 15 on L293D

#pwm_pinL = 10 #pin 16 L293D
#pwm_pinR = 11 #pin 1 L293D

#ultrasonic_trig = 23
#ultrasonic_echo = 24
#data_bus = smbus2.SMBus(1)

class Movement:
    def __init__(self):
        #initialize pins
        gpio.setmode(gpio.BOARD)
        gpio.setup(motor_left1, gpio.OUT)
        gpio.setup(motor_left2, gpio.OUT)
        gpio.setup(motor_right1, gpio.OUT)
        gpio.setup(motor_right2, gpio.OUT)
        
        #pwm pins
        #gpio.setup(pwm_pinL, gpio.OUT)
        #gpio.setup(pwm_pinR, gpio.OUT)
        #pwmL = gpio.PWM(pwm_pinL, 100)
        #pwmR = gpio.PWM(pwm_pinR, 100)
        #pwmL.start(0)
        #pwmR.start(0)

    def set_motors(self, left1, left2, right1, right2):
        #set left motor rotation
        gpio.output(motor_left1, left1)
        gpio.output(motor_left2, left2)
        #set right motor rotation
        gpio.output(motor_right1, right1)
        gpio.output(motor_right1, right2)

    def stop(self):
        self.set_motors(1,1,1,1)
        sleep(1)

    def go_fwd(self,secs):
        if secs == 0:
            self.set_motors(0,1,0,1)
        else:
            self.set_motors(0,1,0,1)
            sleep(secs)

    def go_bwd(self,secs):
        if secs == 0:
            self.set_motors(1,0,1,0)
        else:
            self.set_motors(1,0,1,0)
            sleep(secs)

    def go_l(self,secs):
        if secs == 0:
            self.set_motors(1,1,0,1)
        else:
            self.set_motors(1,1,0,1)
            sleep(secs)

    def go_r(self,secs):
        if secs == 0:
            self.set_motors(0,1,1,1)
        else:
            self.set_motors(0,1,1,1)
            sleep(secs)

#     def __get_distance(self):
#         gpio.setmode(gpio.BCM)
#         gpio.setup(ultrasonic_trig, gpio.OUT)
#         gpio.setup(ultrasonic_echo, gpio.IN)
#         gpio.output(ultrasonic_trig, False)
#         while gpio.input(ultrasonic_echo == 0):
#             start_time = time.time()
#         while gpio.input(ultrasonic_echo == 1):
#             stop_time = time.time()
#         t = stop_time - start_time
#         distance = (34300 * t)/2
#         gpio.cleanup()
#         return distance