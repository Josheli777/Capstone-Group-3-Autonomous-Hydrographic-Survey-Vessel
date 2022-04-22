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
Battery Testing: Thw Water Center had a specification that the autonomous boat must be able to successfully drive the entirety of Cane Creek Lake (0.2266 km^2) in one run. The base station was set up at the dam of Cane Creek Lakeand the boat drove along the dam 56 times at a constant speed of 3-5 ft/s. The speed was determined by using the speeds used by the Water Center to obtain accurate depth measurements. The boat was kept close to the dam due to the boat not being completel waterproof. The inside of the hull was not coated in fiberglass, which allows water to get into the hull and weigh it down. If the boat was to have an issue with water getting in the hull, the team could easily get the boat out of the lake and prevent any damage to the circuits. The battery monitoring circuit showed that the voltages of each cell was 4.2 V, and when the batteries are considered "low", the voltge is approximately 3.7 V. The boat successfully drove the distance determined to be equal to the area of Cane Creek Lake. The team then determined how long the boat could run, and it was concluded that the boat can remain fully operational for approximately 3 hours. The test came to an end when the team noticed that the thrusters started to slow down after full thrust, thus becoming a risk if the boat was hypothetically in the middle of the lake. Additionally, the battery monitoring circuit was transmitting data to the land base, which showed that the cells in the batteries had a voltage of 3.7 V. 

Data Transmission: Rather than testing the radio module's transmission range at Cane Creek Lake, the team tested the range on campus because the hull was taken to get coated in more fiberglass. One team member stood outside of Foster Hall on Tennessee Tech's campus with the laptop and land radio module, while two other team members carried the rover radio module down University Drive until the land module could not receive any data. Data transmission slowed down once the team members crossed North Willow Avenue going towards Tech Village. The last received transmission was about 596 m.

GPS Accuracy and Precision: Using two simpleRTK2b receivers, the accuracy and precision of the recorded GPS data was observed. The receivers were in a base and rover configuration. Using just the rover receiver, the GPS coordinates were accurate to within 1.4 meters and precise to within 10 centimeters. Using the base station and the rover, the accuracy was around 1.9 meters and the precision was 2 centimeters. The base station and rover were tested again with the known location of the base station uploaded to the base station receiver. The accuracy was withing 2 cm and the precision was within 3 cm.

# Video of Project Testing: <br/>
Full test (all systems communicating): https://youtu.be/emZcUE4ue-M


# Video of Experimental Analysis: <br/>
Battery Testing: https://www.youtube.com/embed/ibnFtC95N1E <br/>
Data Transmission Range Testing: https://www.youtube.com/embed/1JbO_NOVdsQ <br/>
Speed Testing: https://www.youtube.com/watch?v=HDup7zcuE3E&t=6s <br/>
GPS Accurcy & Precison Testing: https://www.youtube.com/watch?v=qKELYZJ67d8&t=15s <br/>
Switching Between Autonomous and Manual Control Testing: https://www.youtube.com/watch?v=emZcUE4ue-M&t=8s <br/>

# Images: <br/>
  ![Boat Prototype](https://user-images.githubusercontent.com/104117150/164588852-5f07d6c0-d166-4189-8924-e7fbc01b8f6a.jpg) <br/>
  Autonomous Hydrographic Boat Prototype
 
# About Us: <br/>
The team members involved in the construction of the autonomous hydrographic boat are Andrew Alley, Carter Ashby, Levi Daniel, & Joshua Herrera. Mr. Jesse Roberts provided guidance and insight thoughout the duration of the project. This project was funded by Dr. Alfred Kalyanapu on behalf of the Tennessee Tech Water Center.
