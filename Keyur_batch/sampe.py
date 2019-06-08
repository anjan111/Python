import thread
import time
print "start time : ",time.time()
def  fun(name = "anjan"):
    for i  in range(10):
        print i," time ", name
        time.sleep(1)
fun("hello")
print"*************"
fun("hai")
print "stop time : ",time.time()       
