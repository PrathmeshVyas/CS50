import os
import requests

un = os.getenv("username")
ip = os.getenv("ip")

url = f"http://{ip}/api/{un}/lights/1/state"

requests.put(url, json={"on":False})    