import logging
import os
import json
from datetime import datetime

from pyowm import OWM
from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp

_LOGGER = logging.getLogger("WeatherApp")

app = HermesApp("WeatherApp", host="mqtt.server",username=os.environ["MQTT_USER"], password=os.environ["MQTT_PASS"])
with open("/data/config.json","r") as f:
    config = json.load(f)

owm = OWM(config["api_key"])
mgr = owm.weather_manager()

@app.on_intent("GetWeather")
async def get_time(intent: NluIntent):
    """Tell the Weather."""
    ob = mgr.weather_at_place(config["default_city"])
    if ob is None: 
        return EndSession("no weather data is available")
    w = ob.weather
    temp = w.temperature("celsius")["temp"]
    return EndSession(f"In {ob.location.name} the temperature is {temp} degrees and the humidity is {w.humidity}")

app.run()
