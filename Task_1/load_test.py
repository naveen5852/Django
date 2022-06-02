import multiprocessing
import schedule
import requests
import time

url = 'http://127.0.0.1:8000'

count = 0

def api_request():

    r = requests.get(url)
    print(r.json())




if __name__ == '__main__':
    schedule.every(0.5).seconds.do(api_request)
    while True:
        schedule.run_pending()

    # for i in range(100):
        # multiprocessing.Process(target=api_request(i)).start()


    # schedule.every(.005).minutes.do(api_request())


# p1 = multiprocessing.Process(target=api_request)
# p2 = multiprocessing.Process(target=api_request)
# p3 = multiprocessing.Process(target=api_request)
# p4 = multiprocessing.Process(target=api_request)
# p5 = multiprocessing.Process(target=api_request)
# p6 = multiprocessing.Process(target=api_request)
# p7 = multiprocessing.Process(target=api_request)
# p8 = multiprocessing.Process(target=api_request)
# p9 = multiprocessing.Process(target=api_request)
# p10 = multiprocessing.Process(target=api_request)
#
#
# p1.start()
# p2.start()
# p3.start()
# p4.start()
# p5.start()
# p6.start()
# p7.start()
# p8.start()
# p9.start()
# p10.start()
#
# p1.join()
# p2.join()
# p3.join()
# p4.join()
# p5.join()
# p6.join()
# p7.join()
# p8.join()
# p9.join()
# p10.join()

