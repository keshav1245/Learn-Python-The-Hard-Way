from sys import argv

script, user_name , occupation = argv
prompt = '=>'

print "Hi %s, I'm the %s script.\nI heard you're a %s"%(user_name,script,occupation)
print "I'd like to ask you a few questions."
print "Do you like python %s?"%user_name
likes = raw_input(prompt)

print "Where do you live %s ?"%user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print '''

Alright, so you said %r about liking pyhton.
You live in %r. Not sure where it is...
And you have a %r computer. Nice.
'''%(likes,lives,computer)
