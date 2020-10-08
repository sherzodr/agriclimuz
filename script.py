#!/usr/bin/env python
# coding: utf-8

<<<<<<< HEAD
# @author: sherzodr@gmail.com

# # Ўзбекистонда Эвапотранспирация

# In[1]:
=======
# # Ўзбекистонда Эвапотранспирация

# In[ ]:
>>>>>>> 7ff8a74470d67949566b7e8e300441cd50fdf32a


import pandas, glob, penmon.eto as pm

<<<<<<< HEAD
SOURCE_DIR="data/sourcedata2/"
OUTPUT_DIR="data/"

pm.CHECK_RADIATION_RANGE=False

def calculate_eto(col):
    
    try:
        day = pm.Station(col["latitude"], col["altitude"], anemometer_height=10).get_day(col["date"].strftime("%Y-%m-%d"),
                         temp_min=round(col["temp_min"], 1),
                         temp_max=round(col["temp_max"], 1),
                         wind_speed=round(col["wind_speed"],1),
                         humidity_mean=round(col["humidity_mean"] * 100, 1),
                         radiation_s=round(col["solar_radiation"], 1))
        return day.eto()
    except:
        raise Exception("Exception raised while processing line:\n" + str(col))

count = 0
dataframes=[]
all_csv_files = glob.glob(SOURCE_DIR+"*.csv")

=======
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
>>>>>>> 7ff8a74470d67949566b7e8e300441cd50fdf32a
for csv_file in all_csv_files:
    df = pandas.read_csv(csv_file, header=0,
                         names=["date", "longitude", "latitude", "altitude", "temp_max",
                               "temp_min", "precip", "wind_speed","humidity_mean", "solar_radiation", None], 
                        parse_dates=[0], index_col=None)
<<<<<<< HEAD
    
    df["eto"] = df.apply(calculate_eto, axis=1)
    dataframes.append(df)
    
    #path=csv_file.split('\\')
    #df.to_csv(OUTPUT_DIR+"eto"+path[1], index=False, 
    #         columns=["date", "latitude", "longitude", "altitude", "temp_min", "temp_max",
    #                "wind_speed", "humidity_mean", "solar_radiation", "eto"])
    count += 1
print("Processed ", count, "files")

df=pandas.concat(dataframes)
df.to_csv(OUTPUT_DIR+"eto.csv", index=False, columns=["date", "latitude", "longitude", "altitude", "temp_min", "temp_max",
                      "wind_speed", "humidity_mean", "solar_radiation", "precip", "eto"])

=======
    df["eto"] = df.apply(calculate_eto, axis=1)
    path=csv_file.split('\\')
    df.to_csv("data/etodata/eto"+path[1], index=False, 
              columns=["date", "latitude", "longitude", "altitude", "temp_min", "temp_max",
                      "wind_speed", "humidity_mean", "solar_radiation", "eto"])
    count += 1
print("Processed ", count, "files")

>>>>>>> 7ff8a74470d67949566b7e8e300441cd50fdf32a
