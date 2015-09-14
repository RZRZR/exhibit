#include <Adafruit_DotStar.h>
#include <SPI.h>
#define DATAPIN    4
#define CLOCKPIN   5
#define NUMPIXELS 101
int score = 1;

int digit1 = 0;
int digit2 = 2;
int digit3 = 2;


Adafruit_DotStar strip = Adafruit_DotStar(NUMPIXELS, DATAPIN, CLOCKPIN);

void setup() {

// Open serial connection.
Serial.begin(9600);  
strip.begin(); // Initialize pins for output
strip.show();  // Turn all LEDs off ASAP
for(byte x=0;x<101;x++){ 
  strip.setBrightness(100);
  strip.setPixelColor(x, 0, 255, 0); 
  strip.show();
  }

}


void loop () {
  // wait for serial. When it has received 3 digits.. 
  if (Serial.available() >= 3) {
    digit1 = Serial.read() - 48; // convert first digit
    digit2 = Serial.read() - 48;
    digit3 = Serial.read() - 48;
  
    score =  (digit1 * 100) + (digit2 * 10) + digit3;  // put the digits back together again.
    Serial.print(score);
  
  // would be nice to have a screensaver pattern.
  

    for(byte x=0;x<101;x++){    // For all the pixels, turn them RED
      strip.setBrightness(100);
      strip.setPixelColor(x, 0, 255, 0); 
      strip.show();
    }
    for(byte x=0;x<score;x++){ // For the score-number turn them green    
      strip.setPixelColor(x, 255, 0, 0);   
      strip.show();
    }
    delay(10);
  }

}

