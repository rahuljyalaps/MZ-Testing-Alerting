import requests
import os
from prometheus_client import Gauge

class Connectors:
    def __init__(self):
        self.completness = Gauge("Completness", "Couunter for Completness")
        
    def slack_notify(self, type, userid):
        hook = os.environ.get('WEB_HOOK_SLACK_URL')
        message = f'User *{userid}* has some data {type} issue*'
        payload = {'text': message}

        response = requests.post(hook, data=str(payload))
        return response
    
    def prom_counter(self, isIncrement):
        if isIncrement == 1:
            self.completness.inc()
            print(self.completness.collect())
        else: 
            self.completness.dec()
            print(self.completness.collect())
