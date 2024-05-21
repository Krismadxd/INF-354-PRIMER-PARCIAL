# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:28:13 2024

@author: krismad10
"""

from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('pokemon.csv')

# Seleccionar las columnas categóricas
categorical_columns = ['type1', 'type2']

# Crear un codificador OneHotEncoder
encoder = OneHotEncoder()

# Transformar las columnas categóricas
encoded_data = encoder.fit_transform(data[categorical_columns])

# Convertir la salida a un DataFrame de pandas si es necesario
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(categorical_columns))
