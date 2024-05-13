# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 00:02:58 2023

@author: LENOVO
"""

#**************************prediction de la temperatiure********************************************************
#************************* importation des modules *************************************************************
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from scipy.interpolate import interp1d
donnees=pd.read_excel('Donnees Bokhol.xlsx') #,index_col='',parse_dates=True)
donnees.fillna(donnees['Temperature_module'].mean())
print('la taille des donnees:',donnees.shape)
print(donnees.columns)
print(donnees['Irradiance'])
#********************************indexation des colonnes********************************************************
irradiance=donnees['Irradiance']
T_ambiante=donnees['Temperature_ambiante']
V_vent=donnees['Vitesse_du_vent']
T_module=donnees['Temperature_module']
production_PV=donnees['Production_Centrale']
#******************************* visualisatioin des donnees********************************************************

plt.figure()
plt.subplot(3,2,1) #********************************
plt.plot(irradiance,c='g')
plt.xlabel('temps')
plt.ylabel('IRRADIANCE')
plt.subplot(3,2,2) #************************************
plt.plot(T_ambiante,c='y')
plt.xlabel('temps')
plt.ylabel('T_ambiante')
plt.subplot(3,2,3) # ************************************
plt.plot(T_module,c='r')
plt.xlabel('temps')
plt.ylabel('T_MODULE')
plt.subplot(3,2,4) # **********************************
plt.plot(production_PV,c='k')
plt.xlabel('temps')
plt.ylabel('PROD PV ')
plt.subplot(3,2,5) # **********************************
plt.plot(V_vent,c='b')
plt.xlabel('temps')
plt.ylabel('V_vent')
#**************************************************** PREDICTION **********************************************************



