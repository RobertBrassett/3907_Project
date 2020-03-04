import MotorDriving

def main():
    motors = MotorDriving.movment()
    motors.go_fwd(motors, 3)

if __name__ == '__main__':
    main()