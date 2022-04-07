# -*- coding: utf-8 -*-

import io
import threading

import blescan
import sys
import bluetooth._bluetooth as bluez
import json
import threading

def flusshing():
    print("Timer")
    timer = threading.Timer(5, flusshing)#5초 뒤 이 함수 재실행
    global top2 #전역변수를 함수내에 불러온다.
    top2 =[Beacon('00:19:01:70:81:ed','-100'),Beacon('00:19:01:70:82:62','-100')]
    timer.start()

class Beacon():
    def __init__(self, mac, rssi):#주소, rssi
        self.MAC = mac
        self.RSSI = int(rssi)
        self.G = int(file[mac]["group"])

with io.open('./beacon.json') as f:
    file = json.load(f)

global top2

if __name__ == '__main__':
    flusshing()#주기적으로 리스트를 비워준다. 

    try:
        sock = bluez.hci_open_dev(0)#dev_id = 0
        print("ble thread started")
    except:
        print("error accessing bluetooth device..")
        sys.exit(1)#프로그램을 비정상적으로라도, 강제적으로 종료시키고 싶을 때
    
    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)

    while True:
        #초기화
        top2 = [Beacon('init1','-100'), Beacon('init2','-100')]
        returnedList = blescan.parse_events(sock, 10)
        
        for beacon in returnedList:#blescan 스레드에서 반환되는 신호 리스트
            if beacon[:5] == "00:19":#FB301이 들어오면
                #새로 탐지된 신호의정보
                now_mac = beacon[:17]
                now_rssi = beacon[66:]

                #현재 가까운 2가지의 mac 주소를 저장시키는 리스트
                maclist=[]
                for x in top2:
                    maclist.append(x.MAC) #[init, 00:19~]
                print("origin top2 mac list = {}".format(maclist))

                if (now_mac in maclist):
                    #현재 top2 출력
                    print("already exist beacons!")
                    for i in top2:
                        print("{}:{}".format(i.MAC, i.RSSI))
                    #들어갈 자기자리 (mac")를 찾아 바꿈 ================바뀌는 부분!=====================
                    for a in range(2):
                        #자기자리에 나보다 약한애가 있으면
                        if top2[a].MAC == now_mac and top2[a].RSSI < now_rssi:
                            top2[a] = Beacon(now_mac, now_rssi)
                    print("this is updated top2 by exist beacon:")
                    for i in top2:
                        print("{}:{}".format(i.MAC, i.RSSI))

                else:
                    print("new beacon detected!")
                    for i in top2:
                        print("{}:{}".format(i.MAC, i.RSSI))

                    #새 비콘 정보 반영하기=================바뀌는 부분!!========================
                    for a in range(2): #mac주소가 다른 비콘 두가지 중 앞의 약한 한놈 갈아치우기
                        
                        if top2[a].RSSI < now_rssi:
                            top2[a] = Beacon(now_mac, now_rssi)
                            break#비콘 바꾸는 리스트 탐색 종료: 한 번 조건문 들어가면 끝나게 됨
                            #만약 두번째에 있는애가 너무 강해서 바뀌지 않는 경우 fllushing 함수가 처리해줄것이라 기대함.
                    print("this is updated top2 by new beacon:")
                    for i in top2:
                        print("{}:{}".format(i.MAC, i.RSSI))
                    
