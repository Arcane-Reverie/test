#include <Servo.h>

Servo topServo;

const int switchPin = 2;         // Switch or button to trigger system
const int servoPin = 9;          // Servo signal pin
const int dripRelay = 3;         // Relay to control drip irrigation
const int sprayRelay = 4;        // Relay to control sprinkler

bool activated = false;

void setup() {
  pinMode(switchPin, INPUT_PULLUP); // Use internal pull-up resistor
  pinMode(dripRelay, OUTPUT);
  pinMode(sprayRelay, OUTPUT);

  digitalWrite(dripRelay, LOW);    // Off initially
  digitalWrite(sprayRelay, LOW);   // Off initially

  topServo.attach(servoPin);       // Attach servo
  topServo.write(0);               // Start with top closed

  Serial.begin(9600);
}

void loop() {
  int switchState = digitalRead(switchPin);
  Serial.println(switchState);

  if (switchState == LOW && !activated) { // Switch is pressed
    openTop();
    startIrrigation();
    activated = true;
    delay(1000); // Debounce delay
  }

  // Optional: close top after 10 seconds of irrigation - uncomment if desired
  // delay(10000);
  // closeTop();
}

void openTop() {
  topServo.write(90);   // Open the top
  delay(1000);
}

void closeTop() {
  topServo.write(0);    // Close the top
  delay(1000);
}

void startIrrigation() {
  digitalWrite(dripRelay, HIGH);    // Turn ON drip irrigation
  digitalWrite(sprayRelay, HIGH);   // Turn ON sprinkler
  delay(5000);                       // Run both for 5 seconds
  digitalWrite(dripRelay, LOW);     // Turn OFF drip
  digitalWrite(sprayRelay, LOW);    // Turn OFF sprinkler
  closeTop();                        // Close the top after irrigation
  activated = false;                 // Reset activated state
}