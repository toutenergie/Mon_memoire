#!/usr/bin/env python
# coding: utf-8

# In[1]:


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.regression.linear_model import yule_walker
from statsmodels.tsa.stattools import adfuller,acf
from statsmodels.tsa.arima.model import ARIMA
from  pandas.tseries.offsets import DateOffset
from sklearn.metrics import mean_squared_error,r2_score
from  pandas.tseries.offsets import DateOffset
import seaborn as sms
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


bokhol=pd.read_excel('basedonnees.xlsx',index_col=[0],parse_dates=True)


# In[23]:


bokhol.head()

#sms.pairplot(bokhol)


# In[24]:


TMP=pd.DataFrame(bokhol['Température module (°C)'])
TMP#=np.log(TMP)


# In[25]:


TC=TMP.dropna(axis=0)
TC


# In[26]:


TC.plot()


# In[27]:


def adfuller_test(sales):
    result=adfuller(sales)
    label=['ADF test statistic','p_value','lages used','numbre of observation used']
    for value,label in zip(result,label):
        print(label+':'+str(value))
        if result[1]<=0.05:
            print('strong evident agains the null hypothesis ...')
        else:
            print('weak evidence agains null hypothesis...')
            
#adfuller_test(TC)


# In[28]:


plot_pacf(TC)


# ### TESTONS LE BON MODEL ARIMA(p,d,q)

# In[29]:


from pmdarima import auto_arima
import warnings
warnings.filterwarnings('ignore')


# In[38]:


orderModel=auto_arima(TC,trace=True,supress_warnings=True)


# ### LE  MODEL ARIMA(p,d,q) adequat

# In[30]:


model=ARIMA(TC.values,order=(2,1,4))
model_fit=model.fit()


# In[31]:


model_fit.plot_diagnostics(figsize=(10, 8))


# In[32]:


TC['ARIMA1']=model_fit.predict() #0,2*TC.shape[0]-1)


# In[33]:


TC.plot()


# In[34]:


TC


# In[35]:


mois=['2021-01-01 00:10:00','2021-02-28 00:05:00','2021-03-31 00:05:00', '2021-04-30 00:05:00',
               '2021-05-31 00:05:00', '2021-06-30 00:05:00',
               '2021-07-31 00:05:00', '2021-08-31 00:05:00',
               '2021-09-30 00:05:00', '2021-10-31 00:05:00',
               '2021-11-30 00:05:00', '2021-12-31 21:00:00']#pd.date_range(TC.index[0],periods=12,freq='M'


# ### METHODES DE  PREDICTION

# In[37]:


#  division la base en donnees de test et de train
# selection e la colonne Temperature du module
TC_dp=TC['Température module (°C)']
#disparsing de la base de donnees
TC_train=TC_dp.iloc[:-12]
TC_test=TC_dp.iloc[-12:]


# In[38]:


TC_train.shape


# In[39]:


TC_test.shape[0]


# In[40]:


TC_dp.shape


# In[41]:


model=ARIMA(TC_train,order=(2,1,4))
model_fif=model.fit()


# In[42]:


model_fit.plot_diagnostics(figsize=(10, 8))


# In[51]:


longueur=TC_test.shape[0] #TC_test.shape[0]+TC_dp.shape[0]
prediction=model_fif.get_forecast(steps=longueur)


# In[ ]:





# In[54]:


donnees_futures=pd.date_range(TC.index[-1],periods=TC_test.shape[0],freq='00h05t')
prediction.index=donnees_futures


# In[58]:


predictions=np.exp(prediction.predicted_mean)


# In[ ]:


plt.plot(pd.date_range(x.index[-1], periods=12, freq='M'), x_pred, color='r', label='Predit')


# In[59]:


prediction.plot(figsize=(12,5))
plt.xlabel('minutes')
plt.ylabel('temperature module')
plt.title('EVOLUTION DE LA TEMPERATURE PREDITE DES MODULES PENDANT 1h')


# ### evaluation statistaques du modele de prediction

# In[48]:


mean_pred=prediction.mean()
somme=abs(sum(TC_test-mean_pred))
T=1/len(prediction)
mean_TC_test=TC_test.mean()
#numR=sum((TC_test.values-mean_pred)*(prediction.values-mean_pred))
#demR=sum(((TC_test.values-mean_TC_test)**2)*((prediction.values-mean_pred)**2))


# In[49]:


RMSE=mean_squared_error(prediction,TC_test) # evaluation a court terme
#MBE #information sur les performance du predicteur a long terme
#mape = (np.abs(1-x_pred/x_test)).mean()*100
MAPE=(np.abs((1-prediction)/TC_test).mean()) #il mesure l'ajustement du systeme 10 % EST ACCEPTABLE
R2=r2_score(prediction,TC_test)


# In[50]:


print('performance a court terme:',RMSE)
print('performance PAR rapport a 10%:',MAPE)
#print('COEFFICIENT DE CORRELATION:',R2)

