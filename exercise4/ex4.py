#made variable name cars and gave value 100
cars = 100
#made variable name space_in_car and gave value 4.0
space_in_car = 4.0
#made variable name drivers and gave value 30
drivers = 30
#made variable name passengers and gave value 90
passengers = 90
#made variable name cars_not_driven and its val will be no of cars we have - no of drivers 
#because only the one who knows how to drive can drive the car, if drivers are 30 then only 30 cars will go
cars_not_driven = cars - drivers
#made variable name cars_driven and gave value equal to number of drivers
cars_driven = drivers
#made variable name passengers and gave value number of cars into space in each car
carpool_capacity = cars_driven * space_in_car
#made variable name average_passengers_per_car and its value Will be number of passengers divided by number of cars
average_passengers_per_car = passengers/cars_driven

print "There are ",cars," cars available"
print "There are only ",drivers," drivers available"
print "There will be ",cars_not_driven," empty cars today"
print "We can transport ",carpool_capacity," people today"
print "We have ",passengers," passengers to capool today"
print "We need to put about ",average_passengers_per_car," in each car."
