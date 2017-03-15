import os

# variables
vpath = 'D:/Data/y024716/My Documents/PycharmProjects/Arrek/'
vpattern = '.log'
vline = 'Timeout expired.  The timeout period elapsed prior to completion of the operation or the server is not responding.' + '\n'
vj = 0

# function definition
def parsfile (pfile):
    fr = open(pfile, "r")
    i = 0
    ii = 0
    global vj
    linew = ''
    while True:
        line = fr.readline()
        i = i + 1
        if line == '':
            break
        else:
            if line.find('Timeout expired') != -1:
                if (vj == 0) or ((i - ii > 19) and (line == vline)) or (line != vline):
                    vj = vj + 1
                    linew = str(vj) + ' ' + str(i) + ' ' + str(i - ii) + ' ' + line
                    ii = i
                    print linew
    fr.close()
    return;

def listuj(katalog):
    print katalog

    lista_elementow = os.listdir(katalog)

    for element in lista_elementow:
        pelna_sciezka = os.path.join(katalog, element)

        if os.path.isdir(pelna_sciezka):
            listuj(pelna_sciezka)
        else:
            print pelna_sciezka
            parsfile (pelna_sciezka)
    return;

# main pgm
listuj(vpath)