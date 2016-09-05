#coding=utf-8
tel={'jack':4098,'sape':4139}
print "\nfirst",tel
tel['guid']=4127
print "\nafter: ",tel

print "\njack",tel['jack']
 
del tel['sape']
print "\ntel: ",tel

tel ['irv']=4127

print "irv: ",tel

print "keys: ",tel.keys()

print "has_key: ",tel.has_key('guid')

print 'guid' in tel

print 'Don'
