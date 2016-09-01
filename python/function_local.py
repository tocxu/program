x=50
print x
def func(x):
	print 'x is', x
	x=2
	print 'Changed local x to', x
func(x)
print 'x is still',x

print 'Done'
