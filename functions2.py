#!/usr/bin/python3

def main():
	testfunc(42, 43, 75)
	optional(22)
	moreoptions(50)
	functionargs(1,2,3, 4, 5, 6)
	functionargs2(1,2,3, 4, 5, 6)
	#namedargs(this=1, that=2, other=42)
	#testfunc2(51)

def testfunc(number, another, onemore):
	print('this is a test function', number, another, onemore)

# Function arguments that are defined must be passed.
# If you need to have them be optional, here's how you'd
# handle that:
def optional(number, another = 22, onemore = 33):
	print('This function has optional args', number)

def moreoptions(number, another = None, onemore = 66):
	print('and so does this function', number, another, onemore)


# *args means you can have a list of optional arguments.
# They will return a tuple
def functionargs(this, that, other, *args):
	print(this, that, other, args)

def functionargs2(this, that, other, *args):
	print(this, that, other)
	for n in args: print(n, end=' ')

# Named Parameters in functions. Here, the caller is naming the
# arguments rather than the receiver. 
# **kwargs stands for keyword args and is actually a dictionary.
# Your named arguments must come first, then your tupled arguments
# (OK this one don't work for me and I don't understand why)
#def namedargs(this, that, other, *args,**kwargs):
#	print('This is a function with named args', kwargs['this'], kwargs['that'], kwargs['other'])

#def testfunc2(this, that, other, *args, **kwargs):
#	for k in kwargs:
#		print(k, kwargs[k])




if __name__ == "__main__": main()
