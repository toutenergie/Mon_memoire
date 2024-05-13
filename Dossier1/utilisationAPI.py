# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 02:17:36 2023

@author: ABDOULAHI FAYE
"""

import requests
import pandas as pd
# on recupere URL de l'API
#
reponse_nombre=requests.get(f"{on met l'adresse url}/")
# AFFICHAGE
print(reponse_nombre.json())
# genere un nombre aleatoire
reponse_aleatoire=requests.get(f"url"/nombre_aleatoire)
df=pd.DataFrame([reponse_aleatoire.json()])
print(df)
# generateur e nombre aleatoire entre min et max
val_min=0
val_max=200
reponse_ale_min=requests.get(f"url/autrenom/autrenom"
                             )