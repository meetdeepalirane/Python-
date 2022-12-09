
import os
from threading import Thread
def squared(num):
    print("square of {} is {}".format(num,num*num))
def cube(num):
    print("cube of {} is {}".format(num,num*num*num))


if __name__=="__main__":

    t1=Thread(target=squared,args=(10,))
    t2=Thread(target=cube,args=(15,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
