# Raspberry Pi:
Parts Needed:
  * Keyboard
  * Mouse
  * 16 GB micro SD card
  * micro SD card reader
  * micro HDMI to HDMI cable
  * 5V 3A power cable

Installing Raspberry Pi OS
Download Raspberry Pi Imager:
https://www.raspberrypi.com/software/


* Insert micro SD card into PC using micro SD card reader
* Open Imager
* Click "Choose OS"
* Click "Raspberry Pi OS (32-bit)
* Click "Choose Storage" and select the inserted SD card
* Click "Write"
* Eject SD card when done

Setting up the Raspberry Pi
* Insert micro SD card into Raspberry Pi
* Connect mouse and keyboard
* Connect Raspberry Pi to monitor through left micro HDMI port using adapter cable
* Connect Raspberry Pi to power
* Follow on screen instructions to setup Raspberry Pi OS


Upgrade the Raspberry Pi:

```
sudo apt update
sudo apt full-upgrade
```
 
Install git if not installed already
```
sudo apt install git
```

Install pip
```
sudo apt get-install python3-pip
```

Install numpy
```
pip install numpy
```

Install proj
```
pip install proj
```

Install pyproj
```
pip install pyproj
```

Install stateplane
```
pip install stateplane
```

In order for the Raspberry Pi to interface with the GPS receiver, type the following command:
```
sudo raspi-config
```

Select Interfacing Options, Serial, No, Yes, Finish

Now you can use the python program above. <br/>

To enter a predetermined path into the program, enter a list of latitude points into the lats[] list and enter longitude points into the lons[] list.
Change the countyfips value to the one corresponding to your state and county.


