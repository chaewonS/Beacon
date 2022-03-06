# BLE SCAN PROGRAM

# for scanning for BLE devices
from gattlib import DiscoveryService

# scan function
def scan( str, str1 ):
    print("Scanning for {}...\n".format(str1))
    service = DiscoveryService()
    devices = service.discover(8)

    for address, name in devices.items():
        if address == str:
            print("Beacon found - device: {}\n".format(str1))  
            return True

    return False

# setting each device to false at first, if it is found in scan, will be turned to true
AllDev = True
dev1 = False
dev2 = False
dev3 = False

# setting a counter for each device
count1 = 0
count2 = 0
count3 = 0

# setting each device to their address Ex: "0C:F3:EE:0D:79:5B"
beacon1 = "00:19:01:70:82:41"  
beacon2 = "00:19:01:70:82:AF" 
beacon3 = "00:19:01:70:80:D9"

# naming each device, Ex: device1 = "Oculus Rift"
device1 = "8241"
device2 = "82AF"
device3 = "80D9"

# main file
while AllDev == True:

    # device 1 block

    dev1 = scan(beacon1, device1)
    if dev1 == True:
        print("Found\n")
        count1 = 0
    if dev1 == False:
        print("Not Found\n")
        count1 += 1
    if count1 == 3:
        print("Scan dev1 \n")

    # device 2 block

    dev2 = scan(beacon2, device2)
    if dev2 == True:
        print("Found\n")
        count2 = 0
    if dev2 == False:
        print("Not Found\n")
        count2 += 1
    if count2 == 3:
        print("Scan dev2 \n")

    # device 3 block

    dev3 = scan(beacon3, device3)
    if dev3 == True:
        print("Found\n")
        count3 = 0
    if dev3 == False:
       print("Not Found\n")
       count3 += 1
    if count3 == 3:
        print("Sending Alert\n")
