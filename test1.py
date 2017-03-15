# This prints out: A list: [1, 2, 3]
#mylist = [0,1,2,3,5,7]
#print "A list: %s" % mylist

print "Start: wczytanie pliku"
fr = open('test1.txt', "r")
fw = open('test2.txt', "w")
line = fr.readline()
print line
fr.close()
fw.close()