#JASON MODULE
"""
import json

data = '{"var1":"harry", "var2":56}'
parsed = json.loads(data)
print(parsed["var1"])
"""
import json

data2 = {
    "channel_name":"Tech_Lofiz",
    "Equipments":['mobile','laptop','charger'],
    "goals":('scientist',10000),
    "jsbad":False
}

jstry = json.dumps(data2) #json.dumps convert tis dictionary to java comfortable
print(jstry)
print(type(jstry))