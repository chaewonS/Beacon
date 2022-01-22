import blescan
import sys
import bluetooth._bluetooth as bluez
import json


import threading

#====================================Classes============================================
class Beacon():
    def __init__(self, mac, rssi):
        self.MAC = mac
        with open('./test.json') as f:
            info = json.load(f)
        # self.X = 'MAC 주소 활용해서 만들어진 test.json파일에서 가져온 X'
        # 비콘 x, y 좌표 출력 부분 추가
        if mac[:5]=="00:19":
            self.X = info[mac]["location"].split(',')[0]
            self.Y = info[mac]["location"].split(',')[1]
            self.RSSI = int(rssi) #거리 반비례 변수, *음수도 정수 변환 가능 *
        else:
            print("비콘이 아닙니다.")

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


#========================================= End Of Classes ============================================

global top3_list #* 함수 안에서도 접근 가능하도록 함 *

top3_list =[Beacon(0,-1),Beacon(0,-1),Beacon(0,-1)]

dev_id = 0#scan

#========================================== Definition Of Functions ==================================
def flusshing():
    print("Timer")
    timer = threading.Timer(5, flusshing)#필요에 따라 증감하세요

    global top3_list
    top3_list =[Beacon(0,-1),Beacon(0,-1),Beacon(0,-1)]

    timer.start()

def getTrilateration(first, second, third): #세 기준점과 세 기준점으로부터의 직선거리가 주어졌을 때  위치 (x,y)를 계산
    x1, y1 = first.getXY()
    x2, y2 = second.getXY()
    x3, y3 = third.getXY()
    #거리값을 rssi역수로 취했을 때
    r1 = 1/first.getRSSI()
    r2 = 1/second.getRSSI()
    r3 = 1/third.getRSSI()

    S = (x3**2 - x2**2 + y3**2 - y2**2 + r2**2 - r3**2 )/2.0
    T = (x1**2 - x2**2 + y1**2 + y2**2 + r2**2 - r1**2)/2.0

    y = (  ((T*(x2-x3))) - (S *(x2-x1))  ) / (  ((y1-y2)*(x2-x3)) -  ((y3-y2)*(x2-x1)) )
    x = ((y* (y1-y2)) - T) /(x2-x1)
    return x,y

#================== Select three ==================================
##입력:: n초에 m개씩 수신되는 무작위 신호

##거리를 연산할 무작위 신호를 담을 틀
 #신호 object : id/세기...1 class beacon
####**거리 연산은 무조건 짧은 연산 필요** -> (거리 ∝ 1/rssi) 활용해서 rssi 자체를 사용


if __name__ == '__main__':
    #====init========
    lacationX = -1 #최종 보행자 좌표
    locationY = -1
    flusshing()#n 초마다 top3list를 초기화 한다.

    try:
        sock = bluez.hci_open_dev(dev_id)
        print("ble thread started")

    except:
        print ("error accessing bluetooth device...")
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)



while True:
    top3_list = [Beacon(0,-1),Beacon(0,-1),Beacon(0,-1)] #*수신된 비콘 주소, rssi 만 저장 #큐를 비운다.* <---- 이거 다시 생각해보기

    maclist = []
    returnedList = blescan.parse_events(sock, 10) ### **blescan.py의 def parse_events(sock, loop_count=100): 루프 조정해서 뭔지 확인하기**
    print("----------")
    for beacon in returnedList:
        print(beacon)
        now_mac = beacon[:17]
        now_rssi = beacon[66:] # * rssi  '-' 가 붙거나 붙지 않을 수 있음 *


        for x in top3_list:
            maclist.append(x.getMAC()) ## !!


        if (now_mac in maclist) and (top3_list[maclist.index(now_mac)].getRSSI() < now_rssi):#1. 중복이지만 새로 측정된 rssi가 더 크면 큐에 추가
                if len(top3_list) <3:
                    top3_list[maclist.index(now_mac)].RSSI = now_rssi #동일한 비콘의 RSSI를 수정한다.
                    top3_list.sort(key= lambda x : x.getRSSI())
                else:
                    #3개가 꽉 찼음을 발견했을 때
                    top3_list[maclist.index(now_mac)].RSSI = now_rssi #동일한 비콘의 RSSI를 수정한다.
                    top3_list.sort(key= lambda x : x.getRSSI())
                    try:
                        locationX, locationY = getTrilateration()
                    except:
                        print("비었음/ 연산 불가")

        elif (now_mac not in maclist): #2. 중복된 기기가 아니면 추가
                    #이하 코드 같음
                if len(top3_list) <3:
                    top3_list.append(Beacon(now_mac, now_rssi)) #리스트에 추가
                    top3_list.sort(key= lambda x : x.getRSSI()) #* vscode에서 getter가 안읽혀서 걱정....;; but 같은 조건에서 다 해봤는데 다른 코드는 잘 읽혀서 그냥 vscode 문제인듯*
                else: #큐 동작
                    top3_list[0] = Beacon(now_mac, now_rssi)  #rssi가 가장 작은 비콘을 삭제하고 추가
                    top3_list.sort(key= lambda x : x.getRSSI())
                    try:
                        locationX, locationY = getTrilateration() #삼변측량 결과
                    except:
                        print("비었음/ 연산 불가")
       