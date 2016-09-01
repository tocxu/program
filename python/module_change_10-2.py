#coding:utf-8
import math,doics
a=int(raw_input("Nhap a: "))
b=int(raw_input('Nhap b: '))

c=doics.doics(a)
d=doics.doics(b)

if len(c)>len(d):
	for i in range (len(c)-len(d)):
		d.insert(0,0)
else:
	for i in range(len(d)-len(c)):
		c.insert(0,0)
print a,c
print b,d

k=[]
n=0
for i in range (len(c)+1):
	if (i != len(c)):
		n1=int((c[len(c)-i -1] + d[len(c)-i-1]+n)/2)
		e= int(math.fmod(c[len(c)-i-1]+d[len(c)-i-1]+n,2))
		k.insert(0,e)
	else:
		if n==1:
			k.insert(0,n)
	n=n1
print 'a=b: '
print k
print 'Done'


