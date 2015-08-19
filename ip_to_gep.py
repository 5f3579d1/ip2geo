#!env python
import requests 
import json

fin = open('ip.txt', 'r')
locations = [];
for line in fin:
    split = line.split()
    r = requests.get('http://api.map.baidu.com/location/ip?ak=McLRH4uGcoa99hwKf9Y97y1b&coor=bd09ll&ip='+ split[0])
    info = r.json()
    p = info['content']['point']
    exist = False
    index = 0
    for i, msg in enumerate(locations):
        point = msg['content']['point']
        if(point['x'] == p['x'] and point['y'] == p['y']):
           exist = True
           index = i
    if(exist):
        locations[i]['count'] = int(locations[i]['count']) + int(split[1])
    else:
        info['count'] = split[1]
        locations.append(info)

with open('geo.json', 'w') as f:
     json.dump(locations, f)

fin.close()
