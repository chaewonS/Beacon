# -*- coding: utf-8 -*-
import io
import json

Beacon = dict()

beacon1 = dict()

beacon1["location"] = "1,1"
beacon1["place"] = "엘베"
Beacon["00:19:01:70:82:cb"] = beacon1

beacon2 = dict()
beacon2["location"] = "7,0"
beacon2["place"] = "ML401"
Beacon["00:19:01:70:86:2f"] = beacon2

beacon3 = dict()
beacon3["location"] = "0,7"
beacon3["place"] = "ML402"
Beacon["00:19:01:70:84:4b"] = beacon3

beacon4 = dict()
beacon4["location"] = "7,7"
beacon4["place"] = "ML402_corner"
Beacon["00:19:01:70:82:62"] = beacon4

beacon5 = dict()
beacon5["location"] = "0,0"
beacon5["place"] = "ML403_corner"
Beacon["00:19:01:70:85:c3"] = beacon5

beacon6 = dict()
beacon6["location"] = "0,0"
beacon6["place"] = "ML403"
Beacon["00:19:01:70:81:9d"] = beacon6

beacon7 = dict()
beacon7["location"] = "0,0"
beacon7["place"] = "ML416"
Beacon["00:19:01:70:81:ed"] = beacon7

beacon8 = dict()
beacon8["location"] = "0,0"
beacon8["place"] = "ML415"
Beacon["00:19:01:70:86:03"] = beacon8

#아래부턴 선주가 가지고있음 - 3/29
beacon9 = dict()
beacon9["location"] = "1,1"
beacon9["place"] = "좌상단"
Beacon["00:19:01:70:81:D0"] = beacon9

beacon10 = dict()
beacon10["location"] = "7,1"
beacon10["place"] = "우상단"
Beacon["00:19:01:70:81:75"] = beacon10

beacon11 = dict()
beacon11["location"] = "1,7"
beacon11["place"] = "좌하단"
Beacon["00:19:01:70:86:35"] = beacon11

beacon12 = dict()
beacon12["location"] = "7,7"
beacon12["place"] = "우하단"
Beacon["00:19:01:70:81:33"] = beacon12

with io.open('./test.json', 'wb',
# encoding='utf-8'
)as make_file:
    json.dump(Beacon, make_file)
print("위치 좌표 파일이 현재 위치에 'test.json'으로 갱신되었습니다.")
