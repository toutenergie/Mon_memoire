# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 00:08:10 2023

@author: LENOVO
"""

#***************************************AUTOREGRESSIVE MODEL ******************************************************************
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.regression.linear_model import yule_walker
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#************************************model test************************************************************************************
#plt.rcParams['figure.figsize']=(10,7.5)
#*********************************** simulation du model AR(2)*********************************************************************
# y(t)=0.33y(t-1)+0.5y(t-2)
ar2=np.array([1,0.33,0.5])
ma2=np.array([1,0,0])
AR2_process=ArmaProcess(ar2,ma2).generate_sample(nsample=1000)
plt.plot(AR2_process)
rho,sigma=yule_walker(AR2_process,2,method='mle')
print(f'rho : {-rho}')
print(f'sigma: {sigma}')
plot_acf(AR2_process)
plot_pacf(AR2_process)