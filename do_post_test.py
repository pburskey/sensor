#import json
import requests
from datetime import datetime

api_token = 'your_api_token'
api_url_base = 'http://eskimo:8080/sensor/'

headers = {'Content-Type': 'application/json'}
now = datetime.now()

start = datetime.now().isoformat()
measurements = []
measurements.append(1.12)
measurements.append(2.23)
measurements.append(3.45)
measurements.append(4.67)
measurements.append(5.89)


stop = datetime.now().isoformat()
content = {"start":start,"stop":stop,"measurements":measurements}

response = requests.post(api_url_base, headers=headers, json=content)

