# Autor : Billy Daniel Hanover Tapia

## Crear un Dashboard

1. En el panel principal en la parte izquierda seleccionamos ``Dashboards``
2. Dentro de ``Dashboards`` seleccionamos ``Create Dashboard``

![image.png](./databricks-creacion-dashboard/image1.png)

3. Vamos a ``Data`` y seleccionamos ``Add data source``.  
   Existen varias formas de crear un Dashboard:  
   - **Create from SQL**: permite crear un dashboard directamente desde una consulta SQL, mostrando los resultados en visualizaciones.  
   - **Upload File**: permite subir un archivo externo (como CSV o Excel) y usarlo como fuente de datos para el dashboard.  
   - **Add Data Source**: selecciona una tabla o vista ya existente dentro de tu base de datos, que será la fuente de datos para el dashboard.  

   Para este tutorial, escogemos **Add Data Source**, ya que es la forma más directa y fácil de comenzar.

![image-2.png](./databricks-creacion-dashboard/image2.png)

4. Le damos a **Confirm** y se cargarán los datos. 

### Creación de wigets

1. Para crear wigets vamos a ``Untitled page`` y ``Add Global filters`` para poder filtrar correctamente lo que queramos
   
   La página de Global Filters en un dashboard de Databricks Lakeview se utiliza para crear filtros que afectan a todos los widgets y páginas del dashboard al mismo tiempo

![image-3.png](./databricks-creacion-dashboard/image3.png)

2. Para agregar un grafico seleccionamos en ``Add a visualization``  que se encuentra en la parte inferior central de canvas
   
![image-4.png](./databricks-creacion-dashboard/image4.png)

3. Se abrirá un ``wiget``  donde al darle click derecho puedes: Eliminar, copiar , descargar, clonar , entre otras opciones 

![image-5.png](./databricks-creacion-dashboard/image5.png)

4. Para editar correctamente un widget, ten en cuenta lo siguiente:  
    - 1 Puedes filtrar el contenido de los widgets utilizando filtros globales o específicos.
    - 2 Los widgets pueden ser gráficos, tablas, textos o filtros.
    - 3 Al editar un widget puedes:
        - Seleccionar el dataset que quieres visualizar o filtrar.
        - Elegir el tipo de visualización (gráfico de barras, líneas, tabla, etc.).
        - Configurar los ejes X e Y, y los campos a mostrar.
        - Asignar colores a los valores de una columna para mejorar la interpretación visual.
        - Acceder a otras opciones como duplicar, eliminar o descargar el widget.
    - 4 Finalmente este es el resultado de hacer los pasos anteriores

![image-6.png](./databricks-creacion-dashboard/image6.png)

5. Despues de añadir un nombre tanto a la pagina como al Dashboard
6. Vamos a ``publish`` para configurar como quiero que se comparta mi ``Dashboard``

![image-7.png](./databricks-creacion-dashboard/image7.png)

7. Al publicar, puedes elegir si los visualizadores usan tus permisos de datos (“shared data permission”) o los suyos propios (“individual data permission”). Escogemos (“shared data permission”) luego ``publish``

![image-8.png](./databricks-creacion-dashboard/image8.png)

