"""
#More about python files
#using tell function

f=open("harry.txt")
print(f.tell()) #we can find the file pointer by using this f.tell function
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.close()

#output is
0
Harry bhai jindabad

21
Harry bhai is a good person
48


#how to reset the pointer
#use of f.seak() function

f=open("harry.txt")
print(f.readline())
f.seek(10) #file ko kaha se padhna start kare f.seak decide karta hai
print(f.readline())
f.close()
#output is
Harry bhai jindabad

 jindabad
"""
