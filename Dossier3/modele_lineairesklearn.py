# -*- coding: utf-8 -*-
#********************************************************************************************
# importation des modules
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import SGDRegressor
#************************************************************************************************
# dataset
x,y= make_regression(n_samples=100,n_features=1,noise=10)
# le modele d'etude **********************************************************************
modele=SGDRegressor(max_iter=1000,eta0=0.01)
modele.fit(x,y) # pour entrainer votre modèle
print("Coeff R^2=",modele.score(x,y)) # pour évaluer votre modèle
plt.scatter(x,y)
      
plt.plot(x,modele.predict(x),c='r',lw=3)# pour générer des prédictions
