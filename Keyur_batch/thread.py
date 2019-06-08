import thread
import time
print "start time : ",time.time()
def  fun(name = "anjan"):
    for i  in range(10):
        print i," time ", name
        time.sleep(1)
thread.start_new_thread(fun,('hello',))
print"*************"
thread.start_new_thread(fun,('hai',))
print "stop time : ",time.time()       
