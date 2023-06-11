# Exportar mapas a PDF y JPEG con Python y ArcPy

Este código permite exportar varios archivos .mxd a PDF y JPEG con una resolución de 300 dpi, cambiando algunos elementos del diseño del mapa como el número, la fecha y las observaciones.

## Uso

Para usar este código, solo hay que ejecutarlo en un IDE de Python o en la consola de ArcGIS. El código pedirá al usuario que ingrese la carpeta donde están los archivos .mxd y creará una subcarpeta llamada "Exportados" donde guardará los archivos PDF y JPEG. Por ejemplo:

Para poder usar el codigo y que te funcione en todos los mapas debes hacer algunos cambios en el entorno de ArcGis10.8.

## Requisitos

1. Tener instalado ArcGIS Desktop con la licencia de ArcPy.
2. Tener una carpeta con los archivos .mxd que se quieren exportar.
3. Tener los elementos del diseño del mapa con los nombres y etiquetas especificados en el código.

1. Debes asignarse un name a cada TEXTO que quieras modificar, ejemplo yo tengo asignado estos 
![image](https://github.com/onfevs/Exportar_PY/assets/29380120/0bf1d4f1-c004-45e3-9790-77a1f186b95e)
Para FechaAA, y lo debes asi asi para FechaMM y FechaDD.

2. Lo mismo con todos los campos Type Text que quieras cambiar
![image](https://github.com/onfevs/Exportar_PY/assets/29380120/b798ec19-8e93-493d-8843-32a3d8cd17fa)

3. Luego en el scrypt, lo que haces es modificar estos campos, ![image](https://github.com/onfevs/Exportar_PY/assets/29380120/0963e2f5-fe14-42ad-87c8-3e5f8ae11f3a)

4. Le puedes agregar mas elif al script dependiendo de los campos de texto que quieras modificar, recuerda que cada campo texto debe tener un nombre unico, si no se te va a cambiar en varios lugares.
5. Todos los mxds, que tengas en la carpeta deben tener estas modificaciones listas, si no no se aplicaran a tu proyecto. Solo no se ejecuta en esa capa pero el resto que si lo tenga se ejecutara.
6. Los mapas se exportar en una carpeta aparte, pero el mapa en la carpeta origen conserva las modificaciones.
7. Puedes eliminar de ultima los mapas exportados en dicha carpeta o solo copiar y pegar donde desees.

Lo que puedes hacer para que se ejecute el codigo bien, es revisar tu entorno en ArcGis y veriicar las capas que tengas cargadas en el scrypt y colocar los mismos nombres como se muestran en las imagenes o simplemente copiar y pegar de uno que ya tengas listo. 

# El codigo se debe ejecutar desde el intérprete de Python de ArcGIS: En lugar de ejecutar el script desde IDLE, intenta ejecutarlo desde el intérprete de Python que viene con ArcGIS. Normalmente, se encuentra en "C:\Python27\ArcGIS10.8\python.exe". Abre la línea de comandos, navega hasta esa ubicación y ejecuta tu script desde allí


## # Definir la carpeta donde se guardarán los archivos pdf y jpg
salida = r"D:\MiGEO\COPIAS DE SEGURIDAD\IDI-16113X\03_MapasMXD" esta linea de codigo es opcional, solo ingresar la carpeta donde estan los archivos .mxd y se exportan automaticamente los PDF's y JPG's

python exportar_mapas.py Ingrese la carpeta donde están los archivos .mxd: C:\Users\Onfe\Desktop\3X Se ha exportado el mapa Mapa 1_Zona 1.mxd a PDF: C:\Users\Onfe\Desktop\3X\Exportados\Mapa 1_Zona 1.pdf Se ha exportado el mapa Mapa 1_Zona 1.mxd a JPEG: C:\Users\Onfe\Desktop\3X\Exportados\Mapa 1_Zona 1.jpg Se ha exportado el mapa Mapa 2_Zona 2.mxd a PDF: C:\Users\Onfe\Desktop\3X\Exportados\Mapa 2_Zona 2.pdf Se ha exportado el mapa Mapa 2_Zona 2.mxd a JPEG: C:\Users\Onfe\Desktop\3X\Exportados\Mapa 2_Zona 2.jpg Se han exportado todos los mapas a pdf y jpg con la calidad mejorada


## Autor

- OnfeVS
- Instagram: @onfevs
- LinkedIn: https://www.linkedin.com/in/onfevs/

