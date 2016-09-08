#The current working directory
os.getcwd():

os.chdir('C:\\Windows\\System32')

os.getcwd()

os.makedirs('C:\\delicious\\file') # create new folder

## The  os.path module

contains many helpful functions related to file names and file paths.

os.path.join(): build paths in a way

import os.

os.path.abspath(path): return a string of the absolute path of the argument. the easy way to convert a relative path into an absolute one.

os.path.isabs(path): return True if the argument is an absolute and False if it is a relative path

os.path.relpath(path,start): return string of a relative path from the start path to path, if start is not provided, the current working dirctory is used as the start path.

os.path.relpath('C:\\Windows', 'C:\\')

os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')

'..\\..\\Windows'

os.getcwd() 'C:\\Python34'

path = 'C:\\Windows\\System32\\calc.exe'

os.path.basename(path)

  'calc.exe'

os.path.dirname(path)

  'C:\\Windows\\System32'


## The shelve module

import shelve

shelfile=shelve.open('mydata')

cats=['Zophie','Pooka','Simon']

shelfile['cats']=cats

shelfile.close

## The shutil Module
`shutil` or shell utilities module has functions to let you copy, move, rename, and delete files in your PYthon programs.To use the shulti functions, you will first need to used `import shutil`
###Copying files and folders

calling `shutil.copy`

`shutil.copy()`: copy single file

`shutil.copytree()`: call create a new folder with the same content as the original folder.

### Moving and renaming files and folders
`shutil.move()`: move the file or folder at the path `source` to the path `destinaltion` and will return a string of the absolute path of the new location

## Permanently Deleting Files and Folders
`os.unlink(path)`: xóa file trong `path`

`os.rmdir(path)`: xóa thư mục trong `path`. thư mục này phải rỗng

`shutil.rmtree(path)`: remove thư mục trong `path`, và tất cả files hay folders chứa trong đó cũng bị xóa

## Safe Deletes with the send2trash Module
### send2trash module
tránh trường hợp láu táu xóa nhanh và nhầm, module này giúp thực hiện xóa 2 bước, move tới trash trước khi del vĩnh viễn

### Walking a Directory Tree

`os.walk()`: hàm chứa một chuỗi giá trị đơn: đường dẫn tới thư mục. không giống như range() os.walk() sẽ trả về ba giá trị sau mỗi lần lặp:

1. chuỗi tên của thư mục hiện tại
2. một danh sách của chuỗi các thư mục trong thư mục hiện tại
3. một danh sách các file trong thư mục hiện tại
### Reading ZIP Files

os.chdir(path): chuyển đến thư mục path

`*.namelist()`: hiện tất cả các file trong file zip đã nén


```
>>> import zipfile, os
   >>> os.chdir('C:\\')    # move to the folder with example.zip
   >>> exampleZip = zipfile.ZipFile('example.zip')
   >>> exampleZip.namelist()
   ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
   >>> spamInfo = exampleZip.getinfo('spam.txt') #`variable.getinfo('file.txt')`; lấy thông tin của file.
   >>> spamInfo.file_size #lấy kich thước file.
   13908
   >>> spamInfo.compress_size
   3828
>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
   .compress_size, 2))
   'Compressed file is 3.63x smaller!'
   >>> exampleZip.close()
```
### Extracting from ZIP Files

```
>>> import zipfile, os
   >>> os.chdir('C:\\')    # move to the folder with example.zip
   >>> exampleZip = zipfile.ZipFile('example.zip')
❶ >>> exampleZip.extractall()
   >>> exampleZip.close()
```


## The zipfile module

exampleZip.extractall()

## The webbrowser module

webbrowser.open('http://inventwithpython.com/')
