from esemeny_class import Esemeny
from storage_functions import saveToFile

esemenyek = []

def createEsemeny(date,name,address,price):
    global esemenyek # Globálisan behívjuk a fenti esemenyek változót (tömböt) h tudjuk módosítani is

    # Készítünk egy új Esemény objektumot
    esemeny = Esemeny(date,name,address,price)
    # Hozzáadjuk az objektumot az esemenyek változóba.
    esemenyek += [esemeny]
    
def delEsemeny(id,filename):
    global esemenyek
    del esemenyek[id]
    saveToFile(filename, esemenyek)