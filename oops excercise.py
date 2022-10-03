#OOPS EXCERCISE

class Electronics_Devices:
    Types_of_Electronics=5
    def isElectronic(self):
        return f"Yes its in {self.Types_of_Electronics} types of electronics "

class Pocket_gaget(Electronics_Devices):
    No_of_gagets=10
    def isPocketgaget(self):
        return f"Yes I can make {self.No_of_gagets} no.of gagets"

class Phone(Pocket_gaget):
    No_of_phones=4
    def Howmanyphones(self):
        return f"I have {self.No_of_phones} no.of phones"

ohm_digital_store=Electronics_Devices()
amazon=Pocket_gaget()
puranjan_dream_house=Phone()

print(puranjan_dream_house.No_of_phones)