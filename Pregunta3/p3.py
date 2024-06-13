import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Paso 1: Limpieza de Datos
# Cargar el dataset
df = pd.read_csv('Pokemon.csv')

# Mostrar los primeros registros del dataframe
print("Primeros registros del dataframe:")
print(df.head())

# Eliminar filas con valores faltantes
df_limpio = df.dropna()

# Guardar el dataframe limpio
df_limpio.to_csv('Pokemon_limpio.csv', index=False)

# Paso 2: OneHotEncoder para Variables Categóricas
# Seleccionar columnas categóricas para codificación
columnas_categoricas = ['type1', 'type2', 'generation', 'legendary']

# Aplicar OneHotEncoder
codificador = OneHotEncoder(sparse=False)
columnas_codificadas = codificador.fit_transform(df_limpio[columnas_categoricas])

# Convertir a dataframe y añadir nombres de columnas
df_codificado = pd.DataFrame(columnas_codificadas, columns=codificador.get_feature_names_out(columnas_categoricas))

# Concatenar con el dataframe original
df_completo = pd.concat([df_limpio.reset_index(drop=True), df_codificado], axis=1).drop(columns=columnas_categoricas)

# Guardar el dataframe codificado
df_completo.to_csv('Pokemon_codificado.csv', index=False)

# Paso 3: Escalado de Características Numéricas
# Seleccionar columnas numéricas
columnas_numericas = ['total', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']

# Aplicar StandardScaler
escalador = StandardScaler()
columnas_escaladas = escalador.fit_transform(df_completo[columnas_numericas])

# Convertir a dataframe y añadir nombres de columnas
df_escalado = pd.DataFrame(columnas_escaladas, columns=columnas_numericas)

# Reemplazar las columnas originales por las escaladas
df_completo[columnas_numericas] = df_escalado

# Guardar el dataframe escalado
df_completo.to_csv('Pokemon_escalado.csv', index=False)

# Paso 4: Codificación de Etiquetas
# Aplicar LabelEncoder a la columna 'name'
etiquetador = LabelEncoder()
df_completo['name'] = etiquetador.fit_transform(df_completo['name'])

# Guardar el dataframe con etiquetas codificadas
df_completo.to_csv('Pokemon_etiquetado.csv', index=False)

# Paso 5: División del Dataset
# Definir características (X) y etiquetas (y)
X = df_completo.drop(columns=['name'])
y = df_completo['name']

# Dividir en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Guardar los conjuntos de entrenamiento y prueba
X_entrenamiento.to_csv('Pokemon_X_entrenamiento.csv', index=False)
X_prueba.to_csv('Pokemon_X_prueba.csv', index=False)
y_entrenamiento.to_csv('Pokemon_y_entrenamiento.csv', index=False)
y_prueba.to_csv('Pokemon_y_prueba.csv', index=False)

