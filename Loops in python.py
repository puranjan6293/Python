"""

list1=["Harry","Marry","Carry","Terry","Derry"]
#print(list1)
#or we can write
#print(list1[0],list1[1],list1[2],list1[3],list1[4])

#But if we use for loop function here than,

for item in list1:
    print(item)
#output is   Harry

Marry
Carry
Terry
Derry


#list in list

list1=[["harry",2],["marry",50],["carry",40],["darry",230]]
for item in list1:
    print(item)
#output is
['harry', 2]
['marry', 50]
['carry', 40]
['darry', 230]

#or we can modify this
#list in list

list1=[["harry",2],["marry",50],["carry",40],["darry",230]]
for item,lollypop in list1:
    print(item,lollypop)

#output is
harry 2
marry 50
carry 40
darry 230


#or we can also write this in
#list in list

list1=[["harry",2],["marry",50],["carry",40],["darry",230]]
for item,lollypop in list1:
    print(item,"with lollypop is",lollypop)

#output is
harry with lollypop is 2
marry with lollypop is 50
carry with lollypop is 40
darry with lollypop is 230

"""
