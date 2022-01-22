# -*- coding: utf-8 -*-
import json

Beacon = dict()

beacon1 = dict()

beacon1["location"] = "0,0"
beacon1["place"] = "좌상단"
Beacon["00:19:01:70:81:ed"] = beacon1

beacon2 = dict()
beacon2["location"] = "8,0"
beacon2["place"] = "우상단"
Beacon["00:19:01:70:85:95"] = beacon2

beacon3 = dict()
beacon3["location"] = "0,14"
beacon3["place"] = "좌하단"
Beacon["00:19:01:70:85:c3"] = beacon3

beacon4 = dict()
beacon4["location"] = "8,14"
beacon4["place"] = "우하단"
Beacon["00:19:01:70:84:4b"] = beacon4


with open('./test.json', 'w', encoding='utf-8')as make_file:
    json.dump(Beacon, make_file)

print("위치 좌표 파일이 현재 위치에 'test.json'으로 갱신되었습니다.")
