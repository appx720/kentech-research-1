import folium
import folium.plugins
import pandas as pd

df = pd.read_csv("location.csv", encoding = "cp949")
x, y = df['위도'], df['경도']

m = folium.Map(location = [33.37, 126.5], zoom_start = 11)
mc = folium.plugins.MarkerCluster()

for i in range(len(df)):
    p = [x[i], y[i]]

    if df['종류'][i] == "solar":
        mc.add_child(folium.Marker(location = p, radius = 400, popup = df['지역'], icon = folium.Icon(color = 'red', icon = 'star')))

    else:
        mc.add_child(folium.Marker(location = p, radius = 400, popup = df['지역'], icon = folium.Icon(color = 'blue', icon = 'star')))
    

m.add_child(mc)
m.save("location.html")