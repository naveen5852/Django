from concurrent.futures import ThreadPoolExecutor
import threading
import requests
import time

def myFunc(name):
    print(f'Func Started with {name}\n')
    # time.sleep(5)
    # print('Func Ended')
    count=0
    for i in range(10):
        response = requests.get("http://127.0.0.1:8000")
        print(response.text)
        time.sleep(1)



if __name__ == '__main__':
    myFunc('Nothing')
    with ThreadPoolExecutor(max_workers=10000) as executor:
        for task in range(1):
            t=executor.submit(myFunc,task)
            print(t.result)


    # print('Main func Started\n')
    # t = threading.Thread(target=myFunc,args=['Threading'])
    # t.start()
    # print('Main func ended')


































































































# import requests
# import uuid
# from concurrent.futures import ThreadPoolExecutor, as_completed
#
# url_list = ['http://localhost:8000']
#
#
# def download_file(url, file_name):
#     try:
#         html = requests.get(url, stream=True)
#         # open(f'{file_name}.json', 'wb').write(html.content)
#         return html.status_code
#     except requests.exceptions.RequestException as e:
#         return e
#
#
# def runner():
#     threads = []
#     with ThreadPoolExecutor(max_workers=20) as executor:
#         for url in url_list:
#             file_name = uuid.uuid1()
#             threads.append(executor.submit(download_file, url, file_name))
#
#         for task in as_completed(threads):
#             print(task.result())
#
#
# runner()

