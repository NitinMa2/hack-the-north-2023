#include <Servo.h>
int pos = 0;
int counter = 0;
Servo servo_9;

unsigned long startMillis;  //some global variables available anywhere in the program
unsigned long currentMillis;
const unsigned long period = 10000;  //the value is a number of milliseconds  VARIABLE FROM PYTHON
//const byte ledPin = 13;    //using the built in LED

void setup()
{
  Serial.begin(115200);  //start Serial in case we need to print debugging info
  //pinMode(ledPin, OUTPUT);
  startMillis = millis();  //initial start time
  //define the pin where the servo signal is connected as the first variable
  servo_9.attach(9, 500, 2500);
}

void loop()
{
  currentMillis = millis();  //get the current "time" (actually the number of milliseconds since the program started)
  if (currentMillis - startMillis >= period)  //test whether the period has elapsed
  {
    // digitalWrite(ledPin, !digitalRead(ledPin));  //if so, change the state of the LED.  Uses a neat trick to change the state
    servo_9.detach();
    startMillis = currentMillis;  //IMPORTANT to save the start time of the current LED state.
  }
  // sweep the servo from 0 to 180 degrees in steps
  // of 1 degrees
  for (pos = 0; pos <= 180; pos += 20) {
    // tell servo to go to position in variable 'pos'
    servo_9.write(pos);
    // wait 15 ms for servo to reach the position
    delay(15); // Wait for 15 millisecond(s)
  }
  for (pos = 180; pos >= 180; pos -= 20) {
    // tell servo to go to position in variable 'pos'
    servo_9.write(pos);
    // wait 15 ms for servo to reach the position
    delay(15); // Wait for 15 millisecond(s)
  }
}