# -*- coding: utf-8 -*-

import math

import io
import blescan
import sys
import bluetooth._bluetooth as bluez
import json


import threading

with io.open('./test.json') as f:
    info = json.load(f)
#====================================Classes============================================

class Beacon():
    def __init__(self, mac, rssi):
        self.MAC = mac
     
    # self.X = 'MAC 주소 활용해서 만들어진 test.json파일에서 가져온 X'
    # 비콘 x, y 좌표 출력 부분 추가
        
        self.X = int(info[mac]["location"].split(',')[0])
        self.Y = int(info[mac]["location"].split(',')[1])
        self.RSSI = int(rssi) #거리 반비례 변수, *음수도 정수 변환 가능 *
        self.G = int(info[mac]["group"])

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getXY(self):
        return self.X, self.Y

    def getRSSI(self):
        return self.RSSI

    def getMAC(self):
        return self.MAC
    def getG(self):
        return self.G

#========================================= End Of Classes ============================================

global top2_list


top2_list =[Beacon('00:19:01:70:81:ed','-100'),Beacon('00:19:01:70:82:62','-100')]


dev_id = 0#scan

#========================================== Definition Of Functions ==================================
def flusshing():#5초마다 
    print("Timer")
    timer = threading.Timer(5, flusshing)


    global top2_list
    top2_list =[Beacon('00:19:01:70:81:ed','-100'),Beacon('00:19:01:70:82:62','-100')]
    timer.start()

#FB301BC 초기 설정 TxPower = 41


#================== Select three ==================================

if __name__ == '__main__':

    #====init========
    locationX = -100
    locationY = -100
    flusshing()

    try:
        sock = bluez.hci_open_dev(dev_id)
        print("ble thread started")

    except:
        print ("error accessing bluetooth device...")
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)



    while True:
        top2_list = [Beacon('00:19:01:70:81:ed','-100'),Beacon('00:19:01:70:82:62','-100')]

        maclist = []
        returnedList = blescan.parse_events(sock, 10)
        #print("----------")
        
        for beacon in returnedList:

            if beacon[:5] == "00:19":
                #print(beacon)
                
                now_mac = beacon[:17]
                now_rssi = beacon[66:] 

                maclist =[]
                top2_list.sort(key= lambda x : x.getRSSI())

                for x in top2_list:
                    maclist.append(x.getMAC())
                    print("%s그룹,  id : %s RSSI: %s" %(x.G, x.MAC[12:], x.RSSI))
