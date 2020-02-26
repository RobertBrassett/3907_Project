import time
import smbus2
import RPi.GPIO as gpio


motor_run_left = 17
motor_run_right = 18
motor_dir_left = 4
motor_dir_right = 25
ultrasonic_trig = 23
ultrasonic_echo = 24
data_bus = smbus2.SMBus(1)


class Dropbot:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(motor_run_left, gpio.OUT)
        gpio.setup(motor_run_right, gpio.OUT)
        gpio.setup(motor_dir_left, gpio.OUT)
        gpio.setup(motor_dir_right, gpio.OUT)

    def set_motors(self, run_left, dir_left, run_right, dir_right):
        gpio.output(motor_run_left, run_left)
        gpio.output(motor_dir_left, dir_left)
        gpio.output(motor_run_right, run_right)
        gpio.output(motor_dir_right, dir_right)


    def go_forward(self,secs):
        if secs == 0:
            self.set_motors(1, 1, 1, 1)
        else:
            self.set_motors(1, 1, 1, 1)
            time.sleep(secs)
            gpio.cleanup()

    def go_backward(self,secs):
        if secs == 0:
            self.set_motors(1, 0, 1, 0)
        else:
            self.set_motors(1, 0, 1, 0)
            time.sleep(secs)
            gpio.cleanup()

    def go_left(self,secs):
        if secs == 0:
            self.set_motors(0, 0, 1, 1)
        else:
            self.set_motors(0, 0, 1, 1)
            time.sleep(secs)
            gpio.cleanup()

    def go_right(self,secs):
        if secs == 0:
            self.set_motors(1, 1, 0, 0)
        else:
            self.set_motors(1, 1, 0, 0)
            time.sleep(secs)
            gpio.cleanup()

    def __get_distance(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(ultrasonic_trig, gpio.OUT)
        gpio.setup(ultrasonic_echo, gpio.IN)
        gpio.output(ultrasonic_trig, False)
        while gpio.input(ultrasonic_echo == 0):
            start_time = time.time()
        while gpio.input(ultrasonic_echo == 1):
            stop_time = time.time()
        t = stop_time - start_time
        distance = (34300 * t)/2
        gpio.cleanup()
        return distance

