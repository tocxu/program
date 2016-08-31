number=23
guess=int(raw_input('Enter an integer : '))
if guess==number:
	#new block starts here
	print "Congratulation, you guessed it."
	print '(but you do not win ant prized!)'
	#new block ends here
elif guess<number:
	#another block
	print 'No, it is a little higher than that'
	#you can do whatever you want in a block...
else:
	print 'no, it is a little lower than that'
	#you must have guessed > number to reach here

print 'Done'
#this last statment is always executed, 
#after the if statment is excuted.
