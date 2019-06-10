#here we will combine argv and raw_input()

from sys import argv

script,first = argv

print "Hi! %s"%first
age = raw_input("What's your age ? ")
height = raw_input("How tall are you ? ")

print "%s is %d year(s) old and %s ft tall"%(first,int(age),height)
