# -*- coding: utf-8 -*-
import io
import json
 
Beacon = dict()

init1 = dict()
init1["location"] = "-1, -1"
init1["place"] = "초기화1"
init1["group"] = "-1"
Beacon["init1"] = init1

init2 = dict()
init2["location"] = "-1, -1"
init2["place"] = "초기화2"
init2["group"] = "-1"
Beacon["init2"] = init2

beacon1 = dict()

beacon1["location"] = "1,1"
beacon1["place"] = "좌상단"
beacon1["group"] = "0"
Beacon["00:19:01:70:81:ed"] = beacon1

beacon2 = dict()
beacon2["location"] = "7,0"
beacon2["place"] = "우상단"
beacon2["group"] = "0"
Beacon["00:19:01:70:82:62"] = beacon2

beacon3 = dict()
beacon3["location"] = "0,7"
beacon3["place"] = "좌하단"
beacon3["group"] = "1"
Beacon["00:19:01:70:85:c3"] = beacon3

beacon4 = dict()
beacon4["location"] = "7,7"
beacon4["place"] = "우하단"
beacon4["group"] = "1"
Beacon["00:19:01:70:82:cb"] = beacon4

beacon5 = dict()
beacon5["location"] = "0,0"
beacon5["place"] = "복도"
beacon5["group"] = "2"
Beacon["00:19:01:70:86:03"] = beacon5

beacon6 = dict()
beacon6["location"] = "0,0"
beacon6["place"] = "복도"
beacon6["group"] = "2"
Beacon["00:19:01:70:81:9d"] = beacon6

beacon7 = dict()
beacon7["location"] = "0,0"
beacon7["place"] = "복도"
beacon7["group"] = "3"
Beacon["00:19:01:70:86:2f"] = beacon7

beacon8 = dict()
beacon8["location"] = "0,0"
beacon8["place"] = "복도"
beacon8["group"] = "3"
Beacon["00:19:01:70:84:4b"] = beacon8


beacon9 = dict()
beacon9["location"] = "21,51"
beacon9["place"] = "9"
beacon9["group"] = "4"
Beacon["00:19:01:70:81:d0"] = beacon9#

beacon10 = dict()
beacon10["location"] = "31,51"
beacon10["place"] = "10"
beacon10["group"] = "4"
Beacon["00:19:01:70:81:75"] = beacon10#

beacon11 = dict()
beacon11["location"] = "51,51"
beacon11["place"] = "11"
beacon11["group"] = "5"
Beacon["00:19:01:70:86:35"] = beacon11#

beacon12 = dict()
beacon12["location"] = "41,1"
beacon12["place"] = "12"
beacon12["group"] = "5"
Beacon["00:19:01:70:81:33"] = beacon12#

beacon13 = dict()
beacon13["location"] = "41,16"
beacon13["place"] = "13"
beacon13["group"] = "6"
Beacon['00:19:01:70:82:af'] = beacon13

beacon14 = dict()
beacon14["location"] = "41,51"
beacon14["place"] = "14"
beacon14["group"] = "6"
Beacon['00:19:01:70:82:d7'] = beacon14
#========
beacon15 = dict()
beacon15["location"] = "41,51"
beacon15["place"] = "15"
beacon15["group"] = "7"
Beacon['00:19:01:70:85:95'] = beacon15

beacon16 = dict()
beacon16["location"] = "-1,-1"
beacon16["place"] = "16"
beacon16["group"] = "7"
Beacon['00:19:01:70:80:d9'] = beacon16
with io.open('./beacon.json', 'wb',
# encoding='utf-8'
)as make_file:
    json.dump(Beacon, make_file)
print("위치 좌표 파일이 현재 위치에 'beacon.json'으로 갱신되었습니다.")
