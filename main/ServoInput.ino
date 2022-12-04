#include <Servo.h>
Servo myservo; 
int pos;
int userInput;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  myservo.write(0);
}

void loop()
{ 
  if (Serial.available()){
    userInput = Serial.read();
    myservo.write(userInput);
  }
}
