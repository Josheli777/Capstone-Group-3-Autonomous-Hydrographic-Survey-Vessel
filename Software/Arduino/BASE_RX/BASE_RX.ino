#include <SPI.h>
//#include "printf.h"
#include "RF24.h"

// instantiate an object for the nRF24L01 transceiver
RF24 radio(9, 8); // using pin 9 for the CE pin, and pin 8 for the CSN pin

const byte address[6] = "00001";

void setup() {
  
  Serial.begin(115200);

  // initialize the transceiver on the SPI bus
  if (!radio.begin()) {
   Serial.println(F("radio hardware is not responding!!"));
   while (1) {} // hold in infinite loop
  }

  radio.setPALevel(RF24_PA_HIGH);  // RF24_PA_MAX is default.

  // set the RX address
  radio.openReadingPipe(0, address);

  // put radio in RX mode
  radio.startListening();

}

void loop() {

  if (radio.available())
  {
    char msg[22] = {0};
    radio.read(&msg, sizeof(msg));
    Serial.println(msg);
  }
}
