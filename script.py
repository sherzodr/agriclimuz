#!/usr/bin/env python
# coding: utf-8

# # Ўзбекистонда Эвапотранспирация

# In[ ]:


import pandas, glob, penmon.eto as pm

def calculate_eto(col):
    station = pm.Station(col["latitude"], col["altitude"])
    day = station.get_day(col["date"].strftime("%Y-%m-%d"))
    day.temp_min = col["temp_min"]
    day.temp_max = col["temp_max"]
    day.wind_speed=col["wind_speed"]
    day.humidity_mean=round(col["humidity_mean"] * 100, 0)
    day.radiation_s = col["solar_radiation"]
    return day.eto()

all_csv_files = glob.glob("data/sourcedata/*.csv")
count = 0
for csv_file in all_csv_files:
    df = pandas.read_csv(csv_file, header=0,
                         names=["date", "longitude", "latitude", "altitude", "temp_max",
                               "temp_min", "precip", "wind_speed","humidity_mean", "solar_radiation", None], 
                        parse_dates=[0], index_col=None)
    df["eto"] = df.apply(calculate_eto, axis=1)
    path=csv_file.split('\\')
    df.to_csv("data/etodata/eto"+path[1], index=False, 
              columns=["date", "latitude", "longitude", "altitude", "temp_min", "temp_max",
                      "wind_speed", "humidity_mean", "solar_radiation", "eto"])
    count += 1
print("Processed ", count, "files")

