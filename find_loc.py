import pandas as pd
from geopy.geocoders import Nominatim


def find_loc(pos):
    load = Nominatim(user_agent = "South Korea", timeout = None)
    geo = load.geocode(pos)

    if geo == None:
        return

    return geo.latitude, geo.longitude


solar_raw = pd.read_csv("solar_pos.csv", encoding = "cp949")
wind_raw = pd.read_csv("wind_pos.csv", encoding = "cp949")

pos = []
t = []
_data = {}
data = [[], [], []]


for s, k in zip(solar_raw["행정시"], solar_raw["읍면동"]):
    pos.append([f"{s} {k}", "solar"])

for p in wind_raw['설치장소']:
    pos.append([p, "wind"])

for p in pos:
    if p[0] in _data.keys():
        lat = _data[p[0]][0]
        lng = _data[p[0]][1]

    else:
        loc = find_loc(p[0])
        if loc == None: continue
        lat, lng = loc


    _data[p[0]] = [lat, lng]

    data[0].append(p[0])
    data[1].append(lat)
    data[2].append(lng)
    t.append(p[1])


df = pd.DataFrame({'종류': t, '지역': data[0], '위도': data[1], '경도' : data[2]})
df.to_csv("location.csv", encoding = "cp949")
