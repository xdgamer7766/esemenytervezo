from esemeny_class import Esemeny
from storage_functions import saveToFile,loadFromFile
from ui import *
from config import MAIN_SAVE_LOCATION


esemenyek = loadFromFile(MAIN_SAVE_LOCATION)

def createEsemeny(date,name,address,price):
    global esemenyek # Globálisan behívjuk a fenti esemenyek változót (tömböt) h tudjuk módosítani is

    # Készítünk egy új Esemény objektumot
    esemeny = Esemeny(date,name,address,price)
    # Hozzáadjuk az objektumot az esemenyek változóba.
    esemenyek += [esemeny]
    saveToFile(MAIN_SAVE_LOCATION,esemenyek)

def delEsemeny(id):
    global esemenyek
    del esemenyek[id]
    saveToFile(MAIN_SAVE_LOCATION, esemenyek)

#debugging

#createEsemeny('2077-06-20','ANYUUUUU','valahol a világban',2500)
#createEsemeny('2020-07-05','APUUUUUUU','máshol a világban',3500)
#createEsemeny('2018-08-08','ÉHESVAGYOK','harmadhelyen a világban',10000)


#debugging
options = ['Események megtekintése','Esemény hozzáadása','Esemény törlése','Kilépés']

print(getMenuView(options))

fmenu = int(input()) - 1

if fmenu == 0:
    print(decorateStr(options[fmenu]))
    ujtomb= []   
    for esemeny in esemenyek:
       ujtomb += [esemeny.name]    
    print(getMenuView(ujtomb))
    print("További információkért írja be az esemény sorszámát")
    id = int(input())
    print(decorateStr(f"\n{esemenyek[id-1].name}\n\t{esemenyek[id-1].date}\n\t{esemenyek[id-1].address}\n\t{esemenyek[id-1].price}\n\t"))   
    print("debug message")
if fmenu == 1:
    print(decorateStr(options[fmenu]))  
    esemeny_nev = input("Adja meg az esemény nevét")
    esemeny_idopont = input("Adja meg az esemény időpontját kötőjelekkel elválasztva")
    esemeny_helyszin = input("Adja meg az esemény helyszínét")
    esemeny_jegyar = input("Adja meg a jegyárat")
    createEsemeny(esemeny_idopont,esemeny_nev,esemeny_helyszin,esemeny_jegyar)
    print("debug message")
if fmenu == 2:
    print(decorateStr(options[fmenu]))
    delid = input("Adja meg a törlendő esemény sorszámát") -1
    delEsemeny(delid)
    print("debug message")
if fmenu == 3:
    print(decorateStr(options[fmenu]))
    print("debug message")