#import json
import requests
from datetime import datetime

api_token = 'your_api_token'
api_url_base = 'http://eskimo:8080/sensor/'

headers = {'Content-Type': 'application/json'}
now = datetime.now()

start = datetime.now().isoformat()
measurements = []
measurements.append({"timeStamp":"now", "measurement": 1.12})
measurements.append({"timeStamp":"now", "measurement": 2.23})
measurements.append({"timeStamp":"now", "measurement": 3.45})
measurements.append({"timeStamp":"now", "measurement": 4.67})
measurements.append({"timeStamp":"now", "measurement": 5.89})

stop = datetime.now().isoformat()
content = {"start":start,"stop":stop,"items":measurements}

response = requests.post(api_url_base, headers=headers, json=content)

