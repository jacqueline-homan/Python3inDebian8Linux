#!/usr/bin/python3

def main():
	n = 42
	s = "this is a {} string".format(n)
	t = "this is a soon-to-be-deprecated %s string in Python 2" % n
	x = (1,2,3)
	y = [1,2,3]
	y.append(5)
	y.insert(0, 7)
	g = 'string'
	print(s)
	print(t)
	print(type(x), x)
	print(y)
	print(type(g), g[2])
	print(type(g), g[2:4]) #this is a slice 

if __name__ == "__main__": main()