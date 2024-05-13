# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
x,y= make_regression(n_samples=100,n_features=1,noise=10)
y=y.reshape(y.shape[0],1)
print(x.shape)
print(y.shape)
plt.figure()
plt.scatter(x,y,c='b',label='datasets')
X=np.hstack((x,np.ones(x.shape)))
theta=np.random.randn(2,1)
print(theta)
# inportation du modele X*O ***************************************
def modele(X,theta):
    return X.dot(theta)

#la fonction cout de notre modeles *******************************
def cost_fonction(X,y,theta):
    m=len(y)
    return 1/(2*m)*np.sum((modele(X,theta)-y)**2)
# les gradients ***************************************************
 
def grad(X,y,theta):
    m=len(y)
    return 1/m*X.T.dot((modele(X,theta)-y))

# descente de gradient *****************************************
def gradient_descente(X,y,theta,learning_rate,n_iteration):
    ll=np.ones(n_iteration)
    for i in range(n_iteration):
        theta=theta-learning_rate*grad(X,y,theta)
        ll[i]=cost_fonction(X,y,theta)
    return theta,ll
# le coefficient de regression************************************
def coef_regression(y,prediction):
    num=np.sum((y-prediction)**2)
    den=np.sum((y-np.mean(y))**2)
    r=1-(num/den)
    return r
# ENTRAINEMENT DU MODELE*****************************************
theta_finale,ll=gradient_descente(X,y,theta,learning_rate=0.01,n_iteration=600)
predictions=modele(X,theta_finale)
plt.scatter(x,y)
plt.plot(x,predictions,c='r',label='prediction')
plt.legend()

plt.figure()
plt.plot(ll,c='r',lw=2,label='fonction cout')
plt.show()
print('R^2 = ',coef_regression(y,predictions))


