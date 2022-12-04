#include <Servo.h>
Servo servo9;
Servo servo10;
Servo servo11;

int minPulseWidth = 600;
int maxPulseWidth = 2400; 

int userInput[3];
int angle;
int servo;
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
  if (Serial.available() > 2) {
      startbyte = Serial.read();

      if (startbyte == 255) {
        for (int i = 0; i < 2; i++) {
          userInput[i] = Serial.read();
        }

        servo = userInput[0];
        angle = userInput[1]; 

        switch (servo) {
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
    }
}
