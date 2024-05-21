# 1. Seleccione un dataset de datos tabulares (UCI, KAAGLE). Realice lo siguiente:
#   a. Con Python sin uso de librerías, calcule del último cuartil, 
#   percentil 80 por columna; explique qué significa en cada caso.
#*********************   INSISO a *******************************
import csv

# Leer el archivo CSV
with open('Pokemon.csv', mode='r') as file:
    csvFile = csv.reader(file)
    headers = next(csvFile)
    data = list(csvFile)

# Convertir los datos numéricos a float
def convert_to_float(data):
    for row in data:
        for i in range(len(row)):
            try:
                row[i] = float(row[i])
            except ValueError:
                pass  # Ignorar columnas no numéricas

convert_to_float(data)

# Función para calcular el último cuartil (Q3) y el percentil 80
def calculate_percentiles(data):
    percentiles = {}
    for i in range(len(headers)):
        column = [row[i] for row in data if isinstance(row[i], float)]
        if len(column) == 0:
            continue  # Omitir columnas sin datos numéricos
        column.sort()

        # Último cuartil (Q3)
        q3_index = int(len(column) * 0.75)
        if q3_index == len(column):
            q3_index -= 1  
        q3 = column[q3_index]

        # Percentil 80
        p80_index = int(len(column) * 0.80)
        if p80_index == len(column):
            p80_index -= 1 
        p80 = column[p80_index]

        percentiles[headers[i]] = {'Q3': q3, 'P80': p80}

    return percentiles

percentiles = calculate_percentiles(data)
print(percentiles)
print("\n")

#  b. Realice lo mismo del inciso (a) con el uso de numpy y pandas
#*********************   INSISO b *******************************
import pandas as pd
import numpy as np

# Cargar el conjunto de datos
df = pd.read_csv('Pokemon.csv')

# Seleccionar solo las columnas numéricas
numeric_df = df.select_dtypes(include=[np.number])

# Calcular Q3 y percentil 80 usando pandas y numpy
percentiles = numeric_df.quantile([0.75, 0.80])

# Convertir a DataFrame y usar to_string() para imprimir todas las columnas
print(percentiles.to_string())

#   c. Obtenga la media, mediana, moda y geométrica; explique la diferencia de los  
#   resultados y cuál de ellas se puede utilizar en un artículo científico.
#*********************   INSISO c *******************************
from scipy import stats
from scipy.stats import gmean

# Calcular media, mediana y moda usando pandas
mean = numeric_df.mean()
median = numeric_df.median()
mode = numeric_df.mode().iloc[0]  # Puede haber más de una moda

# Calcular la media geométrica usando scipy
geom_mean = numeric_df.apply(lambda x: gmean(x.dropna()))

print("Media:\n", mean)
print("Mediana:\n", median)
print("Moda:\n", mode)
print("Media Geométrica:\n", geom_mean)

#  d. Grafique los datos y explique su comportamiento (PYTHON)
#*********************   INSISO d *******************************
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Función para graficar barras
def graficar(indices, valores, titulo):
    colores_aleatorios = [random.choice(['red', 'blue', 'green', 'purple', 'orange', 'pink', 'gray', 'brown']) for _ in indices]
    plt.figure(figsize=(15, 6))
    plt.bar(indices, valores, color=colores_aleatorios)
    plt.xlabel('Columnas')
    plt.ylabel(titulo)
    plt.title('{} por Columna en el Conjunto de Datos'.format(titulo))
    plt.xticks(rotation=45)
    plt.show()

# Ejemplo de uso
columnas = ['total', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']
valores_media = numeric_df[columnas].mean().values
graficar(columnas, valores_media, 'Media')



# Función para graficar histogramas
def graficar_histograma(column, titulo):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, color='skyblue')
    plt.title('Distribución de {}'.format(titulo))
    plt.xlabel(titulo)
    plt.ylabel('Frecuencia')
    plt.show()

# Ejemplo de uso
graficar_histograma('hp', 'HP')
graficar_histograma('attack', 'Attack')
graficar_histograma('defense', 'Defense')
graficar_histograma('sp_attack', 'Special Attack')
graficar_histograma('sp_defense', 'Special Defense')
graficar_histograma('speed', 'Speed')
graficar_histograma('generation', 'Generation')

# Función para graficar dispersión
def graficar_dispersion(x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_column, y=y_column, data=df, hue='type1', palette='Set1')
    plt.title('{} vs {}'.format(x_column.capitalize(), y_column.capitalize()))
    plt.xlabel(x_column.capitalize())
    plt.ylabel(y_column.capitalize())
    plt.show()

# Ejemplo de uso
graficar_dispersion('attack', 'defense')

# Función para graficar boxplot
def graficar_boxplot():
    plt.figure(figsize=(15, 10))
    sns.boxplot(data=numeric_df, palette='Set2')
    plt.title('Boxplot de Todas las Columnas Numéricas')
    plt.xticks(rotation=45)
    plt.show()

# Ejemplo de uso
graficar_boxplot()
