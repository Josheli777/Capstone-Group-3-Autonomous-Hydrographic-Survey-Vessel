# Capstone-Group-3-Autonomous-Hydrographic-Survey-Vessel

# Introduction: <br/>
Hydrography is the science of surveying and measuring different bodies of water, such as lakes, rivers, oceans, etc. These analyses are crucial for determining the shape of the water body. This data obtained from hydrography can be used to monitor the effects of climate change, beach erosion, and natural disaster prediction. Additionally, civil engineers must know the layout of a body of water before starting projects like dredging, diverting water sources, building docks, etc. The Tennessee Water Center currently has boats that take hydrographic projections that are remote-controlled; however, this technology is prone to human error and lacks efficiency that could be further improved by automation. There are currently autonomous vehicles that take measurements accurately and precisely. These boats take GPS coordinates and create parallel lines for the boat to travel to retreive less repetitious measurements.  The Water Center has contacted us to design a boat that has similar functionality to commerically avaialble hydrographic boats but at a significantly lower cost. The Water Center has asked that the boat can transmit GPS data and depth measurements in real time to allow surveyors to determine if data is accurate. If the data is not accurate, the team will be able to immediately bring the boat back to land base and not have to wait for the boat to complete its run. 

# Project Capabilities: <br/>
* Navigating bodies of water using a predetermined path
* Calculate its GPS location with centimeter level precision and accuracy
* Transmits GPS data and battery cell voltages for monitering
* Switches between manual and autonomous control through a remote controller switch
* Navigate bodies of water at a speed of 3ft/s for about 3 hours.

# Salient Outcomes: <br/>
## Battery Testing and Monitoring: 
The Water Center has requested that the autonomous hydrographic surveying boat have a run time of at least one hour and an accurate battery monitoring system. The current design of the power subsystem allows surveying teams to operate the boat for approximately 3 hours by use of 2 Liperior Lithium-Polymer batteries (14.8 V, 22000 mAh) connected in parallel. Additionally, 2 quad op-amp circuits were constructed and implemented that provide voltage readings of each cell in the Liperior batteries. These voltages can be verified by using the battery charging station that displays the actual cell voltages. 

## Data Transmission:
The specification to communicate data such as hydrographic measurements, GPS location, and battery voltage levels from the boat to a land base in real time has been addressed by the data transmission subsystem.  A pair of Arduino Unos and two nRF24L01+ radio modules were used in the subsystem design. The subsystem uses 2.4 GHz radio frequency (RF) to transmit the collected data to the base station PC. This system tested on Cane Creek, and it was confirmed that it could reliably transmit GPS data and battery voltage levels measured from the onboard battery monitoring system. The most up-to-date version of this system had a reliable connection at up to 550 meters and was transmitting GPS and battery data successfully. Additional work will be needed to complete the integration with the sonar system in order to transmit hydrographic data. 

## GPS Accuracy and Precision:
The use of Real-Time-Kinematic GPS receivers allowed us to achieve GPS data with much more accuracy than normal receivers. This project makes use of two simpleRTK2b receivers with a long-range transmission to receive latitude and longitude coordinates with centimeter level accuracy and precision. The two receivers are set up in a base and rover configuration. This allows the “rover” receiver, which is on the boat itself, to receive RTCM corrections from the “base” receiver which is connected to a PC on land. For this project, centimeter level accuracy and precision is required for the boat to navigate the predefined path. This can only be achieved if the location of the PC with the base station is known and uploaded to the base station receiver. After testing this configuration, the accuracy was found to be 2 cm and the precision was about 3 cm. 

# Video of Project Testing: <br/>
Full test (all systems communicating): https://youtu.be/emZcUE4ue-M


# Video of Experimental Analysis: <br/>
Battery Testing: https://www.youtube.com/embed/ibnFtC95N1E <br/>
Data Transmission Range Testing: https://www.youtube.com/embed/1JbO_NOVdsQ <br/>
Speed Testing: https://www.youtube.com/watch?v=HDup7zcuE3E&t=6s <br/>
GPS Accurcy & Precison Testing: https://www.youtube.com/watch?v=qKELYZJ67d8&t=15s <br/>
Switching Between Autonomous and Manual Control Testing: https://www.youtube.com/watch?v=emZcUE4ue-M&t=8s <br/>
Updated Battery Monitor: https://youtube.com/shorts/7BtCwoOhJbw?feature=share <br/>

Updated code attempting to navigate: https://youtube.com/shorts/_wtcSN0W4yQ <br/> 

# Images: <br/>
  ![Boat Prototype](https://user-images.githubusercontent.com/104117150/164588852-5f07d6c0-d166-4189-8924-e7fbc01b8f6a.jpg) <br/>
  Autonomous Hydrographic Boat Prototype
 
# About Us: <br/>
The team members involved in the construction of the autonomous hydrographic boat are Andrew Alley, Carter Ashby, Levi Daniel, & Joshua Herrera. Mr. Jesse Roberts provided guidance and insight thoughout the duration of the project. This project was funded by Dr. Alfred Kalyanapu on behalf of the Tennessee Tech Water Center.

# Repository Contents: <br/>

### Project Documentation:
Bill of materials for the project and schematics for each subsystem.

### Reports:
Reports that document the design process for this project.

### Software:
Guides for installing computer applications, programming libraries, and operating systems necessary for this project.
