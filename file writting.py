"""
#How to use write function

f=open("harry.txt","w") #Here w is used for writting function
f.write("harry bhai jinda bad")
f.close()

#Note- write mode means, jo file me hai use khali kardo aur usme new given line likh do
#it will ad 'harry bhai jinda bad' in a new file or replace in a given existing file

#Append function

f=open("harry.txt","a") #here "a" is use for append
f.write("Harry bhai jindabad\n")
f.close()

#Note- append mode means jo file me hai uske sath ye new line jod do


#How to print no of characters?
f=open("harry.txt","w")
a=f.write("Harry bhai jindabad\n")
print(a)

#output is 20


#Handle read and write both

f=open("harry.txt","r+")
print(f.read())
#output is harry bhai jindabad
#because it is aready had in harry.txt file
#now if we want to add something in this file than we have to write

f.write("Harry bhai is a good person")

#now if we check the harry.txt file than we can see a new line is added
#that are
# Harry bhai jindabad
# Harry bhai is a good person

"""

