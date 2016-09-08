#1. Introduce
##1.1 Features of Python
**Simple**

**Easy to learn**

**Free and Open source**

Python is an example of a FLOSS (Free/Libré and Open Source Software).

**High-level language**

**Portable**

All your Python programs can work on any of these platforms without requiring any changes at all if you are careful enough to avoid any system-dependent features.

You can use Python on GNU/Linux, Windows, FreeBSD, Macintosh, Solaris, OS/2, Amiga, AROS, AS/400, BeOS, OS/390, z/OS, Palm OS, QNX, VMS, Psion, Acorn RISC OS, VxWorks, PlayStation, Sharp Zaurus, Windows CE and PocketPC

**Interpreted**

#4. First

##4.1 Using The Interpreter Prompt
> How to Quit the Interpreter Prompt?

```
If you are using a GNU/Linux or OS X shell, you can exit the interpreter prompt by pressing:
 ctrl+d or entering exit()
 (note: remember to include the parentheses, ()) followed by the enter key.
If you are using the Windows command prompt, press
 ctrl+z followed by the enter key.
```
##4.2. Choosing An Editor
The author would recommend using ```[PyCharm Educational Edition1](https://www.jetbrains.com/pycharm-educational/)``` software which is available on Windows, Mac OS X and GNU/Linux.

These are two of the most powerful editors and you will benefit from using them to write your Python programs: [Vim](http://www.vim.org) or [Emacs](http://www.gnu.org/software/emacs/)

##4.3 vim
Install [jedi-vim](https://github.com/davidhalter/jedi-vim) plugin for autocompletion.

```
apt-get install vim-python-jedi
```

##4.4 Getting help

`help('len')` - this displays the help for the len function which is used to count number of items.

Press `q` to exit the help.

#5. Basic
##5.1 Comment
Use as many useful comments as you can in your program to:
* explain assumptions
* explain important decisions
* explain important details
* explain problems you’re trying to solve
* explain problems you’re trying to overcome in your program, etc.
##5.2 Strings
Strings in double quotes work exactly the same way as strings in single quotes.

**Triple Quotes**

You can specify multi-line strings using triple quotes - ( """ or ''' ). You can use single quotes and double quotes freely within the triple quotes. An example is:
```
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He sasaid "Bond, James Bond."
'''
```
##5.3 Strings Are Immutable

This means that once you have created a string, you cannot change it.

Notice that we could have achieved the same using string concatenation:
> name + ' is ' + str(age) + ' years old'

##5.4 Data type
Create our own types using `classes`

##5.5 Object
Instead of saying "**the something**", we say "**the object**".

##6. Operator
> + (plus)
```
3 + 5 gives 8.
'a' + 'b' gives 'ab'
```
> - (minus)

> * (multiply)

```
2 * 3 gives 6 . 'la' * 3 gives 'lalala' .
```
> ** (power)

```
Returns x to the power of y
3 ** 4 gives 81 (i.e. 3 * 3 * 3 * 3 )
```
> / (divide)

> % (modulo)

> << (left shift)

```
2 << 2 gives 8 . 2 is represented by 10 in bits.
```
>> (right shift)

```
Shifts the bits of the number to the right by the number of bits specified.
11 >> 1 gives 5 .
```
> & (bit-wise AND)

```
Bit-wise AND of the numbers
5 & 3 gives 1 .
```
> | (bit-wise OR)

```
Bitwise OR of the numbers
5 | 3 gives 7
```
> ^ (bit-wise XOR)

```
Bitwise XOR of the numbers
5 ^ 3 gives 6
```
> ~ (bit-wise invert)

```
The bit-wise inversion of x is -(x+1)
~5 gives -6 . More details at http://stackoverflow.com/a/11810203
```

> < (less than)

> > (greater than)

> # (less than or equal to)

> >= (greater than or equal to)


> == (equal to)

> != (not equal to)

> not (boolean NOT)

> and (boolean AND)

> or (boolean OR)

##6.1 Shortcut for math operation and assignment
```
a = 2
a = a * 3
can be written as:
a = 2
a *= 3
```
#7. Control Flow
The length of the input string can be found out using the built-in `len` function

Remember that the `break` statement can be used with the for `loop` as well.

#8. Function
Functions are defined using the `def` keyword


 `def func(a, b=5)` is valid, but `def func(a=5, b)` is not valid.

`a tuple`

`a dictionary`

The `pass` statement is used in Python to indicate an empty block of statements.

There is a built-in function called `max` that already implements the 'find maximum' functionality, so use this built-in function whenever possible.
##8.1 Docstrings
```
def print_max(x,y):
        '''Prints the maximum of two numbers.
The two values must be integers.'''
        #convert to integers, if possible
        x=int(x)
        y=int(y)
        if x>y:
                print x, 'is maximum'
        else:
                print y,'is maximum'
print (3,5)
print_max(3,5)
print print_max.__doc__
```

`print print_max.__doc__` DocStrings are an important tool that you should make use of since it helps to document the program better and makes it easier to understand

#9. Module
##9.1 A module's `name`
##9.2 The `dir` function
You can use the built-in `dir` function to list the identifiers that an object defines.

#10
##10.1 Dictionary(Từ điển)
giống với list nhưng khác ở chỗ:

chỉ mục của list là số còn của từ điển là chuỗi (string).

Tạo từ điển:
```
a= [khoa1:giaitri,khoa2:giaitri2]
```
Ví dụ:
```
>>> a= {'cho':'meo','ga':'vit'}
>>>a
['cho':'meo','ga':'vit']
>>>a['ga'] # cách thao tác với 1 phần tử của từ điển
'vit'
```

Từ điển có 3 phương thức là:

  `key()`: trả về một ds các khóa được dùng trong từ điển, theo một thứ tự bất kỳ

  `sort()`: phương thức sắp xếp của từ điển

  `has_key()`:kiểm tra xem từ khóa có trong từ điển hay không.

  để xóa một cặp giá trị: `del()`

*việc thực thi* một hàm tạo ra một bảng ký hiệu mới dùng cho các biến cục bộ của hàm. Chính xác hơn, mọi phép gán biến trong một hàm chứa giá trị vào bảng ký hiệu cục bộ, các tham chiếu biến sẽ trước hết tìm trong bảng ký hiệu cục bộ rồi trong bảng ký hiệu toàn cục, và trong bảng tên có sẵn. => biến toàn cục k được gán giá trị
##10.2 Set
Một nhóm các phần tử không trùng lặp.

Thường được dùng để loại bỏ các phần tử trùng lặp trong ds, hay dùng để ktra nhân viên, hội viên
```
>>>a = ['a','b','a','d','c','d']
>>>taphop = set(a)
set(['a', 'c', 'b', 'd']) #nó đã bỏ đi các phần tử giống nhau
>>>'a' in taphop #kiểm tra xem a có phải phần tử của tập hợp không
True
```
Với kiểu dữ liệu tập hợp, chúng ta cũng có 4 toán tử tác động tới tập hợp: hợp, giao, hiệu, và hiệu đối xứng.

```
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # những kí tự có trong a
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                              # kí tự có trong a nhưng không có trong b
set(['r', 'd', 'b'])
>>> a | b                              # kí tự có ở a hoặc b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                              # kí tự có cả ở a và b
set(['a', 'c'])
>>> a ^ b                              # kí tự có ở a hoặc b nhưng không có ở cả hai
set(['r', 'd', 'b', 'm', 'z', 'l'])
```


##10.3 References

#11. Tuple

1.Hàm `cmp(tuple1, tuple2)`

So sánh hai tuple với nhau

2	Hàm `len(tuple)`

Trả về độ dài của tuple

3	Hàm `max(tuple)`

Trả về item có giá trị lớn nhất từ một tuple đã cho

4	Hàm `min(tuple)`

Trả về item có giá trị nhỏ nhất từ một tuple đã cho

5	Hàm `tuple(seq)`

chyển một dãy thành một tuple

**tại sao sử dụng Tuple?**

* trình xử lý tuple nhanh hơn list
* dl an toàn hơn vì tuple không thay đổi (immutable)
* dùng để định dạng string

#12. Files
Note that we use `sys.stdout.flush()` after `print` so that it prints to the screen
immediately.

#17. WHAT NEXT
#17.1 Next project
[intermediate Python Projects](https://openhatch.org/wiki/Intermediate_Python_Workshop/Projects)

[make a website with django](http://wiki.openhatch.org/Make_a_website_with_Django)


#17.2 Create a website
* [Flask Official Quickstart](http://flask.pocoo.org/docs/quickstart/)
* [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Example Flask Projects](https://github.com/mitsuhiko/flask/tree/master/examples)

#17.3
[Python Interview Q&A](http://dev.fyicenter.com/Interview-Questions/Python/index.html)
