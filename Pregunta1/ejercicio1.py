import csv

# Leer el archivo CSV
with open('/content/sample_data/Pokemon.csv', mode ='r') as file:
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
            q3_index -= 1  # Ajuste en caso de índice fuera de rango
        q3 = column[q3_index]

        # Percentil 80
        p80_index = int(len(column) * 0.80)
        if p80_index == len(column):
            p80_index -= 1  # Ajuste en caso de índice fuera de rango
        p80 = column[p80_index]

        percentiles[headers[i]] = {'Q3': q3, 'P80': p80}

    return percentiles

percentiles = calculate_percentiles(data)
print(percentiles)