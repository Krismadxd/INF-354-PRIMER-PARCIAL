#   Lo mismo en Colab
#https://colab.research.google.com/drive/1Iq2cjRJjBn7ElvqzxuZsnSse9-DikMgX?usp=sharing




from kanren import facts, Relation, var, run
import numpy as np
#son declaraciones de variables especiales, que sierven para trabajar con las relaciones
a = var() 
b = var()

#Relacion padres
padres = Relation()
facts (padres, 
       ("Elena", "Asunta"),  ("Elena", "Luzi"), ("Elena", "Pablo"), ("Elena", "Zenovia"), ("Elena", "Exalta"), ("Elena", "Alfredo"),
       ("Agustin", "Asunta"), ("Agustin", "Luzi"), ("Agustin", "Pablo"), ("Agustin", "Zenovia"), ("Agustin", "Exalta"), ("Agustin", "Alfredo"),
       ("Richard", "Oriana"), ("Richard", "Cristhian"), ("Richard", "Gilda"), 
       ("Asunta", "Oriana"), ("Asunta", "Cristhian"), ("Asunta", "Gilda"), 
       
       ("Luzi", "Yhoselin"),("Luzi", "kevin"),
       ("Ricardo", "Yhoselin"),("Ricardo", "kevin"),
       
       ("Feliza", "Anderson"),("Feliza", "Timmy"),
       ("Pablo", "Anderson"),("Pablo", "Timmy"),
       
       ("Exalta", "Jhamil"),("Exalta", "Belen"),

       ("Nora", "Yan"),("Nora", "Briseida"),
       ("Alfredo", "Yan"),("Alfredo", "Briseida"),
       
       ("Gilda", "Ian"), 
       ("Marco", "Ian"), 
       
       ("Oriana", "Adamaris")

)

#Relacion abuelos
abuelos = Relation()
facts (abuelos, 
       ("Agustin", "Oriana"), ("Agustin", "Cristhian"), ("Agustin", "Gilda"),
       ("Elena", "Oriana"), ("Elena", "Cristhian"), ("Elena", "Gilda"),

       ("Elena", "Yhoselin"),("Elena", "kevin"),
       ("Agustin", "Yhoselin"),("Agustin", "kevin"),

       ("Elena", "Anderson"), ("Elena", "Timmy"),
       ("Agustin", "Anderson"), ("Agustin", "Timmy"),
       
       ("Elena", "Jhamil"),("Elena", "Belen"),
       ("Agustin", "Jhamil"),("Agustin", "Belen"),

       ("Elena", "Yan"), ("Elena", "Briseida"),
       ("Agustin", "Yan"), ("Agustin", "Briseida"),

       ("Asunta", "Adamaris"), ("Asunta", "Ian"), 
       ("Richard", "Adamaris"), ("Richard", "Ian"), 

       
)

def eliminando_repetidos(datos):
  return list(set(datos))

def padres_go(persona):
  res = run(0, a, padres(a, persona))
  return eliminando_repetidos(res)

def hijos_go(persona):
  res = run(0, a, padres(persona, a))
  return eliminando_repetidos(res)


def abuelos_go(persona):
  res = run(0, a, abuelos(a, persona))
  return eliminando_repetidos(res)

def tios_go(persona):
  # para encontrar los tios, hallamos los abuelos y luego buscamos a sus hijos que no sea el papa
  papas = padres_go(persona)
  abuelos = abuelos_go(persona)

  res = []
  for abu in abuelos:
    hijo_abu = run(0, b, padres(abu, b))
    for datos in hijo_abu:
      if not datos in papas:
        res.append(datos)
  return eliminando_repetidos(res)



def primos_go(persona):
  tios = tios_go(persona)
  res = []
  for tio in tios:
    hijo_de_tio = run(0, b, padres(tio, b))
    for datos in hijo_de_tio:
      res.append(datos)
  return eliminando_repetidos(res)

def hermanos_go(persona):
  papas = padres_go(persona)

  res = []
  for papa in papas:
    hijo_papa = run(0, b, padres(papa, b))
    for datos in hijo_papa:
      if not datos == persona:
        res.append(datos)
  return eliminando_repetidos(res)

def sobrinos_go(persona):
  hermanos = hermanos_go(persona)
  res = []
  for hermano in hermanos:
    hijo_hermano = run(0, b, padres(hermano, b))
    for datos in hijo_hermano:
      res.append(datos)
  return eliminando_repetidos(res)


def nietos_go(persona):
  hijos = hijos_go(persona)
  res = []
  for hijo in hijos:
    hijo_del_hijo = run(0, b, padres(hijo, b))
    for datos in hijo_del_hijo:
      if not datos in hijos:
        res.append(datos)
  return eliminando_repetidos(res)




def calcularTodo(persona):
  print("Datos de ", persona)
  print('Padres', padres_go(persona))
  print('Abuelos', abuelos_go(persona))
  print('Hijos', hijos_go(persona))
  print('Tios', tios_go(persona))
  print('Primos', primos_go(persona))
  print('Hermanos', hermanos_go(persona))
  print('Sobrinos', sobrinos_go(persona))
  print('Nietos', nietos_go(persona))
  print()
personas = ["Cristhian", "Gilda", "Oriana", "Adamaris", "Anderson", "Alfredo", "Asunta"]

for _ in personas:
  calcularTodo(_)