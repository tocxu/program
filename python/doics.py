#coding=utf-8
import math
def doics(a):
	k=[]
	while a!=0:
		k.insert(0,int(math.fmod(a,2)))
		a=int(a/2)
	return k

a=int(raw_input("nhập số: "))
print 'k: ',doics(a)
print 'Done'
