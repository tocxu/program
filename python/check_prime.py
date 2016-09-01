import math
def check_prime(a):
	check =1
	n= int(math.sqrt(a))+1
	for i in range(2,n):
		if a%i==0:
			check=0;
			break
	return check
print 'Done'
