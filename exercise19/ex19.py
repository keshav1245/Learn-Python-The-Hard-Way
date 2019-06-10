#defining the function and giving it a name 
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!"%cheese_count
	print "You have %d boxes of crackers!"%boxes_of_crackers
	print "Man that's enought for a party!"
	print "Get a blanket.\n"

#calling function by giving direct vars
print "We can give the args direct values"
cheese_and_crackers(20,30)

#calling the function by passing variables
print "OR, we can use variables from our script"

amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese,amount_crackers)

#calling function by doing maths
print "We can even do math inside too"
cheese_and_crackers(10+20,5+6)

#calling function by combo of vars and maths
print "And we can combine the two, variables and math"
cheese_and_crackers(amount_cheese+100,amount_crackers+1000)
