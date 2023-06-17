import arcpy
import shutil
import os

# Pedir al usuario que ingrese la carpeta donde están los archivos .mxd
carpeta = r"C:\Users\Onfe\Desktop\3X"

# Crear una lista con los nombres y las extensiones de los archivos .mxd
mapas = [os.path.splitext(mapa) for mapa in os.listdir(carpeta) if mapa.endswith(".mxd")]

# Resolución en puntos por pulgada (dpi)
resolucion = 300

# Carpeta de destino para los archivos PDF y JPEG
carpeta_destino = r"C:\Users\Onfe\Desktop\3X\Exportados"

# Crear la carpeta de destino si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Crear un diccionario con los nombres y los textos de los elementos de las fechas
fechas = {"FechaDD": "1  3", "FechaMM": "1  2", "FechaAA": "2  9  2  9"}

# Recorrer la lista de mapas
for i, (nombre, extension) in enumerate(mapas):
    # Crear un objeto MapDocument con el archivo .mxd
    mxd = arcpy.mapping.MapDocument(os.path.join(carpeta, nombre + extension))
    # Crear el nuevo nombre del archivo con el formato "Mapa X_nombre.mxd"
    nombre = "Mapa {}_".format(i+1) + nombre.split("_", 1)[1]
    
    # Obtener una lista de los elementos del diseño del mapa
    elementos = arcpy.mapping.ListLayoutElements(mxd)
    # Recorrer la lista de elementos
    for elemento in elementos:
        # Verificar si el elemento es un cuadro de texto y si contiene la etiqueta <BOL>
        if elemento.type == "TEXT_ELEMENT" and "<BOL>" in elemento.text:
            # Cambiar el texto del cuadro de texto con el número del mapa y el número total de mapas
            elemento.text = "<BOL> Mapa </BOL> {} <BOL> de </BOL> {}".format(i+1, len(mapas))
        # Verificar si el elemento es un cuadro de texto y si su nombre es "Observaciones"
        elif elemento.name == "Observaciones":
            elemento.text = "MAGNA_Colombia_CTM12 EPSG 9377"
        # Verificar si el elemento es un cuadro de texto y si su nombre es "Elaboro"
        elif elemento.name == "Elaboro":
            elemento.text = "Jorge Vallejo - Geologo, Mat Pro. 3880"
    
    # Recorrer el diccionario de fechas
    for nombre_fecha, texto_fecha in fechas.items():
        # Obtener el elemento que tenga el nombre correspondiente
        elemento_fecha = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", nombre_fecha)[0]
        # Cambiar el texto del elemento con el texto correspondiente
        elemento_fecha.text = texto_fecha
    
    # Guardar los cambios en el archivo .mxd original
    mxd.save()
    
    # Ruta de destino para el archivo .mxd con el nuevo nombre
    ruta_destino_mxd = os.path.join(carpeta_destino, nombre + ".mxd")
    
    # Copiar el archivo .mxd con el nuevo nombre a la carpeta de destino
    shutil.copy2(os.path.join(carpeta, mapa), ruta_destino_mxd)
    
    # Crear una lista con los formatos de exportación
    formatos = [".pdf", ".jpg"]
    
    # Recorrer la lista de formatos
    for formato in formatos:
        # Ruta para el archivo con el formato correspondiente
        ruta_formato = os.path.join(carpeta, nombre + formato)
        
        # Exportar el mapa al formato correspondiente con la resolución especificada
        if formato == ".pdf":
            arcpy.mapping.ExportToPDF(mxd, ruta_formato, resolution=resolucion)
        elif formato == ".jpg":
            arcpy.mapping.ExportToJPEG(mxd, ruta_formato, resolution=resolucion)
        
        print("Se ha exportado el mapa {} a {}: {}".format(nombre, formato.upper(), ruta_formato))
    
    # Cerrar el objeto MapDocument
    del mxd

# Imprimir un mensaje de finalización
print("Se han exportado todos los mapas a pdf y jpg con la calidad mejorada")

