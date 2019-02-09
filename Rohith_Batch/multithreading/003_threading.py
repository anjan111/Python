import threading
import time
print time.time()
def fun(arg):
    for i in range(5):
        print arg
T1 = threading.Thread(target = fun,args =("anjan",))
T1.start()

T2 = threading.Thread(target =fun,args =("rohith",))
T2.start()

print "*************"
T3 = threading.Thread(target =fun,args =("rahaman",))

T3.start()
T1.join()
T2.join()
T3.join()
print "************"
print time.time()

