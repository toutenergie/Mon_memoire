# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 01:33:58 2023

@author: ABDOULAHI FAYE
"""

from fastapi import FastAPI
import random

app=FastAPI()
@app.get("/")
def accuel():
    return {"Massage":"Bienvenu dans notre api de generation de nombres aleatoire"}
@app.get("/NOMBRE ALEATOIRE")
def generer_nombre():
    return {"le nombre aleatoire":random.randint(0,1000)}

@app.get("/NOMBRE ALEATOIRE/{min}_{max}")
def generer_nombre(min:int=0,max:int=100):
    return {"le nombre aleatoire":random.randint(min,max)}
