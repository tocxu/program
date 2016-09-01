def total(initial=5, *numbers, **keywords):
	count = initial
	for number in numbers:
		print 'number is ',number 
		print 'numbers is: ',numbers
		count+=number
		print 'numebr is : ',count
	for key in keywords:
		print 'key is ',key
		print 'keywords is ',keywords
		count+=keywords[key]
		print 'count is ',count
		
	return count
print r'total(10,1,2,3,vegetables=50,fruits=100)'
print total(10,1,2,3,vegetables=50,fruits=100)
print 'Done'
