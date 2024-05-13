# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:57:47 2023

@author: ABDOULAHI FAYE
"""

#***************************************DEVELEPPEMENT D'UN MODELE arima de prediction de la temperature*******************************************************
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.regression.linear_model import yule_walker
from statsmodels.tsa.stattools import adfuller,acf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from pmdarima import auto_arima
#************************************* IMPORTATION DE LA BASE DE DONNEES*********************************************************************************************
df=pd.read_excel('basedonnees.xlsx',index_col=[0],parse_dates=True)
#*********************************** selection de la temperature du module ****************************************************************************************
def traitement(dateset):#######################################################################################
    TMP=pd.DataFrame(dateset)
    TC=TMP.dropna(axis=0) # traitement de donnees manquantes
    return TC
def representation(TC,labele,axesx,axesy,titre):##################################################################################################################
    plt.plot(TC,label=labele)
    plt.xlabel(axesx)
    plt.ylabel(axesy)
    plt.title(titre)
    plt.legend()
#################################################stablite de la series temporelle################################################################################################
def adfuller_test(sales):
    result=adfuller(sales)
    label=['ADF test statistic','p_value','lages used','nombres d''observation']
    for value,label in zip(result,label):
        print(label+':'+str(value))
        if result[1]<=0.05:
            print('strong evident agains the null hypothesis ...')
        else:
            print('weak evidence agains null hypothesis...')
###########################################################################################################################################################################"""""""


def ARIMAmodel(traitement,ordre,lenpred):#####################################################################################
    TC_train=traitement.iloc[:-lenpred]
    TC_test=traitement.iloc[-lenpred:]
    longueur=TC_test.shape[0]
    model=ARIMA(TC_train,order=ordre)
    model_fit=model.fit()
    prediction=model_fit.forecast(steps=longueur)
    donnees_futures=pd.date_range(traitement.index[-1],periods=TC_test.shape[0],freq='00h05t')
    prediction.index=donnees_futures
    return prediction,TC_test
def Evaluation(prediction,TC_test):###################################################################################"""""""""""""""""
    mean_pred=prediction.mean()
    somme=abs(sum(TC_test-mean_pred))
    T=1/len(prediction)
    RMSE=mean_squared_error(prediction,TC_test) # evaluation a court terme
    MAPE=T*somme #il mesure l'ajustement du systeme 10 % EST ACCEPTABLE
    R2=r2_score(prediction,TC_test)
    print('performance a court terme:',RMSE)
    print('performance PAR rapport a 10%:',MAPE)
    print('COEFFICIENT DE CORRELATION:',R2)
def Stimation_ARIMA(TC,ordre):
    model=ARIMA(TC,order=ordre)
    model_fitt=model.fit()
    TC['prevision']=model_fitt.predict()
    return TC    
###################################################### utilisation des fonctions#############################################################################
###################################################### representation ##########################################################################################""
Temperature=traitement(df['Température module (°C)'])
plt.figure(1,figsize=(12,5))
plt.subplot(3,2,1)
representation(Temperature,'temperature module','date','temperature','evolution de la temperature module')
###################################################### MODEL D'ESTIMATION#########################################################
stimation=Stimation_ARIMA(Temperature,(2,1,4))
plt.subplot( 3,1,2 )
plt.plot(stimation,c='r')
prediction,donnees_test= ARIMAmodel(Temperature['Température module (°C)'],(2,1,4),12) 
plt.subplot(2,1,3)
plt.plot(donnees_test,c='yellow')
plt.plot(prediction,c='r')
#################################################### EVATUATION DE MODELE ##############################################################################################
print(Evaluation(prediction,donnees_test))

