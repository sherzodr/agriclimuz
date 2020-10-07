#!/usr/bin/env python
# coding: utf-8

# @author: sherzodr@gmail.com

# # Ўзбекистонда Эвапотранспирация

# In[1]:


import pandas, glob, penmon.eto as pm

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

for csv_file in all_csv_files:
    df = pandas.read_csv(csv_file, header=0,
                         names=["date", "longitude", "latitude", "altitude", "temp_max",
                               "temp_min", "precip", "wind_speed","humidity_mean", "solar_radiation", None], 
                        parse_dates=[0], index_col=None)
    
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

