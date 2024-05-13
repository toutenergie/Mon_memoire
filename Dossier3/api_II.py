# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 02:40:29 2023

@author: ABDOULAHI FAYE
"""

from fastapi import FastAPI
from pydantic import BaseModel
imoprt statsmodels.api as sn
import shap
from sklearn.linear_model import LinearRegression
import numpy as np
app=FastAPI()
np.random(seed=0)

import random
