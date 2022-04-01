# -*- coding: utf-8 -*-
import io
import json

Beacon = dict()

beacon1 = dict()

beacon1["location"] = "1,1"
beacon1["place"] = "1"
Beacon["00:19:01:70:81:ed"] = beacon1

beacon2 = dict()
beacon2["location"] = "1,15"
beacon2["place"] = "4"
Beacon["00:19:01:70:82:62"] = beacon2#

beacon3 = dict()
beacon3["location"] = "0,7"
beacon3["place"] = "좌하단"
Beacon["00:19:01:70:85:c3"] = beacon3

beacon4 = dict()
beacon4["location"] = "1,30"
beacon4["place"] = "7"
Beacon["00:19:01:70:82:cb"] = beacon4#

beacon5 = dict()
beacon5["location"] = "15,1"
beacon5["place"] = "2"
Beacon["00:19:01:70:86:03"] = beacon5#

beacon6 = dict()
beacon6["location"] = "0,0"
beacon6["place"] = "복도"
Beacon["00:19:01:70:81:9d"] = beacon6

beacon7 = dict()
beacon7["location"] = "0,0"
beacon7["place"] = "복도"
Beacon["00:19:01:70:86:2f"] = beacon7

beacon8 = dict()
beacon8["location"] = "0,0"
beacon8["place"] = "복도"
Beacon["00:19:01:70:84:4b"] = beacon8

beacon9 = dict()
beacon9["location"] = "30,1"
beacon9["place"] = "3"
Beacon["00:19:01:70:81:d0"] = beacon9#

beacon10 = dict()
beacon10["location"] = "30,15"
beacon10["place"] = "6"
Beacon["00:19:01:70:81:75"] = beacon10#

beacon11 = dict()
beacon11["location"] = "30,30"
beacon11["place"] = "9"
Beacon["00:19:01:70:86:35"] = beacon11#

beacon12 = dict()
beacon12["location"] = "15,30"
beacon12["place"] = "8"
Beacon["00:19:01:70:81:33"] = beacon12#

beacon13 = dict()
beacon13["location"] = "8,1"
beacon13["place"] = "22"
Beacon['00:19:01:70:82:af'] = beacon13

beacon14 = dict()
beacon14["location"] = "23,1"
beacon14["place"] = "33"
Beacon['00:19:01:70:82:d7'] = beacon14
#========
beacon14 = dict()
beacon14["location"] = "8,30"
beacon14["place"] = "77"
Beacon['00:19:01:70:85:95'] = beacon14

beacon14 = dict()
beacon14["location"] = "23,30"
beacon14["place"] = "99"
Beacon['00:19:01:70:80:d9'] = beacon14

beacon01 = dict()
beacon01["location"] = "-1,-1"
beacon01["place"] = "초기화A"
Beacon["A"] = beacon01

beacon02 = dict()
beacon02["location"] = "-1,-1"
beacon02["place"] = "초기화B"
Beacon["B"] = beacon02

beacon03 = dict()
beacon03["location"] = "-1,-1"
beacon03["place"] = "초기화C"
Beacon["C"] = beacon03
#'''

with io.open('./test.json', 'wb',
# encoding='utf-8'
)as make_file:
    json.dump(Beacon, make_file)
print("위치 좌표 파일이 현재 위치에 'test.json'으로 갱신되었습니다.")
