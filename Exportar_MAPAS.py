import arcpy
import os

# Pedir al usuario que ingrese la carpeta donde están los archivos .mxd
carpeta = r"C:\Users\Onfe\OneDrive\Angelopolis\Anexo 1. Mapas y GDB\Mapas"

# Crear una lista con los nombres de los archivos .mxd
mapas = os.listdir(carpeta)

# Resolución en puntos por pulgada (dpi)
resolucion = 300

# Recorrer la lista de mapas
for mapa in mapas:
    # Verificar que el archivo sea un .mxd
    if mapa.endswith(".mxd"):
        # Crear un objeto MapDocument con el archivo .mxd
        mxd = arcpy.mapping.MapDocument(os.path.join(carpeta, mapa))
        # Obtener el nombre del archivo sin la extensión
        nombre = os.path.splitext(mapa)[0]
        # Definir el nombre y la ruta del archivo pdf
        pdf = os.path.join(carpeta, nombre + ".pdf")
        # Definir el nombre y la ruta del archivo jpg
        jpg = os.path.join(carpeta, nombre + ".jpg")
        # Exportar el mapa a pdf con la resolución especificada
        arcpy.mapping.ExportToPDF(mxd, pdf, resolution=resolucion)
        print(f"Se ha exportado el mapa {nombre} a PDF: {pdf}")
        # Exportar el mapa a jpg con la resolución especificada
        arcpy.mapping.ExportToJPEG(mxd, jpg, resolution=resolucion)
        print(f"Se ha exportado el mapa {nombre} a JPEG: {jpg}")
        # Cerrar el objeto MapDocument
        del mxd

# Imprimir un mensaje de finalización
print("Se han exportado todos los mapas a pdf y jpg con la calidad mejorada")
