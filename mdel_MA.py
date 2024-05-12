# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 00:46:37 2023

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
#*************************************model test ARMA ****************************************************************************
plt.rcParams['figure.figsize']=(10,7.5)
#************************************* ARMA(p,q) **********************************************************************************
# ********************************** simulation MA(2) PROCESS***********************************************************************
# y(t)=0.9Z(t-1)+0.3Z(t-2)
mar2=np.array([1,0.9,0.3])
ar2=np.array([1,0,0])
MA2_process=ArmaProcess(ar2,mar2).generate_sample(nsample=1000)
MA_model=ARIMA(MA2_process,ordre=(0,0,2),enforce_stationarity=False).fit()
print(MA_model.summary())