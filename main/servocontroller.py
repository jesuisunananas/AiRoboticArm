import serial

def write_angle(ser : serial.Serial, angle : int, motor : int):
    ser.write(bytes([255]))    
    ser.write(bytes([motor])) 
    ser.write(bytes([angle]))  

def main():
    ser = serial.Serial('COM4', 9600, timeout=.1)
    while True:
        data = int(input("angle: "))
        ser.write(bytes[data])
        
if __name__ == "__main__":
    main()
