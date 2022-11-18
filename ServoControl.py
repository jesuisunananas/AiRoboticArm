import serial

while True:
    with serial.Serial('COM4', 9600, timeout=.1) as ser:
        command = bytes(input("angle?"), 'utf-8')
        ser.write(command)
        message = ser.read(10)
        print(message)
