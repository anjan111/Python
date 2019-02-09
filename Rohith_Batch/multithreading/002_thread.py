import thread
import time
print time.time()
def fun(arg):
    for i in range(5):
        print arg
thread.start_new_thread(fun,("anjan",))
print"**************"
thread.start_new_thread(fun,("rohith",))
print "*************"
thread.start_new_thread(fun,("rahaman",))
print "************"
print time.time()
