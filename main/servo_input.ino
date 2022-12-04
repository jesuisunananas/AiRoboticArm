#include <Servo.h>
Servo servo9;
Servo servo10;
Servo servo11;

int minPulseWidth = 600;
int maxPulseWidth = 2400; 

int pythonData[3];
int angle;
int motor;
int startbyte;

void setup() {
  Serial.begin(9600);
  servo9.attach(9, minPulse, maxPulse);
  servo10.attach(10, minPulse, maxPulse);
  servo11.attach(11, minPulse, maxPulse);
  
  servo9.write(0);
  servo10.write(0);
  servo11.write(0);
}

void loop() {
    if (Serial.available() < 2) {
        return;
    }
    startbyte = Serial.read();
    if (startbyte != 255) {
        return;
    }

    for (int i = 0; i < 2; i++) {
    	pythonData[i] = Serial.read();
    }

    motor = pythonData[0];
    angle = pythonData[1]; 

    switch (motor) {
      case 9:
        servo9.write(angle);
        break;
      case 10:
        servo10.write(angle);
        break;
      case 11:
        servo11.write(angle);
        break;
    }
}
