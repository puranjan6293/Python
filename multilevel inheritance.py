#MULTILEVEL INHERITANCE

class Dad:
    Basketball=5

class Son(Dad):
    dance=3
    def isdance(self):
        return f"Yes I dance {self.dance} no.of times"

class Grandson(Son):
    dance = 6

    def isdance(self):
        return f"Yes I dance verry fast in {self.dance} no.of times"
#SOME INSTANCES-
darry=Dad()
larry=Son()
harry=Grandson()

#LETS USE SOME PRINT STATEMENT

print(harry.isdance())
#output is- Yes I dance verry fast in 6 no.of times
print(harry.Basketball)
"""output is- 5 because humne grandson ka basketball nehi define 
kiye hne so harry apne grandfather or daryy ka basket ball leke aayega"""

