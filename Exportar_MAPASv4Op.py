import arcpy
import os

# Función para obtener el número de mapa del nombre del archivo
def obtener_numero_mapa(nombre_mapa):
    numero_mapa = ""
    for caracter in nombre_mapa:
        if caracter.isdigit():
            numero_mapa += caracter
        elif numero_mapa:
            break
    return int(numero_mapa)

def modificar_texto_mapa(elemento, numero_mapa, total_mapas):
    # Verificar si el elemento es un cuadro de texto y contiene la etiqueta <BOL>
    if elemento.type == "TEXT_ELEMENT" and "<BOL>" in elemento.text:
        # Modificar el texto del cuadro de texto con el número del mapa y el número total de mapas
        elemento.text = "<BOL> Mapa </BOL> {} <BOL> de </BOL> {}".format(numero_mapa, total_mapas)
    #elif elemento.name == "Observaciones":
        #elemento.text = "MAGNA_Colombia_CTM12 EPSG 9377"
    #elif elemento.name == "Elaboro":
    #    elemento.text = "Jorge Vallejo - Geólogo, Mat Pro. 3880"

def exportar_mapa(mxd, nombre, resolucion):
    # Definir las rutas de los archivos PDF y JPEG
    pdf = os.path.join(carpeta, nombre + ".pdf")
    jpg = os.path.join(carpeta, nombre + ".jpg")
    
    # Exportar el mapa a PDF y JPEG con la resolución especificada
    arcpy.mapping.ExportToPDF(mxd, pdf, resolution=resolucion)
    arcpy.mapping.ExportToJPEG(mxd, jpg, resolution=resolucion)
    
    # Imprimir mensajes de confirmación
    print("Se ha exportado el mapa {} a PDF: {}".format(nombre, pdf))
    print("Se ha exportado el mapa {} a JPEG: {}".format(nombre, jpg))

# Pedir al usuario que ingrese la carpeta donde están los archivos .mxd
carpeta = r"C:\Users\Onfe\OneDrive\YARUMAL\PTO_M3801\ANEXOS\Anexo 1. Mapas y GDB\Mapas\Mapas"

# Crear una lista con los nombres de los archivos .mxd
mapas = [mapa for mapa in os.listdir(carpeta) if mapa.endswith(".mxd")]

# Ordenar la lista de mapas según el número de mapa
mapas = sorted(mapas, key=obtener_numero_mapa)

# Resolución en puntos por pulgada (dpi)
resolucion = 300

# Obtener el total de mapas
total_mapas = len(mapas)

# Recorrer la lista de mapas
for mapa in mapas:
    # Crear un objeto MapDocument con el archivo .mxd
    mxd = arcpy.mapping.MapDocument(os.path.join(carpeta, mapa))
    # Obtener el nombre del archivo sin la extensión
    nombre = os.path.splitext(mapa)[0]
    # Obtener una lista de los elementos del diseño del mapa
    elementos = arcpy.mapping.ListLayoutElements(mxd)

    # Obtener el número de mapa del nombre del archivo
    numero_mapa = obtener_numero_mapa(nombre)
    
    # Recorrer la lista de elementos del diseño
    for elemento in elementos:
        # Llamar a la función para modificar el texto del elemento
        modificar_texto_mapa(elemento, numero_mapa, total_mapas)

    # Guardar los cambios en el archivo .mxd original
    mxd.save()
    
    # Llamar a la función para exportar el mapa a PDF y JPEG
    exportar_mapa(mxd, nombre, resolucion)
    
    # Cerrar el objeto MapDocument
    del mxd

# Imprimir un mensaje de finalización
print("Se han exportado todos los mapas a PDF y JPEG con la calidad mejorada")
