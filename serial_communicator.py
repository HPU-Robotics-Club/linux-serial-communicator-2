import string
import serial
from enum import Enum

PORT = '/dev/ttyACM0' 
DIVIDER = "|"
BAUDRATE = 115200

class SerialCommunicator:
    def __init__(self):
        # self.arduino = serial.Serial(PORT, BAUDRATE)
        print("Starting serial communicator...")

        self.prev_left_speed = 0
        self.prev_right_speed = 0
        self.prev_belt_speed = 0
        self.prev_act_speed = 0

    def write(self, msg: str):
        code = f'{msg}{DIVIDER}'
        # self.arduino.write(code.encode())
        print(f'{code}')
    
    def write_motor_command(self, left_motor_code: str, right_motor_code: str, belt_motor_code: str, act_motor_code: str, left_motor_value: int, right_motor_value: int, belt_motor_value: int, act_motor_value: int):
        # This if statement makes it so that it won't send duplicate motor commands right after each other
        if (left_motor_value != self.prev_left_speed or right_motor_value != self.prev_right_speed or belt_motor_value != self.prev_belt_speed or act_motor_value != self.prev_act_speed):
            self.write(f'{left_motor_code}{self.format_motor_value(left_motor_value)}{right_motor_code}{self.format_motor_value(right_motor_value)}{belt_motor_code}{self.format_motor_value(belt_motor_value)}{act_motor_code}{self.format_motor_value(act_motor_value)}')
            
            # Assigns current motor values to the previous motor value variables
            self.prev_left_speed = left_motor_value
            self.prev_right_speed = right_motor_value
            self.prev_belt_speed = belt_motor_value
            self.prev_act_speed = act_motor_value

    def format_motor_value(self, motor_value: int):
        N = 0
        if motor_value < 10:
            N = 2
        elif motor_value < 100:
            N = 1
        
        output_str = str(motor_value)
        for i in range(0, N):
            output_str = f'0{output_str}'

        return output_str

#make sure that there is an "rf" then there will be an "f" or "b" for front or back then the following three charcters will be an number between  -255 to 255(6 charcters in each of the motor codes)
#have unassigned values
class MotorCode():
    RIGHT_FRONT_WHEEL = "rf"
    RIGHT_BACK_WHEEL = "rb"
    LEFT_FRONT_WHEEL = "lf"
    LEFT_BACK_WHEEL = "lb"