print "Start: wczytanie pliku 'D:\Data\y024716\My Documents\PycharmProjects\PlikiIVVR\07282002.422'"
fr = open('D:/Data/y024716/My Documents/PycharmProjects/PlikiIVVR/07282002.422', "r")
fw = open('D:/Data/y024716/My Documents/PycharmProjects/PlikiIVVR/07282002v2.422', "w")

i = 0
j = 0
while True:
    line = fr.readline()
    i = i + 1
    if line == '':
        break
    else:
        if line.find('0.00,,,"","') == -1:
            linew = str(i) + '>> ' + line
        else:
            linew = str(i) + ' ; ' + line[line.find('0.00,,,"","')+11 : -2]
            if len(linew) > 35:
                j = j + 1
                #linew = linew.encode('utf-8-sig')
                linew = str(len(linew)) + ' ' + str(j) + ' ' + linew
                print linew


    #fw.write (linew)


fr.close()
fw.close()