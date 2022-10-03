#Without numerete function
"""

L1=["Bhendi","chaomin","chicken","biriyani","icecream"]
i=1
for item in L1:
    if i%2!=0: #or we can write- if i%2 is not 0:
        print(f"jarviece please buy {item}")
    i+=1

#output is-
# Jarviece please buy Bhendi
# Jarviece please buy chicken
# Jarviece please buy icecream

"""
#By using numerete function
L1=["Bhendi","chaomin","chicken","biriyani","icecream"]

for index, item in enumerate(L1):
    if index%2==0:
        print(f"Jarviece please buy {item}")

#output is-
# Jarviece please buy Bhendi
# Jarviece please buy chicken
# Jarviece please buy icecream