from sys import argv

script , filename = argv

file_open = open(filename)

print "Contents of the %s file are : \n"%filename

print file_open.read()
