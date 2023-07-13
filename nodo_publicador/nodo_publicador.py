import time
import json
import random
import paho.mqtt.client as mqtt


def generate_random_temperature(sensor_data):
    """
    Función que genera una temperatura aleatoria y actualiza el diccionario sensor_data con la nueva medición.
    """
    sensor_data["timestamp"] = time.time(
    )  # Se agrega la marca de tiempo actual al diccionario sensor_data
    # Se obtiene la temperatura actual del diccionario
    current_temp = sensor_data["temperature"]

    # Se genera una diferencia aleatoria entre 0 y 0.5
    difference = random.uniform(0, 5)

    # Se decide aleatoriamente si se suma o resta la diferencia a la temperatura actual
    add_or_substract = random.randint(0, 1)

    if add_or_substract and current_temp < 100:  # Si add_or_substract es 1 y la temperatura actual es menor a 35
        # Se suma la diferencia a la temperatura actual
        sensor_data["temperature"] += difference
    elif current_temp > 25:  # Si la temperatura actual es mayor a 10
        # Se resta la diferencia a la temperatura actual
        sensor_data["temperature"] -= difference


def on_connect(client, userdata, flags, rc):
    print("Conectado al Broker MQTT")


def main():
    """
    Función principal que genera mediciones aleatorias de temperatura y las publica en un tópico MQTT.
    """

    # Configuración del cliente MQTT
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("localhost", 1883, 60)

    # Se crea un diccionario con los datos del sensor
    sensor_data = {
        "device_id": "e2e78334",
        "client_id": "c03d5155",
        "sensor_type": "Temperature",
        "temperature": 25,
        "timestamp": time.time()
    }

    while True:
        # Genera una nueva temperatura aleatoria
        generate_random_temperature(sensor_data)

        # Imprime la medición en la consola
        print("Medición generada: " + str(sensor_data))

        # Se publica la medición en formato JSON en el tópico MQTT
        client.publish("telegraf/telegrafinput/Temperature",
                       json.dumps(sensor_data))

        # Se imprime la medición en la consola
        print("Medición enviada: " + str(sensor_data))

        # Espera 0.5 segundos antes de generar la siguiente medición
        time.sleep(0.5)


if __name__ == '__main__':
    main()
