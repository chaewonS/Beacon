# -*- coding: utf-8 -*-
# test BLE Scanning software
# jcs 6/8/2014


import blescan
import sys

import bluetooth._bluetooth as bluez

#FB301BC 초기 설정 TxPower = 41
def calculateDistance(rssi) :
    txPower = 41
    if (rssi == 0) :
        return -1.0 #if we cannot determine distance return -1.
    ratio = rssi*1.0/txPower #
    if (ratio < 1.0) :
        return ratio**10
  
    else:
        accuracy =  (0.89976)*(ratio**7.7095) + 0.111
        return accuracy
# #https://github.com/location-competition/indoor-location-competition-20

def simpleDistance(rssi):
    TxPower = 41
    return 10 ** ((TxPower - rssi )/(10/4)) # 4 = n : 실내공간


dev_id = 0
try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"

except:
        print "error accessing bluetooth device..."
        sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
        returnedList = blescan.parse_events(sock, 10)
        print "----------"
        for beacon in returnedList:
                if beacon[:17] == '00:19:01:70:81:': #특정 비콘을 선택해서 출력
                        rssi = beacon[66:]
                        print beacon
                        print "rssi :  %s" %rssi
                        print "distance of calc : %f" %calculateDistance(int(rssi))
                        print "distance of simple : %f" %simpleDistance(int(rssi))
                        print "================================================="
