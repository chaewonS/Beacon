# -*- coding: utf-8 -*-
# test BLE Scanning software
# jcs 6/8/2014


import blescan
import sys
import io
import json
import bluetooth._bluetooth as bluez

dev_id = 0
try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"

except:
        print "error accessing bluetooth device..."
        sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
maclist = []
beacons = 0
while True:
        returnedList = blescan.parse_events(sock, 10)
        print "----------"
        for beacon in returnedList:
                #if beacon[:17] == '00:19:01:70:86:03': #특정 비콘을 선택해서 출력
                if beacon[:5] =='00:19':
                        mac = beacon[:17]
                        rssi = beacon[66:]
                        if mac not in maclist:
                            maclist.append(mac)
                            beacons = beacons+1
                        
                        print beacon
                        print "rssi :  %s" %rssi
                        print "================================================="
                        print("총 %d개의 비콘을 찾았습니다." %beacons)
                        for x in maclist:
                            print ("%s : %s" %(x[12:17], info[x]['place']))
