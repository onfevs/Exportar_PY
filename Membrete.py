import arcpy
import os

# Pedir al usuario que ingrese la carpeta donde están los archivos .mxd
carpeta = r"C:\Users\Onfe\Desktop\3X"

# Crear una lista con los nombres de los archivos .mxd que terminen en .mxd
mapas = [mapa for mapa in os.listdir(carpeta) if mapa.endswith(".mxd")]

# Resolución en puntos por pulgada (dpi)
resolucion = 300

# Recorrer la lista de mapas
for i, mapa in enumerate(mapas):
    # Crear un objeto MapDocument con el archivo .mxd
    mxd = arcpy.mapping.MapDocument(os.path.join(carpeta, mapa))
    # Obtener el nombre del archivo sin la extensión
    nombre = os.path.splitext(mapa)[0]
    # Crear el nuevo nombre del archivo con el formato "Mapa X_nombre.mxd"
    nombre = "Mapa {}_".format(i+1) + nombre.split("_", 1)[1]
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
            # Cambiar el texto del cuadro de texto con el número del mapa y el número total de mapas
            elemento.text = "<BOL> Mapa </BOL> {} <BOL> de </BOL> {}".format(i+1, len(mapas))
    
    # Guardar los cambios en el archivo .mxd
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
