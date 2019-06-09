tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a\\ cat."

fat_cat ="""
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
 

#while True:
#	for i in ["/","-","|","\\","-","|"]:
#		print "%s\r"%i,


sample = 'This is a sample\'s String \n It is used to tell you difference between %s and %r '

printStyle = "When we use %%s we get : %s and with %%r we get : %r"
print printStyle % (sample,sample)

sampleBack = "Here we will use Back\bSpace Escape Sequence...\nYou must have obsereved that the 'k' in back is omitted by the \\b escape sequence.!\nLet\'s try and have formfeed\fand here we are just below d :P"
print sampleBack

compare = "Let\'s compare the \\\' and \\\" usage in this \"sentence\" !"

print printStyle % (compare,compare)

print '''
	In this, we're printing 
	using single triple quotes 
	instead of triple double quotes """
	to see different style of using triple quotes
	'''


