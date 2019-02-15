"""
This example will access an API, grab a number like hackaday skulls, github
stars, price of bitcoin, twitter followers... and display it on a screen if you can find something that
spits out JSON data, we can display it!
"""
import time
import board
from digitalio import DigitalInOut, Direction
import adafruit_pyportal

# Get wifi details and more from a settings.py file
try:
    from settings import settings
except ImportError:
    print("WiFi settings are kept in settings.py, please add them there!")
    raise

# Set up where we'll be fetching data from
# A very simple glitch.com proxy to massage the Discord widget data!
# Source is at: https://glitch.com/~gamy-scissor
DATA_SOURCE = "https://gamy-scissor.glitch.me/327254708534116352/online.json"
DATA_LOCATION = ["members","total"]

cwd = __file__.rsplit('/', 1)[0]
pyportal = adafruit_pyportal.PyPortal(url=DATA_SOURCE, json_path=DATA_LOCATION,
                           status_neopixel=board.NEOPIXEL,
                           default_bg=cwd+"/discord_background.bmp",
                           text_font="/fonts/Collegiate-50.bdf",
                           text_position=(165, 140), text_color=0xFFFFFF)

# track the last value so we can play a sound when it updates
last_value = 0

while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
        last_value = value
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    time.sleep(10)