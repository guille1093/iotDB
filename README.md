# Arquitectura de red de sensores IoT con persistencia en influx DB 



## Introducción:
En la actualidad, el Internet de las cosas (IoT) ha experimentado un auge significativo, impulsando la necesidad de soluciones eficientes para recopilar, almacenar y analizar grandes volúmenes de datos generados por sensores distribuidos en diferentes entornos. En este trabajo de investigación, se propone la implementación de un sensor IoT que enviará sus mediciones a través de tecnologías de bases de datos optimizadas para aplicaciones de IoT. El flujo de datos se gestionará mediante una instancia de Telegraph que publicará las mediciones de nuestro sensor en un broker MQTT utilizando EMQX. Posteriormente, otra instancia de Telegraph suscrita al broker escribirá los datos en una base de datos de serie de tiempo InfluxDB. Por último, los datos se visualizarán utilizando Grafana, y todo el sistema se desplegará y orquestará en un entorno Docker Compose.

## Bases de Datos Optimizadas para Aplicaciones de IoT:
En el contexto de las aplicaciones de IoT, es fundamental contar con bases de datos optimizadas para manejar grandes volúmenes de datos en tiempo real y facilitar su análisis. En este trabajo, se utilizará InfluxDB como la base de datos principal, ya que está diseñada específicamente para aplicaciones de serie de tiempo y ofrece características como el almacenamiento eficiente de datos de alta velocidad y una consulta ágil basada en marcas temporales. Estas características hacen que InfluxDB sea una opción idónea para el almacenamiento y análisis de datos provenientes de sensores IoT.


# Integración de Tecnologías:

## Sensor IoT: 
Se implementará un sensor IoT emulado capaz de generar y enviar mediciones en tiempo real. Este sensor estará conectado a través de la red para comunicarse con la instancia de Telegraph. 

## Telegraph: 
Se utilizarán dos instancias de Telegraph, una para recibir las mediciones enviadas por el sensor IoT y publicarlas en el broker MQTT. Otra instancia de telegraph que está suscrita al tópico correspondiente en el broker y envía las mediciones hacia la base de datos para su persistencia. Telegraph actuará como el intermediario para la transferencia de datos entre el sensor y la base de datos.
https://www.influxdata.com/time-series-platform/telegraf/

## Broker MQTT: 
EMQX se empleará como el broker MQTT para facilitar la comunicación bidireccional entre el sensor IoT y la instancia de Telegraph encargada de escribir los datos en InfluxDB. El broker MQTT garantiza la entrega confiable de mensajes en un entorno de IoT distribuido. Una de las ventajas de su utilización es que múltiples dispositivos pueden publicar o leer de los tópicos permitiendo una comunicación eficiente utilizando un patrón de diseño publicador / suscriptor en nuestra arquitectura.
https://www.emqx.io/

## InfluxDB: 
La base de datos InfluxDB se utilizará para almacenar y gestionar las mediciones provenientes del sensor IoT. Gracias a su estructura optimizada para datos de serie de tiempo, InfluxDB permite un almacenamiento eficiente y consultas ágiles sobre los datos capturados por el sensor.
https://www.influxdata.com/

## Grafana: 
Se empleará Grafana como herramienta de visualización para representar los datos almacenados en InfluxDB. Grafana permite crear paneles de control personalizados, gráficos interactivos y alertas basadas en los datos provenientes del sensor IoT.
https://grafana.com/

## Docker Compose: 
El entorno de Docker Compose se utilizará para orquestar y desplegar todas las tecnologías y componentes del sistema propuesto como servicios integrados dentro de una misma imagen. La utilización de contenedores facilita la replicación y escalabilidad del sistema en entornos de producción.
https://docs.docker.com/compose/
