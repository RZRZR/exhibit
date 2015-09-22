int analog0 = 0;
int analog1 = 1;
int analog2 = 2;
int analog3 = 3;
int analog4 = 4;
int analog5 = 5;
int analog6 = 6;
int analog7 = 7;
int analog8 = 8;
int analog9 = 9;
int analog10 = 10;
int analog11 = 11;
int analog12 = 12;
int analog13 = 13;
int analog14 = 14;
int analog15 = 15;

int val0 = 0;
int val1 = 1;
int val2 = 2;
int val3 = 3;
int val4 = 4;
int val5 = 5;
int val6 = 6;
int val7 = 7;
int val8 = 8;
int val9 = 9;
int val10 = 10;
int val11 = 11;
int val12 = 12;
int val13 = 13;
int val14 = 14;
int val15 = 15;


int score = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.begin(9600);
if (Serial.available() > 0) {
  val0 = analogRead(analog0);
  val1 = analogRead(analog1);
  val2 = analogRead(analog2);
  val3 = analogRead(analog3);
  val4 = analogRead(analog4);
  val5 = analogRead(analog5);
  val6 = analogRead(analog6);
  val7 = analogRead(analog7);
  val8 = analogRead(analog8);
  val9 = analogRead(analog9);
  val10 = analogRead(analog10);
  val11 = analogRead(analog11);
  val12 = analogRead(analog12);
  val13 = analogRead(analog13);
  val14 = analogRead(analog14);
  val15 = analogRead(analog15);

  score = ((val0 + val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8 + val9 + val10 + val11 + val12 + val13 + val14 + val15) / 16 ) / 10.23;
  Serial.println(score);
  delay(10);
  Serial.end();
}

}


