# -*- coding: utf-8 -*-
# test BLE Scanning software
# jcs 6/8/2014

from turtle import distance
import blescan
import sys
import csv

import bluetooth._bluetooth as bluez

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
    return 10 ** ((TxPower - rssi )/(10*4)) # 4 = n : 실내공간


if(sys.argv >0):
    add_to_filename = sys.argv[1]#사용자 입력 파일명에 추가할 이름

with open('ML_4F_'+ add_to_filename + '.csv', 'wb') as f:
    w=csv.writer(f)
    w.writerow(['MACaddress','distance','RSSI'])
    dev_id = 0
    try:
            sock = bluez.hci_open_dev(dev_id)
            print("ble thread started")

    except:
            print("error accessing bluetooth device...")
            sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)

    num = 0
    while num <= 1000:
          returnedList = blescan.parse_events(sock, 10)
          for beacon in returnedList:
                    #if beacon[:17] == '00:19:01:70:81:': #특정 비콘을 선택해서 출력
                    if beacon[:5] =='00:19':
                         rssi = beacon[66:]
                         rssi = beacon[66:]
                        #  print("simple distance:",simpleDistance(int(rssi)))
                         data = (str(beacon[12:17])+" "+str(calculateDistance(int(rssi)))+" "+ str(rssi)).split(" ")
                         if(data.__len__() is 3):#오류 없이 됐을 때만 반복 체크 및 해당 데이터 작성
                              num += 1
                              w.writerow(data)
                              print(num)
    print("done!")