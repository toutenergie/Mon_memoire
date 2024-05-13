# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:14:47 2023

@author: ABDOULAHI FAYE
"""
#************************************** importation des bibiotheque ***************************************************
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.regression.linear_model import yule_walker
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#************************************ developement d'un model *************************************************************
df=pd.read_csv('base.csv')
