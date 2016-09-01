import sys
print('The command line argument are: ')
for i in sys.argv:
	print i
	print '\t'
print '\n\nThe PYTHONPATH is', sys.path, '\t'
print 'Done'
