#coding=utf-8
def fib(b):
    '''In một dãy số fobinao cho đến n: '''
    a,b=0,1
    while b<n:
        print b,
        a,b=b,a+b
#gọi hàm đã được định nghĩa "nhập số: "
n= int(raw_input('nhập số: '))
fib(n)
print 'Done'
