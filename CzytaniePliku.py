print "Start: wczytanie pliku 'D:/Data/y024716/My Documents/PycharmProjects/Pliki/u_ex160501.log'"
fr = open('D:/Data/y024716/My Documents/PycharmProjects/Pliki/u_ex160501.log', "r")
fw = open('D:/Data/y024716/My Documents/PycharmProjects/Pliki/log.txt', "w")

i = 0
while True:
    line = fr.readline()
    i = i + 1
    if line == '':
        break
    else:
        if line[48 : 49] == '/':
            if line.find('200 0 0') != -1:
                linew = str(i) + ' ; ' + line[48: 72] + ' ; ' + line[0: 10] + ' ; ' + line[line.find('200 0 0')+8 : 270].strip() + '\n'
                print linew
                #fw.write (linew)

fr.close()
fw.close()