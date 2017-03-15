import os

# variables
vpath = 'D:/Data/y024716/My Documents/PycharmProjects/Arrek/'
vpattern = '.log'
voutput = 'D:/Data/y024716/My Documents/PycharmProjects/Pliki/logabp_e1.csv'

# function definition
def parsfile ( pfile ):
    fr = open(pfile, "r")
    i = 0
    while True:
        line = fr.readline()
        i = i + 1
        if line == '':
            break
        else:
            if line.find('Timeout expired') != -1:
                linew = str(i) + ' ' + linew + '\n'
                print linew
                fw.write (linew)

    fr.close()
    return;

# main pgm

fw = open(voutput, "w")
for file in os.listdir(vpath):
    if file.endswith(vpattern):
        filepars = vpath + file
        print filepars
        parsfile(filepars)
    else:
        

fw.close()