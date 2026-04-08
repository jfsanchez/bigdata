#  Creación de Alertas en Databricks

Este tutorial te guiará a través del proceso de creación de alertas en Databricks para monitorear tus datos y recibir notificaciones cuando se cumplan ciertas condiciones.

##  Pasos para crear una alerta

1.  **Navegar a la sección de Alertas**

    Para comenzar, dirígete a la sección de **SQL** en el menú lateral y selecciona la opción **Alerts** (Alertas).

![alt text](imglotf/image-2.png)

2.  **Crear la consulta**

    Haz clic en el botón para crear una nueva alerta. A continuación, define la consulta SQL que recuperará los datos que deseas monitorear. Una vez escrita, ejecuta la consulta para verificar que devuelve los resultados esperados.

![alt text](imglotf/image-1.png)

3.  **Especificar la condición de la alerta**

    Especifica la condición que disparará la alerta basándote en los resultados de tu consulta. Por ejemplo, puedes configurar la alerta para que se active cuando el valor de una columna específica supere un umbral determinado.

![alt text](imglotf/image.png)
![alt text](imglotf/image-3.png)

4.  **Configurar el destino de la notificación**

    Introduce la dirección de correo electrónico que recibirá la alerta.
    > **Nota:** Solo funcionará con correos electrónicos que estén vinculados al *workspace* donde se está ejecutando la tarea.

![alt text](imglotf/image-4.png)

5.  **Establecer la frecuencia de actualización**

    Establece la frecuencia con la que Databricks debe volver a ejecutar la consulta para verificar la condición. Finalmente, guarda y activa la alerta.

![alt text](imglotf/image-5.png)

6.  **Verificar la notificación**

    Una vez que la condición de la alerta se cumpla, recibirás una notificación por correo electrónico como la que se muestra a continuación.

![alt text](imglotf/image-8.png)

![alt text](imglotf/image-9.png)