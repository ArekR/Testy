import os, datetime

# variables
vpath = 'D:/Data/y024716/My Documents/PycharmProjects/ABP_ERR/'
vpattern = '.log'
voutput = 'D:/Data/y024716/My Documents/PycharmProjects/Pliki/logabp_v31.csv'
vline = 'Timeout expired.  The timeout period elapsed prior to completion of the operation or the server is not responding.' + '\n'
vj = 0

# function definition
def parsfile (pfile):
    fr = open(pfile, "r")
    i = 0
    global vj
    vj = vj + 1
    linew = ''
    while True:
        line = fr.readline()
        if line == '':
            break
        else:
            if line.find('Timeout expired') != -1:
                i = i + 1
    fr.close()
    linew = str(vj) + '|' + str(pfile) + '|' + str(i) + '|' + str(pfile)[-14: -4] + '|'
    print linew
    linew = linew + '\n'
    fw.write(linew)
    return;

def listuj(katalog):
#    print katalog

    lista_elementow = os.listdir(katalog)

    for element in lista_elementow:
        pelna_sciezka = os.path.join(katalog, element)

        if os.path.isdir(pelna_sciezka):
            listuj(pelna_sciezka)
        else:
#            print pelna_sciezka
            parsfile (pelna_sciezka)
    return;

# main pgm
print 'Poczatek: ' + str(datetime.datetime.now())
fw = open(voutput, "w")
listuj(vpath)
fw.close()
print 'Koniec: ' + str(vj) + ' plikow; ' + str(datetime.datetime.now())