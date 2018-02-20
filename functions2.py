#!/usr/bin/python3

def main():
	testfunc(42, 43, 75)
	optional(22)
	moreoptions(50)
	functionargs(1,2,3)

def testfunc(number, another, onemore):
	print('this is a test function', number, another, onemore)

# Function arguments that are defined must be passed.
# If you need to have them be optional, here's how you'd
# handle that:
def optional(number, another = 22, onemore = 33):
	print('This function has optional args', number)

def moreoptions(number, another = None, onemore = 66):
	print('and so does this function', number, another, onemore)



def functionargs(this, that, other, *args):
	print('This is a test function with the *args thingie')



if __name__ == "__main__": main()
