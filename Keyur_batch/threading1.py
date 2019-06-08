import threading
import time
print "start time : ",time.time()
def  fun(name = "anjan"):
    for i  in range(10):
        print i," time ", name
        time.sleep(1)
t1 = threading.Thread(target = "fun",args=("hello",))
print"*************"

t2 = threading.Thread(target = "fun",args=("hai",))
t1.start()
t2.start()
print "stop time : ",time.time()       
