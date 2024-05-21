# -*- coding: utf-8 -*-
"""
Created on Tue May 21 03:11:58 2024

@author: krismad10
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Cargar el conjunto de datos Pokemon
pokemon_df = pd.read_csv('pokemon.csv')

# Seleccionar características y variable objetivo
X = pokemon_df[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'generation', 'legendary']]
y = pokemon_df['type1']

# Codificar la variable objetivo
label_encoder_y = LabelEncoder()
y_encoded = label_encoder_y.fit_transform(y)

# Codificar la columna 'legendary' que es categórica
label_encoder_legendary = LabelEncoder()
X['legendary'] = label_encoder_legendary.fit_transform(X['legendary'])

# Entrenar un árbol de decisión
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y_encoded)

# Visualizar el árbol de decisión
plt.figure(figsize=(20, 10))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=label_encoder_y.classes_, rounded=True, fontsize=10)
plt.show()


