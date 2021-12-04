/*
  Blink
Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led1 = 5;
int led2 = 6;
int led3 = 7;

// the setup routine runs once when you press reset:
void setup() {                
  // inwitialize the digital pin as an output.
   pinMode(led1, OUTPUT);
   pinMode(led2, OUTPUT);
   pinMode(led3, OUTPUT);     
   
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led1, HIGH);
  delay(200);
  digitalWrite(led2, HIGH);
  delay(200);
  digitalWrite(led3, HIGH);
  delay(200);

  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  delay(500);
  
  digitalWrite(led1, HIGH);
  delay(1);
  digitalWrite(led2, HIGH);
    delay(1);
  digitalWrite(led3, HIGH);
  delay(1);
  
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  delay(500)
    
  
 
}
