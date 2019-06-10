# import modules
from sys import argv
#giving variable name to argv
script, filename = argv
#opening a file 
txt = open(filename)
#printing string
print "Here's your file %r"%filename
#function on file 
print txt.read()
#printing
print "Type filename again : "

#user input
file_again = raw_input("<^>")
#opening a file
txt_again = open(file_again)
#function on a file
print txt_again.read()

close(txt)
close(txt_again)

