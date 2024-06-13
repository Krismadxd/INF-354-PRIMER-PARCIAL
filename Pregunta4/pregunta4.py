from kanren import facts, Relation, var, run

# Definición de variables especiales para trabajar con relaciones
a = var() 
b = var()

# Definición de la relación 'padres'
padres = Relation()
facts(padres, 
    ("Elena", "Asunta"), ("Elena", "Luzi"), ("Elena", "Pablo"), ("Elena", "Zenovia"), ("Elena", "Exalta"), ("Elena", "Alfredo"),
    ("Agustin", "Asunta"), ("Agustin", "Luzi"), ("Agustin", "Pablo"), ("Agustin", "Zenovia"), ("Agustin", "Exalta"), ("Agustin", "Alfredo"),
    ("Richard", "Oriana"), ("Richard", "Cristhian"), ("Richard", "Gilda"), 
    ("Asunta", "Oriana"), ("Asunta", "Cristhian"), ("Asunta", "Gilda"), 
    ("Luzi", "Yhoselin"), ("Luzi", "Kevin"),
    ("Ricardo", "Yhoselin"), ("Ricardo", "Kevin"),
    ("Feliza", "Anderson"), ("Feliza", "Timmy"),
    ("Pablo", "Anderson"), ("Pablo", "Timmy"),
    ("Exalta", "Jhamil"), ("Exalta", "Belen"),
    ("Nora", "Yan"), ("Nora", "Briseida"),
    ("Alfredo", "Yan"), ("Alfredo", "Briseida"),
    ("Gilda", "Ian"), 
    ("Marco", "Ian"), 
    ("Oriana", "Adamaris")
)

# Definición de la relación 'abuelos'
abuelos = Relation()
facts(abuelos, 
    ("Agustin", "Oriana"), ("Agustin", "Cristhian"), ("Agustin", "Gilda"),
    ("Elena", "Oriana"), ("Elena", "Cristhian"), ("Elena", "Gilda"),
    ("Elena", "Yhoselin"), ("Elena", "Kevin"),
    ("Agustin", "Yhoselin"), ("Agustin", "Kevin"),
    ("Elena", "Anderson"), ("Elena", "Timmy"),
    ("Agustin", "Anderson"), ("Agustin", "Timmy"),
    ("Elena", "Jhamil"), ("Elena", "Belen"),
    ("Agustin", "Jhamil"), ("Agustin", "Belen"),
    ("Elena", "Yan"), ("Elena", "Briseida"),
    ("Agustin", "Yan"), ("Agustin", "Briseida"),
    ("Asunta", "Adamaris"), ("Asunta", "Ian"), 
    ("Richard", "Adamaris"), ("Richard", "Ian")
)

# Función para eliminar duplicados en una lista
def eliminando_repetidos(datos):
    return list(set(datos))

# Función para obtener los padres de una persona
def padres_go(persona):
    res = run(0, a, padres(a, persona))
    return eliminando_repetidos(res)

# Función para obtener los hijos de una persona
def hijos_go(persona):
    res = run(0, a, padres(persona, a))
    return eliminando_repetidos(res)

# Función para obtener los abuelos de una persona
def abuelos_go(persona):
    res = run(0, a, abuelos(a, persona))
    return eliminando_repetidos(res)

# Función para obtener los tíos de una persona
def tios_go(persona):
    papas = padres_go(persona)
    abuelos = abuelos_go(persona)
    res = []
    for abu in abuelos:
        hijo_abu = run(0, b, padres(abu, b))
        for datos in hijo_abu:
            if datos not in papas:
                res.append(datos)
    return eliminando_repetidos(res)

# Función para obtener los primos de una persona
def primos_go(persona):
    tios = tios_go(persona)
    res = []
    for tio in tios:
        hijo_de_tio = run(0, b, padres(tio, b))
        for datos in hijo_de_tio:
            res.append(datos)
    return eliminando_repetidos(res)

# Función para obtener los hermanos de una persona
def hermanos_go(persona):
    papas = padres_go(persona)
    res = []
    for papa in papas:
        hijo_papa = run(0, b, padres(papa, b))
        for datos in hijo_papa:
            if datos != persona:
                res.append(datos)
    return eliminando_repetidos(res)

# Función para obtener los sobrinos de una persona
def sobrinos_go(persona):
    hermanos = hermanos_go(persona)
    res = []
    for hermano in hermanos:
        hijo_hermano = run(0, b, padres(hermano, b))
        for datos in hijo_hermano:
            res.append(datos)
    return eliminando_repetidos(res)

# Función para obtener los nietos de una persona
def nietos_go(persona):
    hijos = hijos_go(persona)
    res = []
    for hijo in hijos:
        hijo_del_hijo = run(0, b, padres(hijo, b))
        for datos in hijo_del_hijo:
            if datos not in hijos:
                res.append(datos)
    return eliminando_repetidos(res)

# Función para calcular y mostrar todas las relaciones de una persona dada
def calcularTodo(persona):
    print("Datos de", persona)
    print('Padres:', padres_go(persona))
    print('Abuelos:', abuelos_go(persona))
    print('Hijos:', hijos_go(persona))
    print('Tíos:', tios_go(persona))
    print('Primos:', primos_go(persona))
    print('Hermanos:', hermanos_go(persona))
    print('Sobrinos:', sobrinos_go(persona))
    print('Nietos:', nietos_go(persona))
    print()

# Lista de personas para las cuales se calcularán las relaciones
personas = ["Cristhian", "Gilda", "Oriana", "Adamaris", "Anderson", "Alfredo", "Asunta"]

# Calcular y mostrar las relaciones para cada persona en la lista
for persona in personas:
    calcularTodo(persona)
