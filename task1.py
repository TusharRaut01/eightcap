list=['Maths','English','Science','Marathi','Science']

def myFun(**kwargs):
	for key, list in kwargs.items():
		print("%s == %s" % (key, list))


# Driver code
myFun(Tushar=list, Vishu=list, OM=list,shubham=list,Suyog=list)
