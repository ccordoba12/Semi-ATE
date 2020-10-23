import json
from ATE.utils.mqtt_router import MqttRouter
import aiomqtt


class ConnectionHandler:

    """ handle connection """

    def __init__(self, host, port, mqtt_client_id, logger):
        self.mqtt_client = aiomqtt.Client(client_id=mqtt_client_id)
        self.mqtt_client.reconnect_delay_set(10, 15)
        self.log = logger
        self.host = host
        self.port = port
        self.router = MqttRouter()

    def init_mqtt_client_callbacks(self, on_connect, on_message, on_disconnect):
        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_message = on_message
        self.mqtt_client.on_disconnect = on_disconnect

    def start_loop(self):
        self.mqtt_client.connect_async(self.host, self.port)
        self.mqtt_client.loop_start()

    async def stop_loop(self):
        await self.mqtt_client.loop_stop()

    def create_message(self, msg):
        return json.dumps(msg)

    def decode_message(self, message):
        return self.decode_payload(message.payload)

    def decode_payload(self, payload_bytes):
        try:
            payload = json.loads(payload_bytes)
            return payload
        except json.JSONDecodeError as error:
            self.log.error(f'{error}')

        return None

    def set_last_will(self, topic, msg):
        self.mqtt_client.will_set(topic, msg, 0, False)

    def subscribe(self, topic):
        self.mqtt_client.subscribe(topic)

    def publish(self, topic, payload=None, qos=0, retain=False):
        self.mqtt_client.publish(topic, payload, qos, retain)

    def register_route(self, route, callback):
        self.router.register_route(route, callback)

    def subscribe_and_register(self, route, callback):
        self.subscribe(route)
        self.router.register(route, callback)

    def unsubscribe(self, topic):
        self.mqtt_client.unsubscribe(topic)

    def unregister_route(self, route, callback):
        self.router.unregister_route(route, callback)

    # TODO: remove if not needed
    def send_log(self, message):
        pass