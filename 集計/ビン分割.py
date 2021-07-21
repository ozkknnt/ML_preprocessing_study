import pandas as pd
from pandas import DataFrame

attri_data1 = {"ID":[100,101,102,103,104,106,108,110,111,113]
        ,"city":["Tokyo","Osaka","Kyoto","Hokkaido","Tokyo","Tokyo","Osaka","Kyoto","Hokkaido","Tokyo"]
        ,"birth_year":[1990,1989,1992,1997,1982,1991,1988,1990,1995,1981]
        ,"name":["Hiroshi","Akiko","Yuki","Satoru","Steeve","Mituru","Aoi","Tarou","Suguru","Mitsuo"]}
attri_data_frame1 = DataFrame(attri_data1)

pd.cut(attri_data_frame1.ID,2)
