import arcpy
import os

# Pedir al usuario que ingrese la carpeta donde están los archivos .mxd
carpeta = r"C:\Users\Onfe\Desktop\3X"

# Crear una lista con los nombres de los archivos .mxd
mapas = [mapa for mapa in os.listdir(carpeta) if mapa.endswith(".mxd")]

# Resolución en puntos por pulgada (dpi)
resolucion = 300

# Función de clave personalizada para ordenar los mapas según el número de mapa en el nombre del archivo
def obtener_numero_mapa(nombre_mapa):
    numero_mapa = ""
    for caracter in nombre_mapa:
        if caracter.isdigit():
            numero_mapa += caracter
        elif numero_mapa:
            break
    return int(numero_mapa)

# Ordenar la lista de mapas según el número de mapa
mapas = sorted(mapas, key=obtener_numero_mapa)

# Recorrer la lista de mapas
for mapa in mapas:
    # Crear un objeto MapDocument con el archivo .mxd
    mxd = arcpy.mapping.MapDocument(os.path.join(carpeta, mapa))
    
    # Obtener el nombre del archivo sin la extensión
    nombre = os.path.splitext(mapa)[0]
    
    # Definir el nombre y la ruta del archivo pdf
    pdf = os.path.join(carpeta, nombre + ".pdf")
    # Definir el nombre y la ruta del archivo jpg
    jpg = os.path.join(carpeta, nombre + ".jpg")
    
    # Obtener una lista de los elementos del diseño del mapa
    elementos = arcpy.mapping.ListLayoutElements(mxd)
    
    # Recorrer la lista de elementos
    for elemento in elementos:
        # Verificar si el elemento es un cuadro de texto y si contiene la etiqueta <BOL>
        if elemento.type == "TEXT_ELEMENT" and "<BOL>" in elemento.text:
            # Obtener el número de mapa del nombre del archivo
            numero_mapa = obtener_numero_mapa(nombre)
            
            # Cambiar el texto del cuadro de texto con el número del mapa y el número total de mapas
            elemento.text = "<BOL> Mapa </BOL> {} <BOL> de </BOL> {}".format(numero_mapa, len(mapas))
    
    # Guardar los cambios en el archivo .mxd original
    mxd.save()
    
    # Exportar el mapa a pdf con la resolución especificada
    arcpy.mapping.ExportToPDF(mxd, pdf, resolution=resolucion)
    print("Se ha exportado el mapa {} a PDF: {}".format(nombre, pdf))
    # Exportar el mapa a jpg con la resolución especificada
    arcpy.mapping.ExportToJPEG(mxd, jpg, resolution=resolucion)
    print("Se ha exportado el mapa {} a JPEG: {}".format(nombre, jpg))
    
    # Cerrar el objeto MapDocument
    del mxd

# Imprimir un mensaje de finalización
print("Se han exportado todos los mapas a pdf y jpg con la calidad mejorada")
