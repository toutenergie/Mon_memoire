# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:12:18 2023

@author: LENOVO
"""

#***************************** utilisation de DT AVEC k**********************************************
# TC=Tamb+KG
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#********************************de claration des variables ****************************
temperature=np.array([20.7,20.7,21,21.4,22.8,25.6,27.1,27.4,27.6,27.6,25.8,23.4])
G=np.array([4.84,5.8,6.57,6.92,6.71,6.21,5.6,5.34,5.34,5.53,4.98,4.57])
#******************************* verivification de dimension*********************************************
print(temperature.shape)
print(G.shape)
#************************************* TC=Tamb+kG **************************************************
k=np.array([0.02,0.0208,0.026,0.0342,0.0455]) #,0.0538,0.0563])
couleur=['r','b','y','g','k']
titre=['TCpv k=0.02','TCpv k=0.0208','TCpv k=0.026','TCpv k=0.0342','TCpv k=0.0455']
print(k.shape)
TC=np.zeros(len(G))
for i,l in enumerate(k):
    m=couleur[i]
    n=titre[i]
    for j in range(len(G)):
        TC[j]=temperature[j]+l*G[j] 
        
    plt.plot(TC,label=n,c=m,lw='3',ls='--')
    plt.xlabel('MOIS')
    plt.ylabel('TC')
    plt.legend()
