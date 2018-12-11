import datetime
import time
import requests
import json
import Adafruit_DHT
from pprint import pprint

#Création objet et envoi de données sur base mongodb toutes les 10s

url = "http://10.92.1.27:3000/thing/create"

while 1:
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    temperature = '{0:0.1f}'.format(temperature)
    value = str(temperature)

    date_time = datetime.datetime.now()
    date = str(date_time)

    #Toutes les valeurs vides dans le Json sont optionnelles dans la base
    #Remplies par l'utilisateur de l'app
    data = json.dumps({
        "name": "test",
        "description": "",
        "type": "",
        "warning_low": "",
        "warning_high": "", 
        "measure_unit": "", 
        "value": value, 
        "date": date
        }) 

    request = requests.post (
        url, 
        data = data,
        headers = {'Content-Type': 'application/json'}    
    )
    pprint(request)
    time.sleep(10)