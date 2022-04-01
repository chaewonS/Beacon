
# -*- coding: utf-8 -*-
# from easy_trilateration.model import *  
# from easy_trilateration.least_squares import easy_least_squares  
# from easy_trilateration.graph import *  

import io

import blescan
import sys
import bluetooth._bluetooth as bluez
import json
#from tkinter import*
import Tkinter
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

global top3_list


top3_list =[Beacon('00:19:01:70:81:d0','-100'),Beacon('00:19:01:70:81:75','-100'),Beacon('00:19:01:70:86:35','-100')]


dev_id = 0#scan

#========================================== Definition Of Functions ==================================
def flusshing():
    print("Timer")
    timer = threading.Timer(5, flusshing)


    global top3_list
    top3_list =[Beacon('00:19:01:70:81:d0','-100'),Beacon('00:19:01:70:81:75','-100'),Beacon('00:19:01:70:86:35','-100')]

    timer.start()

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
    #return 10 ** ((TxPower - rssi )/(10*4)) # 4 = n : 실내공간
    return (TxPower - rssi) / (10*4)

def getTrilateration(first, second, third):
    # print("호출")
    x1, y1 = first.getXY()
    x2, y2 = second.getXY()
    x3, y3 = third.getXY()

    # 1 :
    r1 = calculateDistance(first.getRSSI())
    r2 = calculateDistance(second.getRSSI())
    r3 = calculateDistance(third.getRSSI())
    print("==============실제 거리와 비교해보기========================")
    print("distances : r1 =%f r2=%f r3=%f" %(r1, r2, r3)) #use old formatstring to run it with python 2.7
    
    
    # 2 :
    # r1 = simpleDistance(first.getRSSI())
    # r2 = simpleDistance(second.getRSSI())
    # r3 = simpleDistance(third.getRSSI())
    # print("==============실제 거리와 비교해보기===(심플)=====================")
    # print("distances : r1 =%f r2=%f r3=%f" %(r1, r2, r3))

    S = (x3**2 - x2**2 + y3**2 - y2**2 + r2**2 - r3**2 )/2.0
    T = (x1**2 - x2**2 + y1**2 + y2**2 + r2**2 - r1**2)/2.0

    y = (  ((T*(x2-x3))) - (S *(x2-x1))  ) / (  ((y1-y2)*(x2-x3)) -  ((y3-y2)*(x2-x1)) )
    x = ((y* (y1-y2)) - T) /(x2-x1)
    # arr = [Circle(x1,y1, float(first.getRSSI())),    #(x,y,r)
    # Circle(x2,y2, float(second.getRSSI())),
    # Circle(x3,y3, float(third.getRSSI()))]
    # # Circle(8,2, float(math.sqrt(17)))         # 4 beacon 으로 하면 정확도 up

    # result, meta = easy_least_squares(arr)
    # create_circle(result, target=True)
    
    # # 값 추출
    # re = str(result)
    # re = re.replace("Circle(","").replace(")","").replace(",","")
    # x,y,r = re.split(" ")
    return x,y
global a

def showposition():
    global a
    canvas.delete(a)
    global x
    global y
    a = canvas.create_rectangle(SP_w +(x-1)*column, SP_h+(y-1)*row, SP_w+x*column,SP_h+y*row,fill="yellow")
    canvas.after(1000, showposition)



#================== Select three ==================================

if __name__ == '__main__':
    global x
    global y
    x=1
    y=1
    #====init========
    locationX = -100
    locationY = -100
    flusshing()
    master = Tkinter.Tk()
    width = 1080
    height = 650
    #label = Label(master, text="placeholder").pack()
    canvas = Tkinter.Canvas(master, width=width, height=height)

    rectanglesize = 7
    rows = range(1,rectanglesize)
    columns = range(1, rectanglesize)
    SP_w = 215 #1080-650/2
    SP_h = 10 #StartPoint
    polygon = canvas.create_rectangle(SP_w,SP_h, width-SP_w,height-SP_h)

    row = int((height-SP_h -SP_h)/rectanglesize) # 행 간격

    for i in rows:
        i = canvas.create_line(SP_w, SP_h+row*i, width-SP_w, SP_h+row*i)


    column = int((width-SP_w-SP_w)/rectanglesize) #열 간격
    for i in columns:
        i = canvas.create_line(SP_w+column*i, SP_h, SP_w +column*i, height-SP_h)
    a=canvas.create_rectangle(1,1,2,2)
    showposition()
    canvas.pack()
    canvas.mainloop()
    try:
        sock = bluez.hci_open_dev(dev_id)
        print("ble thread started")

    except:
        print ("error accessing bluetooth device...")
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)



    while True:
        top3_list = [Beacon('00:19:01:70:81:d0','-100'),Beacon('00:19:01:70:81:75','-100'),Beacon('00:19:01:70:86:35','-100')] 

        maclist = []
        returnedList = blescan.parse_events(sock, 10)
        print("----------")
        
        for beacon in returnedList:

            if beacon[:5] == "00:19":
                print(beacon)
                
                now_mac = beacon[:17]
                now_rssi = beacon[66:] 

                maclist =[]
                for x in top3_list:
                    maclist.append(x.getMAC())

                if (now_mac in maclist) and (top3_list[maclist.index(now_mac)].getRSSI() < now_rssi):#1. 리스트에 이미 있는 비콘이며, 더 가까워진 경우.
                    if len(top3_list) <3:
                        top3_list[maclist.index(now_mac)].RSSI = now_rssi
                        top3_list.sort(key= lambda x : x.getRSSI())
                    else:
                    #3개가 꽉 찼음을 발견했을 때
                        top3_list[maclist.index(now_mac)].RSSI = now_rssi #동일한 비콘의 RSSI를 수정한다.
                        top3_list.sort(key= lambda x : x.getRSSI())
                    try:
                        locationX, locationY = getTrilateration(top3_list[0], top3_list[1], top3_list[2])
                    except:
                        print("비었음/ 연산 불가 duplicated.")

                elif (now_mac not in maclist): #2. 중복된 기기가 아니면 추가
                    #이하 코드 같음
                    if len(top3_list) <3:
                        top3_list.append(Beacon(now_mac, now_rssi)) #리스트에 추가
                        top3_list.sort(key= lambda x : x.getRSSI())
                    else: #큐 동작
                        top3_list[0] = Beacon(now_mac, now_rssi)  #rssi가 가장 작은 비콘을 삭제하고 추가
                        top3_list.sort(key= lambda x : x.getRSSI())
                    try:
                        locationX, locationY = getTrilateration(top3_list[0], top3_list[1], top3_list[2]) #삼변측량 결과
                    except:
                        print("비었음/ 연산 불가 no duplicated.")
        #print(locationX, locationY)
        x=int(locationX)
        y=int(locationY)
        print(x,y)

