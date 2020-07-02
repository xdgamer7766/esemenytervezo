from esemeny_class import Esemeny

def saveToFile(self, filename, esemenyek):
    data = ""
    for i in esemenyek:
        data += i.convertToString()
        data += ';' 
    f = open(filename, 'w')
    f.write(data)

def loadFromFile(filename):
    f = open(filename)
    # Letisztítjuk a szöveget és eltároljuk a contentben
    content = f.read().strip().replace("\n", "").replace("\r", "")
    # Bezárjuk a fájlhoz való kapcsolatot.
    f.close()

    # esemény stringek (még nincs felbontva tulajdonságra)
    esemenystrs = content.split(";")

    # Kimenő végső esemény tömb definiálása
    esemenyarr = []

    # darabonként átmegyünk rajta, felbontjuk, és elkiszítjük az esemény objektumot.
    for esemenystr in esemenystrs:
        # Biztonsági ellenőrzés h ne legyen üres az esemenystr (ha üres, skippeli a többi kódot)
        if esemenystr.strip() == '':
            continue

        # Esemény string feldarabolása
        properties = esemenystr.split(".")

        # Esemény rekreálása; újra elkészítése
        jelenlegiEsemeny = Esemeny(properties[0], properties[1], properties[2], properties[3])

        # Esemény tömbhöz hozzáadás
        esemenyarr += [jelenlegiEsemeny]
    # Befejeztük az összeset

    #Esemény tömb visszaadása
    return esemenyarr
        

