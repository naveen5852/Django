import requests
import threading

url = "http://127.0.0.1:8000"


def api_request():
    r = requests.get(url)
    data=r.content
    return data

def thread_range(n):
    store = {}
    threads = []
    for i in range(n):
        t = threading.Thread(target=api_request)
        threads.append(t)

    [t.start() for t in threads]

    [t.join() for t in threads]

    for t in threads:
        print(t.result)

if __name__=='__main__':
    print(api_request())
    thread_range(5)