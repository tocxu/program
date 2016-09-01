#coding:utf-8
import check_prime 
a=int(raw_input("Nhap so bất kỳ: "))
check=check_prime.check_prime(a)
if check ==0:
	print '%d không là số nguyên tố' %a
else:
	print '%d là số nguyên tố' %a
print 'Done'

