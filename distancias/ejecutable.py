# Importa la librería json para trabajar con archivos JSON
import json

# Importa la librería puntos_centrales, que se supone tiene una función para calcular las coordenadas centrales de una característica
import puntos_centrales as p

# Importa la librería openpyxl para trabajar con archivos de Excel
import openpyxl

# Crea un nuevo libro de Excel y selecciona la primera hoja (hoja activa)
wb = openpyxl.Workbook()
ws = wb.active

# Define una lista de tuplas que incluye los encabezados de las columnas de la hoja de cálculo
datos = [
    ("COMUNA", "FID", "TOTAL_PERS", "Coordenada_Central_lat", "Coordenada_Central_lon" ,"NOM_COMUNA","TOTAL_VIVI","Shape__Area")
]

# Abre el archivo "geometry" en modo lectura y lee su contenido en una variable
with open('/home/nicobolton/Escritorio/DS_v1/densidadPoblacional/layers/datos_f.json', 'r') as f:
  # Convierte el contenido del archivo a un diccionario Python
  json_string = f.read()
  data = json.loads(json_string)

  # Itera sobre cada una de las características del diccionario
  for feature in data["features"]:
    # Calcula las coordenadas centrales de la característica
    lat,lon = p.calcular_el_punto_central(feature["geometry"]["coordinates"][0])

    # Crea una tupla que incluye los datos de la característica, incluyendo las coordenadas centrales calculadas
    centro = (
      feature["properties"]["COMUNA"],
      feature["properties"]["FID"],
      feature["properties"]["TOTAL_PERS"],
      lat,
      lon,
      feature["properties"]["NOM_COMUNA"],
      feature["properties"]["TOTAL_VIVI"],
      feature["properties"]["Shape__Area"]
      )    

    # Agrega la tupla a la lista "datos"
    datos.append(centro)

# Itera sobre cada elemento en la lista "datos" y escribe cada elemento en la hoja de cálculo
for dato in datos:
    ws.append(dato)

# Guarda el libro de Excel con el nombre "datos_de_las_comunas.xlsx"
wb.save("datos_de_las_comunas.xlsx")


'''
barrios = {
    "type": "FeatureCollection",
    "name": "Poblaci%C3%B3n_por_manzana_seg%C3%BAn_Censo_2017%2C_Chile.",
    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
    "features": [
      { "type": "Feature", 
        "properties": { 
          "FID": 136205, "REGION": "13", "NOM_REGION": "REGIÓN METROPOLITANA DE SANTIAGO", "PROVINCIA": "132", "NOM_PROVIN": "CORDILLERA", "COMUNA": "13201", "NOM_COMUNA": "PUENTE ALTO", "DISTRITO": 9, "LOCALIDAD": 4, "ENTIDAD_MA": 16, "CATEGORIA": 1, "NOM_CATEGO": "CD", "MANZENT_I": "13201091004016", "TOTAL_PERS": 46, "TOTAL_VIVI": 16, "NHOMBRES": 26, "NMUJERES": 20, "Shape__Area": 4519.03515625, "Shape__Length": 281.43933145317197 
        },"geometry": { 
          "type": "Polygon", "coordinates": [ [ [ -70.554407149370405, -33.577439869084202 ], [ -70.554418920596703, -33.577440556166202 ], [ -70.554432769256806, -33.577440431160397 ], [ -70.554444150177304, -33.577437247560397 ], [ -70.554454545440905, -33.577432754547502 ], [ -70.554460814614899, -33.577429027756899 ], [ -70.5544666260339, -33.577423576965998 ], [ -70.554474620107598, -33.577413881375001 ], [ -70.5546253329927, -33.577134171534297 ], [ -70.554245433280101, -33.576975559903701 ], [ -70.554241115634994, -33.576973756763003 ], [ -70.554237916746402, -33.576972529188403 ], [ -70.554235502965994, -33.576971602886701 ], [ -70.553865769189898, -33.576829733035296 ], [ -70.553677746131001, -33.577151634569802 ], [ -70.553906812449398, -33.5772400487187 ], [ -70.554360520421696, -33.577422537349698 ], [ -70.554404074588305, -33.577439800735696 ], [ -70.554407149370405, -33.577439869084202 ] ] ] 
        } 
      },
      { "type": "Feature", 
        "properties": { 
          "FID": 136206, "REGION": "13", "NOM_REGION": "REGIÓN METROPOLITANA DE SANTIAGO", "PROVINCIA": "132", "NOM_PROVIN": "CORDILLERA", "COMUNA": "13201", "NOM_COMUNA": "PUENTE ALTO", "DISTRITO": 16, "LOCALIDAD": 4, "ENTIDAD_MA": 19, "CATEGORIA": 1, "NOM_CATEGO": "CD", "MANZENT_I": "13201161004019", "TOTAL_PERS": 155, "TOTAL_VIVI": 46, "NHOMBRES": 77, "NMUJERES": 78, "Shape__Area": 11876.12109375, "Shape__Length": 569.31093276687795 
        }, "geometry": {
          "type": "Polygon", "coordinates": [ [ [ -70.609780398846297, -33.577922796029704 ], [ -70.609878915979195, -33.577936755306503 ], [ -70.609893106381705, -33.577935036702101 ], [ -70.6099130371569, -33.577929187511501 ], [ -70.609927153815093, -33.577917730148599 ], [ -70.609937516702999, -33.577907225167799 ], [ -70.609942968393199, -33.577893265890999 ], [ -70.609947324709296, -33.577878418983303 ], [ -70.610234938691406, -33.5762399567381 ], [ -70.610233362179898, -33.576218874830801 ], [ -70.610222834715998, -33.576197369342601 ], [ -70.610204845577101, -33.576180107755299 ], [ -70.610187709894802, -33.576174018445698 ], [ -70.609808235561601, -33.576118657979201 ], [ -70.609692027864796, -33.5767557314214 ], [ -70.609487200973504, -33.577878718457598 ], [ -70.609697530816305, -33.577910346714603 ], [ -70.609780398846297, -33.577922796029704 ] ] ] 
        } 
      },
    ]
  }
'''