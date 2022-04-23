#include <SPI.h>
#include "printf.h"
#include "RF24.h"
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); // RX, TX

// instantiate an object for the nRF24L01 transceiver
RF24 radio(9, 8); // using pin 9 for the CE pin, and pin 8 for the CSN pin

const byte address[6] = "00001";
char msg[90] = {0};
String battery_msg;
char battery_msg_char[32] = {0};

int SelectPin0 = 5;
int SelectPin1 = 6; // Pins used for mux select lines
int MeasuredCell1 = A0;
int MeasuredCell2 = A1; // Pin used to measure voltage from mux
float CellVoltage1 = 0;
float CellVoltage2 = 0;
float MinVoltage = 2.5; // Threshold for "dead" battery cell

void SelectLineOut(bool S0, bool S1) {
  digitalWrite(SelectPin0, S0);
  digitalWrite(SelectPin1, S1);
}

bool BatteryCheck() {
  // Cycles through select lines outputs 00,01,10,11
  for (int i = 0; i < 4; i++)
  {
    SelectLineOut(bitRead(i, 0), bitRead(i, 1));
    CellVoltage1 = analogRead(MeasuredCell1) * 5.07 / 1024.0; // Checks the voltage at both
    //delay(10);
    CellVoltage2 = analogRead(MeasuredCell2) * 5.07 / 1024.0; // cells for each select line output

    battery_msg = String(String(CellVoltage1, 2) + "  " + String(CellVoltage2, 2));
    if (i == 3) {
      battery_msg = String(String(CellVoltage1, 2) + "  " + String(CellVoltage2, 2) + "\n");
    }
    battery_msg.toCharArray(battery_msg_char, 32);
    //Serial.println(battery_msg_char);
    //Serial.println(strlen(battery_msg_char)+1);
    radio.write(&battery_msg_char, strlen(battery_msg_char) + 1);
    /*if(CellVoltage1 < MinVoltage)
      return true;
      if(CellVoltage2 < MinVoltage)
      return true;*/

  }
}

void setup() {

  // Battery Monitoring Pins
  pinMode(SelectPin0, OUTPUT);
  pinMode(SelectPin1, OUTPUT);
  pinMode(MeasuredCell1, INPUT);
  pinMode(MeasuredCell2, INPUT);

  Serial.begin(115200);

  mySerial.begin(115200);
  //mySerial.println("mySerial");
  //Serial.println("Serial");

  radio.begin();

  radio.setPALevel(RF24_PA_HIGH);  // RF24_PA_MAX is default.

  // set the TX address
  radio.openWritingPipe(address);

  // put radio in TX mode
  radio.stopListening();

}

void loop() {

  if (mySerial.available()) {
    for (int pos = 0; pos < 90; pos++)
    {
      msg[pos] = mySerial.read();
    }
    //Serial.println(msg);

    radio.write(msg, strlen(msg));
  }

  if (!mySerial.available()) {
    const char err[] = "NoData";
    radio.write(&err, sizeof(err));
    Serial.println(err);
  }
  else {
    radio.write(&msg, sizeof(msg));
  }

  BatteryCheck();
  //Serial.println();

  //delay(250);


}
