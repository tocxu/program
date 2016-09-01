def maximum(x,y):
	if x>y:
		return x
	elif x==y:
		return 'The numbers are equal'
	else:
		return y
print maximum(2,3)
print '\n'
#x=int(raw_input('x= ' ))
#y=int(raw_input('y= '))
x=raw_input('x= ')
y=raw_input('y= ')
print maximum(x,y)
print 'Done'

