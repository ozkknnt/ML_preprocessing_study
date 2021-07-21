import pandas as pd
from pandas import DataFrame

attri_data1 = {"ID": ["100", "101", "102", "103", "104", "106", "108", "110", "111", "113"]
        ,"city": ["Tokyo", "Osaka", "Kyoto", "Hokkaido", "Tokyo", "Tokyo", "Osaka", "Kyoto", "Hokkaido", "Tokyo"]
        ,"birth_year" :[1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981]
        ,"name" :["Hiroshi", "Akiko", "Yuki", "Satoru", "Steeve", "Mituru", "Aoi", "Tarou", "Suguru", "Mitsuo"]}
attri_data_frame1 = DataFrame(attri_data1)

city_map = {"Tokyo":"east"
          ,"Hokkaido":"east"
          ,"Osaka":"west"
          ,"Kyoto":"west"}

#DataFrameattri_data1のcityをキーに上で作成した辞書を参照して新しい列WEを追加し、その結果を出力
attri_data_frame1["WE"] = attri_data_frame1["city"].map(city_map)

attri_data_frame1