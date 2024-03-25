#include <Arduino.h>

// put function declarations here:
int myFunction(int, int);

void setup() {
  // Setup the controllers pin
  pinMode(2, OUTPUT);
  // init the serial communication
  Serial.begin(921600);
  Serial.println("Testing from setup");
  // put your setup code here, to run once:
  // int result = myFunction(2, 3);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  Serial.println("Testing from loop");
  digitalWrite(2, HIGH);
  delay(1000);
  digitalWrite(2, LOW);
}

// put function definitions here:
int myFunction(int x, int y) { return x + y; }