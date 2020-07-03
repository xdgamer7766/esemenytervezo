
dashes = 60
print('-'*dashes)
print('1) Események megtekintése')
print('2) Esemény hozzáadása')
print('3) Esemény törlése')
print('4) Kilépés')
print('-'*dashes)


def decorateStr(s):
    ...

def getMenuView(items):
    ...




while False:
    option = input('Választás: ')
    available_options = ['1','2','3','4']
    # Ha a kiválasztott opció nincs benne a available_options tömbbe, nem folytatjuk a loop-ot, az elejére megyünk, és ujra megkérdezzük.
    if option not in available_options:
        print('Hibás választás!')
        continue
    
    if option == '1':
        print(getEventDisplayStr())
        # Todo: Wait for more input, multiple pages, 5 items per page, sorted by date
    if option == '2':
        #Todo: add event ui
        ...
    if option == '3':
        #Todo: Get event id and remove based on that.
        ...
    if option == '4':
        break