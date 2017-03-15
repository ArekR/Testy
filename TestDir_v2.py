import os

# variables
vpath = 'D:/Data/y024716/My Documents/PycharmProjects/PlikiABP/'
vpattern = '.log'
voutput = 'D:/Data/y024716/My Documents/PycharmProjects/Pliki/logabp.csv'

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
            if line[48: 49] == '/':
                if line.find('200 0 0') != -1:
                    linew = line[48: 72] + ' ; ' + line[0: 10] + ' ; ' + line[line.find('200 0 0') + 8: 270].strip() + '\n'
                    print linew
                    fw.write (linew)

    fr.close()
    return;

# main pgm

fw = open(voutput, "w")
for file in os.listdir(vpath):
    if file.endswith(vpattern):
        filepars = vpath + file
        parsfile(filepars)
fw.close()