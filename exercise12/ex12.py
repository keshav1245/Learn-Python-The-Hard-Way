age = raw_input("How old are you ? ")
height = raw_input("How tall are you ? ")
weight = raw_input("How much do you weigh ? ")

print "So, you're %r old, %r tall and your weight is %r"%(
	age,height,weight)


#READING pydoc open, file

#OPEN

##open(name[, mode[, buffering]])
##open(file,mode)
## Eg. f = open("demofile.txt", "r")
##mode:	A string, define which mode you want to open the file in:
###"r" - Read - Default value. Opens a file for reading, error if the file does not exist

###"a" - Append - Opens a file for appending, creates the file if it does not exist

###"w" - Write - Opens a file for writing, creates the file if it does not exist

###"x" - Create - Creates the specified file, returns an error if the file exist

###In addition you can specify if the file should be handled as binary or text mode

###"t" - Text - Default value. Text mode

###"b" - Binary - Binary mode (e.g. images)


## FILE
###file(name[, mode[, buffering]])
### Operations : tell() , seek() , write() , truncate() , readline() , readlines() , read() , flush() , 
### close() , fileno() , __setattr__('name','value') , __repr__ , __getattr__('name') , __exit__ , 
### __delattr__('name')


 

