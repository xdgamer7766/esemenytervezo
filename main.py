from esemeny_class import Esemeny
from storage_functions import saveToFile
from ui import *

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
    #saveToFile(filename, esemenyek)

options = ['Események megtekintése','Esemény hozzáadása','Esemény törlése','Kilépés']

print(getMenuView(options))

fmenu = int(input()) - 1

if fmenu == 1:
    print(decorateStr(options[fmenu]))    
    for i in esemenyek:
        print(i.name)
if fmenu == 2:
    print(decorateStr(options[fmenu]))
if fmenu == 3:
    print(decorateStr(options[fmenu]))
if fmenu == 4:
    print(decorateStr(options[fmenu]))