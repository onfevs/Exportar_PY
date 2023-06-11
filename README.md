# Exportar_PY
 Exportar archivos .mxd a PDF y JPG 

Para poder usar el codigo y que te funcione en todos los mapas debes hacer algunos cambios en el entorno de ArcGis10.8.

Aca te los enseno.

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

# El codigo se debe ejecutar desde el intérprete de Python de ArcGIS: En lugar de ejecutar el script desde IDLE, intenta ejecutarlo desde el intérprete de Python que viene con ArcGIS. Normalmente, se encuentra en "C:\Python27\ArcGIS10.8\python.exe". Abre la línea de comandos, navega hasta esa ubicación y ejecuta tu script desde allí


## # Definir la carpeta donde se guardarán los archivos pdf y jpg
salida = r"D:\MiGEO\COPIAS DE SEGURIDAD\IDI-16113X\03_MapasMXD" esta linea de codigo es opcional, solo ingresar la carpeta donde estan los archivos .mxd y se exportan automaticamente los PDF's y JPG's
