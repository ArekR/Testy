import os

for file in os.listdir('D:/Data/y024716/My Documents/PycharmProjects/PlikiABP/ngapiis01'):
    if file.endswith(".log"):
        fileold = 'D:/Data/y024716/My Documents/PycharmProjects/PlikiABP/ngapiis01/' + file
        filenew = 'D:/Data/y024716/My Documents/PycharmProjects/PlikiABP/ngapiis01/a2' + file
        os.rename(fileold, filenew)
        print(file)