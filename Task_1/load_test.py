import concurrent.futures
import multiprocessing

import requests
from concurrent.futures import ThreadPoolExecutor

url = 'http://127.0.0.1:8000'

threads=20

def api_request():
    r = requests.get(url)
    print(r.json())

p1 = multiprocessing.Process(target=api_request)
p2 = multiprocessing.Process(target=api_request)
p3 = multiprocessing.Process(target=api_request)
p4 = multiprocessing.Process(target=api_request)

p1.start()
p2.start()
p3.start()
p4.start()
p1.join()
p2.join()
p3.join()
p4.join()

#
# with ThreadPoolExecutor(max_workers=threads) as executor:
#     f = executor.submit(api_request)
#     print(f)
#     data = f.result()
#     print(data)
#
