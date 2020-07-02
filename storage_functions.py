def saveToFile(self, filename, esemenyek):
    data = ""
    for i in esemenyek:
        data += i.convertToString()
        data += ';' 
    f = open(filename, 'w')
    f.write(data)