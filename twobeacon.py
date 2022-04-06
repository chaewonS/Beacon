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
                for x in top2_list:
                    maclist.append(x.getMAC())

                if (now_mac in maclist) and (top2_list[maclist.index(now_mac)].getRSSI() < now_rssi):#1. 리스트에 이미 있는 비콘이며, 더 가까워진 경우.
                    if len(top2_list) <2:#비콘이 하나 있을 때
                        top2_list[maclist.index(now_mac)].RSSI = now_rssi
                        #top2_list.sort(key= lambda x : x.getRSSI())
                    else:
                    #2개가 꽉 찼음을 발견했을 때
                        top2_list[maclist.index(now_mac)].RSSI = now_rssi #동일한 비콘의 RSSI를 수정한다.
                        top2_list.sort(key= lambda x : x.getRSSI())
                        print("==============================")
                        for x in top2_list:
                            if top2_list[0].RSSI == -100 or top2_list[1].RSSI == -100:
                                break
                            print("%s그룹,  id : %s RSSI: %s" %(x.G, x.MAC[12:], x.RSSI))

                elif (now_mac not in maclist): #2. 중복된 기기가 아니면 추가
                    #이하 코드 같음
                    if len(top2_list) <2 and top2_list[0].G == info[now_mac].G:
                        top2_list.append(Beacon(now_mac, now_rssi)) #리스트에 추가
                        top2_list.sort(key= lambda x : x.getRSSI())
                    else: #큐 동작
                        top2_list[0] = Beacon(now_mac, now_rssi)  #rssi가 가장 작은 비콘을 삭제하고 추가
                        top2_list[1] = Beacon('00:19:01:70:81:ed','-100') #그룹 비콘만을 나타내기 위해 뒤의 자리를 비워줌
                        top2_list.sort(key= lambda x : x.getRSSI())
                       # for x in top2_list:
                       #     if top2_list[0].RSSI == -100 or top2_list[1].RSSI == -100:
                       #         break
                       #     print(x)
                       #     print("==============================")
                       #     print("%s그룹,  id : %s RSSI: %s" %(x.G, x.MAC[12:], x.RSSI))
