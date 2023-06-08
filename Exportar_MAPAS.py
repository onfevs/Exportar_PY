# Importar los módulos necesarios
import arcpy
import os

# Definir la carpeta donde están los archivos .mxd
carpeta = r"D:\MiGEO\COPIAS DE SEGURIDAD\IDI-16113X\03_MapasMXD"

# Definir la carpeta donde se guardarán los archivos pdf y jpg
salida = r"D:\MiGEO\COPIAS DE SEGURIDAD\IDI-16113X\03_MapasMXD"

# Crear una lista con los nombres de los archivos .mxd
mapas = os.listdir(carpeta)

# Recorrer la lista de mapas
for mapa in mapas:
    # Verificar que el archivo sea un .mxd
    if mapa.endswith(".mxd"):
        # Crear un objeto MapDocument con el archivo .mxd
        mxd = arcpy.mapping.MapDocument(os.path.join(carpeta, mapa))
        # Obtener el nombre del archivo sin la extensión
        nombre = os.path.splitext(mapa)[0]
        # Definir el nombre y la ruta del archivo pdf
        pdf = os.path.join(salida, nombre + ".pdf")
        # Definir el nombre y la ruta del archivo jpg
        jpg = os.path.join(salida, nombre + ".jpg")
        # Exportar el mapa a pdf
        arcpy.mapping.ExportToPDF(mxd, pdf)
        # Exportar el mapa a jpg
        arcpy.mapping.ExportToJPEG(mxd, jpg)
        # Cerrar el objeto MapDocument
        del mxd

# Imprimir un mensaje de finalización
print("Se han exportado todos los mapas a pdf y jpg")
