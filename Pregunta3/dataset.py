# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:35:17 2024

@author: krismad10
"""

import pandas as pd

# Especifica la ruta del archivo CSV
file_path = "pokemon.csv"

# Lee el archivo CSV y carga los datos en un DataFrame
data = pd.read_csv(file_path)

# Muestra las primeras filas del DataFrame para verificar que se haya cargado correctamente
print(data.head(15))
