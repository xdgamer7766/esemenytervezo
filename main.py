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

if fmenu == 0:
    print(decorateStr(options[fmenu]))
    ujtomb= []   
    for esemeny in esemenyek:
       ujtomb += esemeny.name
    print(getMenuView(ujtomb))
    print("További információkért írja be az esemény sorszámát")
    id = int(input())
    print(f"{esemenyek[id-1].name}\n\t{esemenyek[id-1].date}\n\t{esemenyek[id-1].address}\n\t{esemenyek[id-1].price}")   
    print("debug message")
if fmenu == 1:
    print(decorateStr(options[fmenu]))
    print("debug message")
if fmenu == 2:
    print(decorateStr(options[fmenu]))
    print("debug message")
if fmenu == 3:
    print(decorateStr(options[fmenu]))
    print("debug message")