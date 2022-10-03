# ELSE AND FINALLY IN TRY EXCEPT
f1 = open("harry.txt")
try:
   f= open("dosent exist")

except Exception as e:
    print(e)

else:
    print("this will run if exception is not running")

finally:
    print("run this anyway...")
    f1.close()

print("important things")

#output is
# [Errno 2] No such file or directory: 'dosent exist'
# important things

#Finally use-
