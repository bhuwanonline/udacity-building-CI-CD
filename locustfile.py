import time
from locust import  task, between
from locust.contrib.fasthttp import FastHttpUser

class MyUser(FastHttpUser):
  host = r'https://udacity-flask-ml-service.azurewebsites.net:443/predict'

  @task
  def prediction(self):
    post_data = {
        "CHAS":{
            "0":0
        },
        "RM":{
            "0":6.575
        },
        "TAX":{
            "0":296.0
        },
        "PTRATIO":{
            "0":15.3
        },
        "B":{
            "0":396.9
        },
        "LSTAT":{
            "0":4.98
        }
    }
    
    post_headers = {r'Content-Type': r'application/json'}


    response = self.client.request(method='POST', url=self.host, json=post_data )



    print("Response status code:", response.status_code)
    print("Response text:", response.text)
