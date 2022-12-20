#Se encontro una bdds en Geojson, la cual mostraba los datos por html, 
#el probeolma es que eran tantos datos que no cargaba la pagina 
#y al intentar copiar lis datos estos superaban la capacidad de caracdteres que soporte el Ctrl + c
#se creo este script para realizar web scraping a los datos
#resultado: ni aún así se consiguieron los datos. :c


from lxml import html
import requests
 
page = requests.get('http://datos.cedeus.cl/geoserver/wfs?srsName=EPSG%3A4326&typename=geonode%3Amaestro_de_calles_2018_stgo&outputFormat=json&version=1.0.0&service=WFS&request=GetFeature')
tree = html.fromstring(page.content)
print(tree)
# Get element using XPath
buyers = tree.xpath('/html/body[@style="word-wrap: break-word; white-space: pre-wrap;"]/text()')
f = open ('SS.js','w')
a=len(buyers)
f.write(str(a))
f.close()
