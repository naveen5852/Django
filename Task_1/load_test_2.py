import concurrent.futures
import asyncio

import requests
from concurrent.futures import ThreadPoolExecutor

url = 'http://127.0.0.1:8000'


def api_request():
    r = requests.get(url)
    print(r.json())

api_request()