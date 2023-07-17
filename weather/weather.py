import requests
from datetime import datetime
from os.path import exists, dirname, realpath

WEATHER_FILE = dirname(realpath(__file__)) + '/weather.txt'

REFRESH_FREQUENCY = 3600 # seconds - 1 hour

try:
    path = dirname(realpath(__file__)) + '/location.txt'
    location_file = open(path, 'r')
    location = location_file.readlines()[0]
except:
    #print("Missing location.txt file! Create it with your location data defined in wttr.in!")
    pass

# ?1 is the standard daily forecast format only for today.
url ="https://wttr.in/" + location + '?2F'

def ago(seconds):
    diff_srt = 'now'
    if (seconds > 60): diff_srt = str(round(seconds / 60)) + 'm ago'
    if (seconds < 180): diff_srt = str(round(seconds / 60 / 60)) + 'h ago'
    return diff_srt

def get_existing_cache():
    if (exists(WEATHER_FILE)):
        weather_file_content = open(WEATHER_FILE).readlines()
        last_update_str = weather_file_content[0][:-1]
        last_update = datetime.fromisoformat(last_update_str)
        now = datetime.now()
        diff = (now - last_update).total_seconds()
        return {
            'age': diff,
            'last_update_text': 'Last Updated: ' + ago(diff),
            'content': "".join(weather_file_content[1:])
        }
    return False

def update():
    resp = requests.get(url)
    lines = "\n".join(resp.content.decode().splitlines()[1:-1])
    file_with_last_update = datetime.now().isoformat() + "\n" + lines

    # Dummy check if we got a proper response, save to cache!
    if (len(lines) > 4):
        with open(WEATHER_FILE, 'w') as f:
            f.write(file_with_last_update)
    else:
        existing_weather = get_existing_cache()
        if (existing_weather):
            return existing_weather['last_update_text'] + ' - overdue\n' + existing_weather['content']
    return "Last Updated: just now\n" + lines

def get_weather():
    existing_weather = get_existing_cache()
    # Is there a file already?
    if (existing_weather):
        if (existing_weather['age'] < REFRESH_FREQUENCY):
            return existing_weather['last_update_text'] + "\n" + existing_weather['content']
    return update()

# test it!
# print(get_weather())
