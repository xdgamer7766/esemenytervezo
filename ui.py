from config import UI_DASH_CHARS,UI_DASH_COUNT

def decorateStr(s):
    decorator = UI_DASH_CHARS*UI_DASH_COUNT
    return f'{decorator}\n{s}\n{decorator}'
    
    

def getMenuView(items):
    menuStr = ''
    for ind,item in enumerate(items):
        menuStr += f'{ind+1}) {item}\n'

    return decorateStr(menuStr)

options = ['Események megtekintése','Esemény hozzáadása','Esemény törlése','Kilépés']

print(getMenuView(options))