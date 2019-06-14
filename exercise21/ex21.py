def add(a,b):
	print "ADDING %d and %d"%(a,b)
	return a + b

def subtract(a,b):
	print "SUBTRACTING %d and %d"%(a,b)
	return a - b

def multiply(a,b):
	print "MULTIPLYING %d and %d"%(a,b)
	return a * b

def divide(a,b):
	print "DIVIDING %d and %d"%(a,b)
	return a/b

print "Let's do some maths with just functions..."

age = add(30,5)
height = subtract(78,4)
weight = multiply (90,2)
iq = divide(100,2)

print "\nAGE : %d, HEIGHT :  %d, WEIGHT : %d, IQ : %d\n"%(age,height,weight,iq)

print "Here is a puzzle..."

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes : ", what , " Can you do it by hand ???"

what2 = add(age,divide(height,subtract(weight,multiply(iq,2))))

print "That becomes : ", what2 , " Can you do it by hand ???"
