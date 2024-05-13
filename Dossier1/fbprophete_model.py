# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:21:50 2023

@author: ABDOULAHI FAYE
"""
#python
# *********************************************model facebook prophet ************************************************************
#********************************************* importation des modules************************************************************
import pandas as pd
import prophet import Prophet
import plotly.express as px
#**********************************************importation de la base de donnees***************************************************

df=pd.read_excel('basedonnees.xlsx',index_col=[0],parse_dates=True)
print(df.head())
TC=pd.DataFrame(df['Température module (°C)'])
print(TC.plot())
m=pr.Prophet()
m.fit()
future=m.make_future_dataframe(periods=365)
forecast=m.predict(future)
print(forecast)