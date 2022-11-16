import serial
import time

while True:
    with serial.Serial('COM4', 9600, timeout=.1) as ser:
        command = chr(int(input("angle?")))
        ser.write(command) 
        ser.read(command)        
