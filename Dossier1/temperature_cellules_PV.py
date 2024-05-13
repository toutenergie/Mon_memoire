# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#**************************prediction de la temperatiure*********************************
#************************* importation des modules ***********************************************************************
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from scipy.interpolate import interp1d
#********************************declaration des variables ****************************************************************
donnees=pd.read_excel('Donnees Bokhol.xlsx') #,index_col='',parse_dates=True)
donnees.fillna(donnees['Temperature_module'].mean())
G=donnees['Irradiance']
Ta=donnees['Temperature_ambiante']
#Ta=np.array([20.7,20.7,21,21.4,22.8,25.6,27.1,27.4,27.6,27.6,25.8,23.4])
#G=np.array([4.84,5.8,6.57,6.92,6.71,6.21,5.6,5.34,5.34,5.53,4.98,4.57])
Tonc=25
print(Ta.shape)
print(G.shape)
TC=np.ones(len(G))
for i in range(len(G)):
    TC[i]=Ta[i]+(G[i]/800)*(Tonc-20)

plt.figure()
plt.plot(TC,label='TCpv theorique',c='r',lw='3',ls='--')
plt.title('EVOLUTION DE LA TEMPERATURE D''UNE CELLULE PV')
plt.xlabel('MOIS')
plt.ylabel('TCpv(temperature des cellules)')
plt.legend()
print(TC.shape)
#************************* modeles de prediction TC***********************************************************************
X=np.array([Ta,G,np.ones(len(G))]) 
L=X.dot(X.T)
U=X.dot(TC)
A=np.linalg.inv(L) # np.linalg.inv(A) l'inverse d'une matrice
O=A.dot(U) 
predict=O[0]*Ta+O[1]*G +O[2]
#************************************ affichage du modele ***************************************************************
plt.plot(predict,c='b',label='TCpv PREDITE')
plt.plot(donnees['Temperature_module'],c='k',label='TCpv reelle')
plt.legend()