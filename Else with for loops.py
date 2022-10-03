# Else with for loops
"""
khana=["roti" , "chicken" , "bisket"]

for item in khana:
    print(item)
    break


else:
    print("this forloop ended properly")

# output
# roti
# chicken
# bisket
# this forloop ended properly

# after using break
# output is-
# roti

"""
#LIVE USING OF ELSE IN FOR LOOP

khana=["roti" , "chicken" , "bisket"]

for item in khana:
    if item=="parratha":
        break


else:
    print("this forloop ended properly")

# output is- this forloop ended properly
