# -*- coding: utf-8 -*-
import io
import json

Beacon = dict()

beacon1 = dict()
beacon1["location"] = "1,1"
beacon1["place"] = "좌상단"
beacon1["group"] = "1"
Beacon["00:19:01:70:81:4e"] = beacon1

beacon2 = dict()
beacon2["location"] = "1,1"
beacon2["place"] = "좌상단"
beacon2["group"] = "1"
Beacon["00:19:01:70:85:ed"] = beacon2




beacon3 = dict()
beacon3["location"] = "1,1"
beacon3["place"] = "좌상단"
beacon3["group"] = "2"
Beacon["00:19:01:70:80:d9"] = beacon3

beacon4 = dict()
beacon4["location"] = "1,1"
beacon4["place"] = "좌상단"
beacon4["group"] = "2"
Beacon["00:19:01:70:84:4b"] = beacon4




beacon5 = dict()
beacon5["location"] = "1,1"
beacon5["place"] = "좌상단"
beacon5["group"] = "3"
Beacon["00:19:01:70:82:cb"] = beacon5

beacon6 = dict()
beacon6["location"] = "1,1"
beacon6["place"] = "좌상단"
beacon6["group"] = "3"
Beacon["00:19:01:70:86:2e"] = beacon6




beacon7 = dict()
beacon7["location"] = "1,1"
beacon7["place"] = "좌상단"
beacon7["group"] = "4"
Beacon["00:19:01:70:85:0f"] = beacon7

beacon8 = dict()
beacon8["location"] = "1,1"
beacon8["place"] = "좌상단"
beacon8["group"] = "4"
Beacon["00:19:01:70:86:35"] = beacon8





beacon9 = dict()
beacon9["location"] = "1,1"
beacon9["place"] = "좌상단"
beacon9["group"] = "5"
Beacon["00:19:01:70:82:af"] = beacon9

beacon10 = dict()
beacon10["location"] = "1,1"
beacon10["place"] = "좌상단"
beacon10["group"] = "5"
Beacon["00:19:01:70:81:33"] = beacon10




beacon11 = dict()
beacon11["location"] = "1,1"
beacon11["place"] = "좌상단"
beacon11["group"] = "6"
Beacon["00:19:01:70:80:de"] = beacon11

beacon12 = dict()
beacon12["location"] = "1,1"
beacon12["place"] = "좌상단"
beacon12["group"] = "6"
Beacon["00:19:01:70:81:75"] = beacon12



beacon13 = dict()
beacon13["location"] = "1,1"
beacon13["place"] = "좌상단"
beacon13["group"] = "6"
Beacon["00:19:01:70:85:95"] = beacon13

with io.open('./pair.json', 'wb',
# encoding='utf-8'
)as make_file:
    json.dump(Beacon, make_file)
print("위치 좌표 파일이 현재 위치에 'pair.json'으로 갱신되었습니다.")
