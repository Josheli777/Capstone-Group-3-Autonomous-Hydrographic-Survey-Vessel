# Arduino

## Software Description
Two Arduino Uno's are currently used to read GPS data, control the battery monitoring subsystem, and transmit/receive data using the nRF24L01+ radio modules.

### Rover Arduino:
The script "ROVER_full_function.ino" was written to control the Arduino on the rover. The serial baud rate should be set in 'setup()' to match the output baud rate of the simplertk2b GPS. Commands to start and configure the nRF24L01+ radio module and initialize pins for the battery monitoring task are also written in the 'setup()' function. The radio module is setup as the transmitter.<br/><br/>
The 'loop()' function contains the instructions for the primary functionality of the onboard Arduino. The program checks the Arduino's serial buffer for GPS data, and if data is found, it reads it and sends it to the radio module for wireless transmission. If no data is found in the buffer, a message that says "NoData" is transmitted by the radio module.<br/><br/>
Next, the 'BatteryCheck()' function is called. The function uses two GPIO pins to control the select lines of the 4 to 1 multiplexers. Two analog input pins on the Arduino are used to read the voltage levels of the multiplexer outputs. The program cycles through each of the battery cell voltage levels by changing the values on the select lines. The select line values are written to the appropriate pins in the 'SelectLineOut()' function. The voltages are converted from what the analog pins return to the actual voltage value. These voltage values are sent to the radio modules for transmission. The program continues by starting the next iteration of the 'loop()' function.

### Base Station Arduino:
The script "BASE_RX.ino" was written to control the Arduino at the base station. This Arduino will be connected to the technician's computer via its USB port. Commands to start and configure the nRF24L01+ radio module are written in the 'setup()' function. An if statement checks if the radio module starts successfully. The radio module is setup as the receiver.<br/><br/>
The 'loop()' function checks if the radio has received any transmissions, and if it has, it reads the information and outputs it to the Arduino serial buffer.

## Dependencies
The Arduino SPI library is used in both scripts to communicate to the nRF24L01+ modules using SPI protocol.<br/><br/>
The external RF24 library is used to control the radio modules in both scripts. https://github.com/nRF24/RF24 <br/><br/>
The Arduino SoftwareSerial library is used by the rover Arduino to make two GPIO pins (2,3) function as serial pins (TX/RX).

## Installation
Both .ino files can be downloaded and opened in the Arduino IDE. To upload the scripts to the Arduinos, connect the computer running the IDE to the USB port of the approprate Arduino and select "Upload". Note that the .ino files must be in a folder of the same name (excluding the '.ino') to upload properly. When the "Done uploading" message is displayed, the program will now execute on power-on until it is overwritten by another program. For more details on using the Arduino IDE follow https://docs.arduino.cc/learn/starting-guide/the-arduino-software-ide

## How to Operate
Refer to the design schematics to connect power and onboard components to the rover Arduino. The uploaded program will execute at power-on.<br/><br/>
The base station Arduino should remain connected to the base station computer via USB. The data received from the rover can be viewed by clicking Tools->Serial Monitor and changing the baud rate to match the baud rate set in the "BASE_RX.ino" script.
