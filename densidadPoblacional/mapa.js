// Crear la variable mapa con coordenadas de centro y zoom
let map = L.map('map').setView([-33.583455, -70.571755],14)

// Agregar mapa base de OpenStreetMap
//blanco
//https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png	
//normal
//https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png
//negro
//https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png	
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',{
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Volar a coordenadas de los sitios de la Lista desplegable
document.getElementById('select-location').addEventListener('change', function(e){
    let coords = e.target.value.split(",");
    map.flyTo(coords,14);
})

// Agregar mapa base para el Mini Mapa
var carto_light = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {attribution: '©OpenStreetMap, ©CartoDB',subdomains: 'abcd',maxZoom: 24});

// Agregar plugin MiniMap
var minimap = new L.Control.MiniMap(carto_light,
    {
        toggleDisplay: true,
        minimized: false,
        position: "bottomleft"
    }).addTo(map);

// Agregar escala
 new L.control.scale({imperial: false}).addTo(map);

// Agregar control para ver los datos al pasar el puntero
var info = L.control();

// Crear un div con una clase info
info.onAdd = function(map){
    this._div = L.DomUtil.create('div','info');
    this.update();
    return this._div;
};

// Agregar el metodo que actualiza el control segun el puntero vaya pasando
//ejemplo: "FID": 136205, "REGION": "13", "NOM_REGION": "REGIÓN METROPOLITANA DE SANTIAGO", "PROVINCIA": "132", "NOM_PROVIN": "CORDILLERA", "COMUNA": "13201", "NOM_COMUNA": "PUENTE ALTO", "DISTRITO": 9, "LOCALIDAD": 4, "ENTIDAD_MA": 16, "CATEGORIA": 1, "NOM_CATEGO": "CD", "MANZENT_I": "13201091004016", "TOTAL_PERS": 46, "TOTAL_VIVI": 16, "NHOMBRES": 26, "NMUJERES": 20, "Shape__Area": 4519.03515625, "Shape__Length": 281.43933145317197 
info.update = function(props){
    this._div.innerHTML = '<h4>Total Viviendas por Barrio</h4>' + 
                            (props ? 
                                '<b>' + 'Datos Recopilados en censo 2017' + '</b>'+
                                '<br/> FID: ' + props.FID + '</sup>' +
                                '<br/> REGION: ' + props.REGION + '</sup>' +
                                '<br/> NOM_REGION: ' + props.NOM_REGION + '</sup>' +
                                '<br/> PROVINCIA: ' + props.PROVINCIA + '</sup>' +
                                '<br/> NOM_PROVIN:' + props.NOM_PROVIN + '</sup>' +
                                '<br/> COMUNA: ' + props.COMUNA + '</sup>' +
                                '<br/> NOM_COMUNA: ' + props.NOM_COMUNA + '</sup>' +
                                '<br/> DISTRITO: ' + props.DISTRITO + '</sup>' +
                                '<br/> LOCALIDAD: ' + props.LOCALIDAD + '</sup>' +
                                '<br/> ENTIDAD_MA: ' + props.ENTIDAD_MA + '</sup>' +
                                '<br/> CATEGORIA: ' + props.CATEGORIA + '</sup>' +
                                '<br/> NOM_CATEGO: ' + props.NOM_CATEGO + '</sup>' +
                                '<br/> MANZENT_I: ' + props.MANZENT_I + '</sup>' +
                                '<br/> TOTAL_PERS: ' + props.TOTAL_PERS + '</sup>' +
                                '<br/> TOTAL_VIVI: ' + props.TOTAL_VIVI + '</sup>' +
                                '<br/> NHOMBRES: ' + props.NHOMBRES + '</sup>' +
                                '<br/> NMUJERES: ' + props.NMUJERES + '</sup>' +
                                '<br/> Shape__Area: ' + props.Shape__Area + '</sup>' +
                                '<br/> Shape__Length: ' + props.Shape__Length + '</sup>'                             
                            : 'Pase el puntero por un barrio');
};
info.addTo(map);

// Generar rangos de colores, hay que cambiarlo y trabajar con las variables de area
function getColor(d){
    return  d > 300 ? '#F2E9FF' :
            d > 200 ? '#e8d8ff' :
            d > 133 ? '#cfb1ff' :
            d > 89  ? '#b38bff' :
            d > 59  ? '#9265ff' :
            d > 39  ? '#673dff' :
            d > 26  ? '#0000ff' :
                      '#2510a3' ;
}

// Crear la funcion para mostrar la simbologia de acuerdo al campo total_personas 
function style(feature){
    var val = feature.properties.Shape__Area/feature.properties.TOTAL_PERS;
    return {
        fillColor: getColor(val),
        weight: 0, //ojito con esto que le da contorno antes de marcarlo
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.5
    };
}

// Agregar interaccion del puntero con la capa para resaltar el objeto
function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 4,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    info.update(layer.feature.properties);
}

// Configurar los cambios de resaltado y zoom de la capa

var barriosJS;

function resetHighlight(e){
    barriosJS.resetStyle(e.target);
    info.update();
}

function zoomToFeature(e){
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer){
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}

// Agregar capa en formato GeoJson
barriosJS = L.geoJson(barrios,{
    style: style,
    onEachFeature: onEachFeature
}).addTo(map);

// Agregar atribucion
map.attributionControl.addAttribution('Viviendas en Bogotá &copy; <a href="https://www.dane.gov.co/">DANE</a>');