# Ardusimple
The simpleRTK2b LR kit comes with two receivers that are preconfigured as a base and rover. They are marked with a 'B' and 'R' respectively.
These configurations need to be changed in order for the program in this repository to work. Further configurations would require alterations
to both the Raspberry Pi Python code and the Arduino code in order for this project to function properly. <br/>

To configure the simpleRTK2b base and rover receivers, download the u-center application. <br/>
Download the configuration files above and follow the instructions below to upload them to the base and rover receivers. <br/>

### U-center
Download u-center here: https://www.u-blox.com/en/product/u-center <br/>

Make sure to download u-center and NOT u-center2 . The chip in the simpleRTK2b receiver is not compatible with u-center 2.

### Base Station:
* Download baseconfiguration.txt
* Connect the batch antenna to the simpleRTK2b base receiver and place near window
  to receiver GPS data.
* Connect the base receiver to a laptop using the micro-USB port labeled "Power+GPS"
* Wait until the receiver is set up.
* Open u-center
* Click the "connect serial port" button at the bottom left of the menu bar.
* Click the port connection that the receiver is connected to (COM4, COM3, etc.).
* Click "Tools", "Receiver Configuration", "Transfer GNSS to File", name current configuration and save it
  in a known location if you plan on using it later.
* Click "Tools", "Receiver Configuration", "Transfer File to GNSS", upload the baseconfiguration.txt
* Wait until GPS data appears in the top right window.
* Disconnect receiver
* Done

To upload the known location of the base station to the receiver, do the following:
* Plug in the base station to your laptop or PC
* Open u-center
* Click "View", "Configuration View", "TMODE3", "fixed mode"
* Click "Use Lat/Lon/Alt position"
* Enter in latitude, longitude and altitude.
* Click "Send", "Poll", exit and save the configurations.
* Exit window
* Done


### Rover:

* Download roverconfiguration.txt
* Repeat steps for base station except upload receiverconfiguration.txt


