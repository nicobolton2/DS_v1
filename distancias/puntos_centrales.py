
def calcular_el_punto_central(coords):

  # Inicializamos las variables acumuladoras
  lat_sum = 0.0
  lng_sum = 0.0

  # Iteramos a través de las coordenadas y acumulamos los valores
  for lat, lng in coords:
    lat_sum += lat
    lng_sum += lng

  # Calculamos las medias aritméticas
  lat_mean = lat_sum / len(coords)
  lng_mean = lng_sum / len(coords)

  # Creamos la tupla con la coordenada central
  center = (lat_mean, lng_mean)

  return center


# Lista con las coordenadas de la figura
coords = [[1.0, 2.0], [3.0, 2.0], [3.0, 6.0], [5.0, 6.0]]
print(calcular_el_punto_central(coords))
