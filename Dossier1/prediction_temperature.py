# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 01:54:33 2023

@author: LENOVO
"""

#***************************************AUTOREGRESSIVE MODEL ******************************************************************
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.regression.linear_model import yule_walker
from statsmodels.tsa.stattools import adfuller,acf
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#**************************** projet *********************************************************************************************
feuil=pd.read_csv('base.csv',index_col=[0],parse_dates=True,squeeze=True)
p_value= range(0,5)
d_value=range(0,3)
q_value=range(0,5)
for p in p_value:
    for d in d_value:
        for q in q_value:
            ordre=(p,d,q)
            train,test=feuil[0:761],feuil[762:feuil.shape[0]]
            prediction=[]
            for i in range(len(test)):
                try:
                    model=ARIMA(train,ordre)
                    model_fit=model.fit()
                    pred_y=model_fit.forecast()
                    prediction.append(pred_y)
                    #error=mean_squared_error(test,prediction)
                except:
                    continue
                
                
plt.plot(prediction)
                    
                        
