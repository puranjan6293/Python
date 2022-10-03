#PICKLE MODULE
"""
import pickle
#pickling a python object
cars = ["maruti", "ferari", "honda"]
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()

"""

#dipickling a object

import pickle
file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)