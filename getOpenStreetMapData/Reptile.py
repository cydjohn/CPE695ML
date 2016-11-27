#coding = utf-8

import re
import os
import csv
import time
import urllib.request

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

def process(file_name):
    print(file_name)
    poi_file = open('CSVFile/'+ file_name +'', 'r')
    data = []
    for line in poi_file:
        data.append(list(line.strip().split(',')))
    data.pop(0)
    for line in data:
        i_user_id = line[1]
        i_time = line[2]
        i_longitude = float(line[3])
        i_latitude = float(line[4])
        info = getinfo(i_user_id, i_time, i_longitude, i_latitude)
        with open('Out/'+ file_name +'', 'a+', encoding='utf8', newline='') as datacsv:
            csvwriter = csv.writer(datacsv, dialect='excel')
            csvwriter.writerow(info)
        time.sleep(1)

def getinfo(user_id, time, longitude, latitude):
    longitude = "%.8f"%longitude
    latitude = "%.8f"%latitude
    url = 'http://nominatim.openstreetmap.org/search.php?q='+ longitude +'%2C+'+ latitude +'&polygon=1&viewbox='
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    #print(html.decode("utf8"))
    response.close()
    poi_osm_id = re.findall(b"\"osm_id\":\s\"(\w+)\",", html)
    poi_class = re.findall(b"\"class\":\s\"(\w+)\",", html)
    poi_type = re.findall(b"\"type\":\s\"(.*)\",", html)
    poi_placename = re.findall(b"\"placename\":\s\"(.*)\",", html)
    poi_langaddress = re.findall(b"\"langaddress\":\s\"(.*)\",", html)
    if not poi_placename:
        poi_placename.append(b'null')
    #print(poi_osm_id, poi_class, poi_type, poi_placename, poi_langaddress)
    poi = [user_id, time, longitude, latitude, int(poi_osm_id[0]), str(poi_class[0])[2:-1], str(poi_type[0])[2:-1], str(poi_placename[0])[2:-1], str(poi_langaddress[0])[2:-1]]
    print(poi)
    return poi

if __name__ == "__main__":
    filename = file_name('CSVFile/')
    for names in filename:
        if names == '.DS_Store':
            pass
        else:
            with open('Out/'+ names +'', 'w', encoding='utf8', newline='') as datacsv:
                csvwriter = csv.writer(datacsv, dialect='excel')
                csvwriter.writerow(['userid', 'time', 'longitude', 'latitude', 'osm_id', 'class', 'type', 'placename', 'address'])
            process(names)
            time.sleep(15)
