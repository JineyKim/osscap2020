#include "Keyboard.h"

int handle;

void setup() {
  pinMode(A0, INPUT);
  Keyboard.begin();
}

void loop() {
  handle=analogRead(A0);
  
  if(handle<245&&handle>153){
    Keyboard.press(KEY_LEFT_ARROW);
    delay(33);
  }
  else if(handle>260&&handle<351){
    Keyboard.press(KEY_RIGHT_ARROW);
    delay(33);
  }
  else if(handle>245&&handle<260){
    Keyboard.releaseAll();
    delay(10); 
  }
}
