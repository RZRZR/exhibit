#include <Adafruit_DotStar.h>
#include <SPI.h>
#define DATAPIN    4
#define CLOCKPIN   5
#define NUMPIXELS 101
int score = 1;

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

  if (Serial.available() >= 3) {
    digit1 = Serial.read() - 48;
    digit2 = Serial.read() - 48;
    digit3 = Serial.read() - 48;
  
    score =  (digit1 * 100) + (digit2 * 10) + digit3

  for(byte x=0;x<101;x++){ 
    strip.setBrightness(100);
    strip.setPixelColor(x, 0, 255, 0); 
    strip.show();
    }
   for(byte x=0;x<score;x++){     
      strip.setPixelColor(x, 255, 0, 0);   
      strip.show();
      }
      delay(10);
    }
}



