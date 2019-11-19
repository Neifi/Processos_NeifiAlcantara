from multiprocessing import Process
import datetime
import time
import os
from multiprocessing import Value

a = Value('i', 5)

datetime.datetime(2009, 1, 6, 15, 8, 24)

def t(s):
    while True:
        time.sleep(s)
        print(datetime.datetime.now())
        


def main():
    process = Process(target=t, args=(1, ))
    process.start()
    for i in range(10):
        time.sleep(0.5)
        print(process.pid)
    #process.terminate()
    print("FIN")
    print(a.value)
      
       

main()
