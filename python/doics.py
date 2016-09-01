import math
def doics(a):
	k=[]
	while a!=0:
		k.insert(0,int(math.fmod(a,2)))
		a=int(a/2)
	return k
print 'Done'
