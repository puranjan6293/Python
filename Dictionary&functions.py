"""

d1={}
print(d1)

#output is {}


d2={"subham":"chicken","priti":"roti","rohit":"dall","dog":"everything"}
print(d2)

#output is subham:chicken:,priti:roti,rohit:dall,dog:everything


d2={"subham":"chicken","priti":"roti","rohit":"dall","dog":"everything"}
print(d2["priti"])

#output is roti
#here question function used



d2={"subham":"chicken","priti":"roti","rohit":"dall","dog":{"B":"poti","L":"rice","D":"susu"}}

print(d2["dog"]["B"])

#output is poti
#Means we can use dictionary under dictionary

"""
#Some other important functions

d2={"subham":"chicken","priti":"roti","rohit":"dall","dog":{"B":"poti","L":"rice","D":"susu"}}
#print(d2.get("rohit"))
#output is dall

#d2.update({"leena":"tofee"})
#print(d2)
#output is {'subham': 'chicken', 'priti': 'roti', 'rohit': 'dall', 'dog': {'B': 'poti', 'L': 'rice', 'D': 'susu'}, 'leena': 'tofee'}

#print(d2.keys())
#output is dict_keys(['subham', 'priti', 'rohit', 'dog'])

#print(d2.items())
#dict_items([('subham', 'chicken'), ('priti', 'roti'), ('rohit', 'dall'), ('dog', {'B': 'poti', 'L': 'rice', 'D': 'susu'})])

#these all related to the dictionary function in python