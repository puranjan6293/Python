#Use of time module
#It is use to find the excution time of a pogram
"""
import time
initial=time.time()
k=0

while(k<45):
    print("harry bhai jindabad")
    k+=1
print("while loop ran in:",time.time()-initial,"seconds")

initial2=time.time()

for i in range(45):
    print("harry bhai jindabad")
print("for loop ran in:",time.time()-initial2,"seconds")

"""
#from harry sir
import time
initial = time.time()

k = 0
while(k<45):
    print("This is harry bhai")
    time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 =time.time()
for i in range(45):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "Seconds")


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)