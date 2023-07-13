import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
    print("Conectado al Broker MQTT")
    client.subscribe("telegraf/telegrafinput/#")


def on_message(client, userdata, msg):
    # Limpiar la pantalla
    print("\033c")
    # Obtener la temperatura actual del mensaje recibido
    if "Temperature" in msg.topic:
        payload = json.loads(msg.payload.decode("utf-8"))
        temperatura = payload["temperature"]

        # Redondear la temperatura a dos decimales
        temperatura = round(temperatura, 2)

        # Mostrar la temperatura actual
        print("Temperatura actual: {:.2f}".format(temperatura))

        # Verificar si la temperatura excede los 60°C
        if temperatura > 60:
            print(
                "¡Alerta! La temperatura ha excedido los 60°C: {:.2f}".format(
                    temperatura
                )
            )


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
