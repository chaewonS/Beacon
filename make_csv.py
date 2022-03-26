# -*- coding: utf-8 -*-
#make csv for ML

# import io
import blescan
import bluetooth._bluetooth as bluez
import csv


distance = 0.1# 측정 시작 거리
with open('distance_RSSI.csv', 'wb') as f:
    w=csv.writer(f)
    w.writerow(['MACaddress','Distance','RSSI'])
    dev_id = 0
    try:
            sock = bluez.hci_open_dev(dev_id)
            print "ble thread started"

    except:
            print "error accessing bluetooth device..."
            sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)

    for i in range(30):
        maden = 0 #각 반복마다 작성된 신호의 수
        while maden <5000:
            returnedList = blescan.parse_events(sock, 10)
            print "----------"
            for beacon in returnedList:
                #if beacon[:17] == '00:19:01:70:81:': #특정 비콘을 선택해서 출력
                if beacon[:5] =='00:19':
                        print beacon
                        print str(distance) + "거리에서 " + str(maden) +"개의 신호가 작성되는 중..."
                        rssi = beacon[66:]
                        data = (str(beacon[:17])+" "+str(distance)+" "+ str(rssi)).split(" ")
                        if(data.__len__() is 2):#오류 없이 됐을 때만 반복 체크 및 해당 데이터 작성
                            maden += 1
                            w.writerow(data)

        raw_input("비콘의 거리를 10cm 멀리 조정해주세요. <완료시 Enter>")
        distance += 0.1
        print("거리"+ str(distance) +"(으)로 측정을 시작합니다.")
