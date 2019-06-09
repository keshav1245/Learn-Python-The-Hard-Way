print "How old are you ?",
age = raw_input()
print "How tall are you ?",
height = raw_input()
print "How much do you weight ? ",
weight = raw_input()

#raw_input([prompt])
#If the prompt argument is present, it is written to standard output without a trailing newline. The 
#function then reads a line from input, converts it to a string (stripping a trailing newline), and 
#returns that. When EOF is read, EOFError is raised. Example:

name = raw_input("What is your name? >> ")

print "So, you're %r old, %r tall and your weight is %r."%(age,height,weight)
print ("Your name is : %s"% name + "\n")*10

#getting a number

marks = float(raw_input("Enter your CGPA : "))

print "CGPA is : ",marks

print ("%s \n %r")%(name,name)
