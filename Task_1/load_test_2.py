import concurrent.futures
import asyncio

import requests
from concurrent.futures import ThreadPoolExecutor

url = 'http://127.0.0.1:8000'


def api_request():
    r = requests.get(url)
    print(r.json())

pool = concurrent.futures.ProcessPoolExecutor()

loop=asyncio.get_running_loop()
x= await loop.run_in_executor(pool,api_request)

# api_request()