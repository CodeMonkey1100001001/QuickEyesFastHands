// QuickEyesFastHands.ino

int portList[]={6,9,10,11,A0,A1,A2,A3};
const int portCount=8;
const int buttonPin=5;
void setup() 
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  //pinMode(11,OUTPUT); digitalWrite(11,HIGH);

  for (int i=0; i < portCount; i++) 
  {
    pinMode(portList[i],OUTPUT);
    digitalWrite(portList[i],HIGH);
  }
  
}

void loop() 
{
  while(digitalRead(buttonPin) == HIGH)
  {
    delay(1);
  }


  for (int i=0; i < portCount; i++) 
  {
    int n = random(0, portCount);  // Integer from 0 to questionCount-1
    int temp = portList[n];
    portList[n] =  portList[i];
    portList[i] = temp;
  }

  for (int i=0; i < portCount; i++) 
  {
    delay(random(2000,4500));
    //delay(500);
    digitalWrite(portList[i],LOW);
    delay(100);
    digitalWrite(portList[i],HIGH);
    
  }
    
  for (int i=0; i<4; i++)
  {  
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    delay(500);
  }
}
