def somefunction(arg1):
	print "This is some arg of some function %s"%arg1



somefunction(10)
somefunction(10+10)
somefunction(10*10)
somefunction(10-20)
somefunction(10.0/4)
somefunction("String Args")

prompt = raw_input("Some input for arg ?")

somefunction(prompt)
prompt = 10

somefunction(prompt+10)
somefunction(prompt*10)
somefunction(prompt/10)
somefunction(prompt-10)
