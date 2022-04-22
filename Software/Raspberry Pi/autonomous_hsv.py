import RPi.GPIO as GPIO
import time
import serial
import math
import stateplane

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
#GPIO.setup(25, GPIO.IN)
#GPIO.setup(8, GPIO.IN)
#GPIO.setup(23, GPIO.IN)

countyfips = 47141

# Planned Path
lats = [36.160707, 36.1614368, 36.1621665, 36.1622055, 36.1614909, 36.1607763, 36.1608326, 36.1615364, 36.1622402, 36.1622748, 36.1615732, 36.1608716, 36.1609192, 36.1616014, 36.1622835, 36.1622878, 36.1616122, 36.1609365, 36.1609668, 36.1616187, 36.1622705, 36.1622878, 36.1616447, 36.1610015, 36.1610275, 36.1616663, 36.1623051, 36.1628855, 36.1619717, 36.1610578, 36.1610924, 36.1621622, 36.1632319, 36.1633186, 36.1622445, 36.1611704, 36.161231, 36.1622921, 36.1633532, 36.1634052, 36.1623441, 36.161283, 36.1613436, 36.1624134, 36.1634831, 36.1635178, 36.1624654, 36.1614129, 36.1614562, 36.162513, 36.1635697, 36.1635524, 36.1625303, 36.1615082, 36.1615602, 36.162565, 36.1635697, 36.1635697, 36.1626039, 36.1616381, 36.1616555, 36.1626343, 36.1636131, 36.163691, 36.1626906, 36.1616901, 36.1617161, 36.1627252, 36.1637343, 36.1638036, 36.1627815, 36.1617594, 36.1617378, 36.1628097, 36.1638816, 36.1639768, 36.1628768, 36.1617767, 36.16182, 36.1629201, 36.1640202, 36.1640981, 36.1629721, 36.161846, 36.1620539, 36.163102, 36.1641501, 36.1642454, 36.1632276, 36.1622098, 36.1623571, 36.1632406, 36.1641241, 36.1637949, 36.1631496, 36.1625043, 36.1626689, 36.163193, 36.163717, 36.1637083, 36.1631843, 36.1626603, 36.1626949, 36.16318, 36.163665, 36.1636564, 36.1631973, 36.1627382, 36.1627036, 36.1631757, 36.1636477, 36.1636304, 36.1631497, 36.1626689, 36.1626862, 36.163167, 36.1636477, 36.1636564, 36.1631627, 36.1626689, 36.1627122, 36.163206, 36.1636997, 36.1636997, 36.16318, 36.1626603, 36.1626603, 36.1631973, 36.1637343, 36.1637516, 36.163167, 36.1625823, 36.1626862, 36.1632103, 36.1637343, 36.1637776, 36.1633272, 36.1628768]
lons = [-85.5473399, -85.5476269, -85.5479139, -85.5477637, -85.5474821, -85.5472004, -85.5470556, -85.5473346, -85.5476135, -85.5474526, -85.5471763, -85.5469, -85.5467552, -85.5470261, -85.547297, -85.5471307, -85.5468706, -85.5466104, -85.5464655, -85.546723, -85.5469805, -85.5468303, -85.5465701, -85.5463099, -85.5461758, -85.5464172, -85.5466586, -85.5467176, -85.5463609, -85.5460042, -85.5458379, -85.5462617, -85.5466855, -85.5465567, -85.5461115, -85.5456662, -85.5454946, -85.5459291, -85.5463636, -85.5461919, -85.5457682, -85.5453444, -85.545162, -85.5455804, -85.5459988, -85.5458379, -85.5454088, -85.5449796, -85.5447972, -85.545221, -85.5456448, -85.5454409, -85.5450386, -85.5446362, -85.5444431, -85.5448455, -85.5452478, -85.5450332, -85.5446631, -85.5442929, -85.5441105, -85.5444914, -85.5448723, -85.5446899, -85.544309, -85.5439281, -85.543735, -85.5441213, -85.5445075, -85.5443037, -85.5439282, -85.5435526, -85.5433595, -85.543735, -85.5441105, -85.543896, -85.5435259, -85.5431557, -85.5429518, -85.5432952, -85.5436385, -85.543381, -85.5430109, -85.5426407, -85.5424368, -85.5427748, -85.5431128, -85.5428553, -85.5425173, -85.5421793, -85.5419433, -85.5422545, -85.5425656, -85.5421472, -85.541938, -85.5417287, -85.5415034, -85.5416536, -85.5418038, -85.5415249, -85.5414015, -85.5412781, -85.5410743, -85.541187, -85.5412996, -85.5410528, -85.5409348, -85.5408168, -85.5406022, -85.5406827, -85.5407631, -85.5404091, -85.5403769, -85.5403447, -85.5401409, -85.5401409, -85.5401409, -85.5399156, -85.5398941, -85.5398726, -85.5396044, -85.5396205, -85.5396366, -85.5394113, -85.5393952, -85.5393791, -85.5391002, -85.5391324, -85.5391645, -85.5389071, -85.5389017, -85.5388963, -85.5386496, -85.5386818, -85.5387139, -85.5384779, -85.5384618, -85.5384457]

slope = []
intercept = []

for i in range(0,len(lats)):
    [slat,slon] = stateplane(lats[i],lons[i])
    if i < len(lats):
        [slat2,slon2] = stateplane(lats[i+1],lons[i+1])
    else:
        [slat2,slon2] = stateplane(lats[i],lons[i])
    m = (slat-slat2)/(slon-slon2)
    b = slat-(m * slon)
    slope.append(m)
    intercept.append(b)



pwmleft = GPIO.PWM(10, 100)
pwmleft.start(14.2)
pwmright = GPIO.PWM(9, 100)
pwmright.start(14.2)

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter = 0

time.sleep(30)

# Duty limits: 33,45,57

lstill = 14.2
rstill = 14.2
lformin = 16
lformax = 17
rformin = 17
rformax = 17.6
leftdelay = 1
rightdelay = 1

quad = 0
n = 1
g = 1
p = 1
z = 1
count = 0
wait = 0
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
time.sleep(5)
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)

#Check if unicode works
def unicode(serial):
    decode = True
    parsed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    serialdecode = "0,0,0,0,0,0,0,0,0"
    try:
        serialdecode = serial.decode()
    except UnicodeError:
        decode = False
    if decode == True:
        if ',' in decode:
            parsed = serialdecode.split(",")
        else:
            parsed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
        serialdecode = "0,0,0,0,0,0,0,0,0"
        parsed = serialdecode.split(",")
    return parsed

def isnumber(data, value):
    number = True
    try:
        float(data)
    except ValueError:
        number = False

    if number == True:
        num= float(value)
    else:
        num= 0

    return num

#Determine location
def location():
    valid = 1
    while valid > 0:
        pos = ser.readline()
        parsepos = unicode(pos)
        
        if parsepos[0] == '$GNVTG':
            pos = ser.readline()
            parsepos = unicode(pos)

        if parsepos[0] == '$GNGGA':
            pos = ser.readline()
            parsepos = unicode(pos)
        
        if len(parsepos) < 9:   
            deglatitude, northsouth, deglongitude, eastwest = 0,0,0,0
            
        elif len(parsepos) >= 9:
            if (parsepos[3] == '') or (parsepos[4] == '') or (parsepos[5] == '') or (parsepos[6] == ''):
                deglatitude, northsouth, deglongitude, eastwest = 0,0,0,0
                
            else:
                field3 = parsepos[3]
                deglatitude = isnumber(field3,field3)
                field5 = parsepos[5]
                deglongitude = isnumber(field5,field5)
                
                if (parsepos[4] == 'S') or (parsepos[4] == 'N'):
                    northsouth = parsepos[4]
                else:
                    northsouth = 'N'
                if (parsepos[4] == 'E') or (parsepos[6] == 'W'):
                    eastwest = parsepos[6]
                else:
                    eastwest = 'W'
                
            latitude = ((deglatitude - (deglatitude % 100)) / 100) + \
                ((deglatitude % 100) / 60)
            longitude = ((deglongitude - (deglongitude % 100)) / 100) + \
                ((deglongitude % 100) / 60)

            if northsouth == 'S':  # 4 for RMC 3 for GGA
                latitude *= -1

            if eastwest == 'W':  # 6 for RMC 5 for GGA
                longitude *= -1
            
            field8 = parsepos[8]
            course = isnumber(field8) + 90
            if parsepos[8] == '':
                course = 361
        
        meters = 0
        feet = 0

        state = stateplane.from_latlon(latitude, longitude)
        statelat = state[0]
        statelon = state[1]

        if (latitude == 0) or (longitude == 0):
            valid = 1
        else:
            valid = 0

    return [latitude, longitude, course, statelat, statelon] #add course


def distance(lat1,lon1,lat2,lon2,slope,A,B,C):
    R=6371000                               # radius of Earth in meters
    phi_1=math.radians(lat1)
    phi_2=math.radians(lat2)

    delta_phi=math.radians(lat2-lat1)
    delta_lambda=math.radians(lon2-lon1)

    a=math.sin(delta_phi/2.0)**2+\
        math.cos(phi_1)*math.cos(phi_2)*\
        math.sin(delta_lambda/2.0)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    
    waydist = R*c                         # output distance in meters
    pathdist = (( A * lon2)+( B * lat2) + C )/math.sqrt(( A ** 2)+1)
    #leftright = (( A * lon2)+( B * lat2) + C )
    return [waydist, pathdist]


def direction(lat1, lon1, lat2, lon2):

    if (lon2-lon1) == 0:
        traj = 90
    else:
        traj = ((math.atan((lat2-lat1)/(lon2-lon1)))*180)/math.pi

    if lat1 > lat2 and lon1 > lon2:
        traj += 180

    elif lat1 > lat2 and lon1 < lon2:
        traj += 360

    elif lat1 < lat2 and lon1 > lon2:
        traj += 180

    elif lat1 == lat2:
        traj = 0

    return traj


def turnright(timedelay):
    pwmright.ChangeDutyCycle(rformax)
    time.sleep(timedelay)
    pwmright.ChangeDutyCycle(rformin)
    time.sleep(timedelay)


def turnleft(timedelay):
    pwmleft.ChangeDutyCycle(lformax)
    time.sleep(timedelay)
    pwmleft.ChangeDutyCycle(lformin)
    time.sleep(timedelay)


def bigright():
    pwmright.ChangeDutyCycle(rformax)
    pwmleft.ChangeDutyCycle(lstill)
    time.sleep(2)
    pwmright.ChangeDutyCycle(rformin)
    pwmleft.ChangeDutyCycle(lformin)
    time.sleep(2)


def bigleft():
    pwmleft.ChangeDutyCycle(lformax)
    pwmright.ChangeDutyCycle(rstill)
    time.sleep(2)
    pwmleft.ChangeDutyCycle(lformin)
    pwmright.ChangeDutyCycle(rformin)
    time.sleep(2)


while n > 0:
    RMC = location()
    
    if RMC[0] == 0:
        n = 1

    else:
        n = 0
    wait += 1

    if wait > 120:
        n = 0

    time.sleep(1)


# FIRST POINT (WAYPOINT)
RMC = location()
waylat1 = RMC[3]
waylon1 = RMC[4]

#waylat1 = 36.1992700600613
#waylon1 = -85.51498414971903
GPIO.output(27, GPIO.HIGH)
pwmright.ChangeDutyCycle(rformax)
pwmleft.ChangeDutyCycle(lformax)
#time.sleep(20)
'''
while p > 0:
    RMC = location()
    waylat2 = RMC[0]
    waylon2 = RMC[1]
    dist = math.sqrt(((waylat1-waylat2)**2)+((waylon1-waylon2)**2))
    if dist > 0.00003:
        p = 0
    else:
        p = 1
    time.sleep(1)
'''
RMC = location()
waylat2 = RMC[0]
waylon2 = RMC[1]
count = 0

if (waylon2-waylon1)==0:
    slope = 1000
else:
    slope = (waylat2-waylat1)/(waylon2-waylon1)
d = waylat1-(slope * waylon1)

pslope = (1 / slope )*-1
e = waylat1-( pslope * waylon1)

# VARIABLES FOR PATH DISTANCE
a = -slope 
b = 1
c = -d

r = -pslope 
s = 1
t = -e


# PATH DIRECTION
waydir = direction(waylat2, waylon2, waylat1, waylon1)

if waydir < 10:
    dirmin = 360-(10-waydir)
    dirmax = waydir + 10

elif waydir >= 350:
    dirmin = waydir - 10
    dirmax = 10-(360-waydir)

else:
    dirmin = waydir - 10
    dirmax = waydir + 10

if waydir == 10:
    dirmin = 0
    dirmax = 20

if waydir == 350:
    dirmin = 340
    dirmax = 0

if waydir > 0:
    quad = 1

if waydir > 90:
    quad = 2

if waydir > 180:
    quad = 3

if waydir > 270:
    quad = 4






GPIO.output(22, GPIO.HIGH)
time.sleep(2)
# START MOVING
pwmright.ChangeDutyCycle(rformin)
pwmleft.ChangeDutyCycle(lformin)
time.sleep(2)

# START RECORDING
RMC = location()
lat1 = RMC[0]
lon1 = RMC[1]
time.sleep(2)
#angle = RMC[2]
waydist1 = math.sqrt(((waylat1-lat1)**2)+((waylon1-lon1)**2))


for i in range(0,len(lats2)):
    waydistance = 10

    while (waydistance > 0.00009):
        '''
        time.sleep(1)
        pwmright.ChangeDutyCycle(rformax)
        pwmleft.ChangeDutyCycle(lformax)
        time.sleep(3)
        '''
        RMC = location()
        lat2 = RMC[0]
        lon2 = RMC[1]
        #angle = RMC[2]

        waydist2 = math.sqrt(((waylat1-lat2)**2)+((waylon1-lon2)**2))
        pathdist2 = (( a * lon2)+( b * lat2) + c )/math.sqrt(( a ** 2)+1)
        leftright = (( a * lon2)+( b * lat2) + c )

        if pathdist2 < 0:
            pathdist2 = pathdist2 * -1

        dir2 = direction(lat1, lon1, lat2, lon2)

        if waydist2 >= waydist1:

            if waydir < 180:
                if (dir2 > (waydir+180)) or (dir2 < waydir):
                    bigleft()

                elif (dir2 < (waydir+180)) and (dir2 > waydir):
                    bigright()

            if waydir >= 180:
                if (dir2 > (waydir-180)) and (dir2 < waydir):
                    bigleft()

                elif (dir2 <= (waydir-180)) or (dir2 > waydir):
                    bigright()

        elif (waydist2 > 0.00002):

            if (pathdist2-pathdist1) > 0.00002:

                if dir2 > dirmax:
                    turnright()

                elif dir2 < dirmin:
                    turnleft()

            if pathdist2 > 0.00002:
                if (quad == 2) or (quad == 3):
                    if leftright > 0:
                        turnleft()
                        turnright()

                    elif leftright < 0:
                        turnright()
                        turnleft()

                if (quad == 1) or (quad == 4):
                    if leftright < 0:
                        turnleft()
                        turnright()

                    elif leftright > 0:
                        turnright()
                        turnleft()

        elif (waydist2 < 0.00002):
            g = 0
        lat1 = lat2
        lon1 = lon2
        waydist1 = waydist2
        pathdist1 = pathdist2

        time.sleep(1)
    
GPIO.cleanup()
