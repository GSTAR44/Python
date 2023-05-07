Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> List=["python",12,"matlab",45]
>>> List1=["Day","12",23,"#","de45","rt%","56!"]
>>> print(List1)
['Day', '12', 23, '#', 'de45', 'rt%', '56!']
>>> List1[:]
['Day', '12', 23, '#', 'de45', 'rt%', '56!']
>>> List1[1]
'12'
>>> List[2]
'matlab'
>>> List1[2]
23
>>> List[1:3]
[12, 'matlab']
>>> List1[1:3]
['12', 23]
>>> List[2:]
['matlab', 45]
>>> List1[2:]
[23, '#', 'de45', 'rt%', '56!']
>>> List1[1]
'12'
>>> List1[2]
23
>>> List1[1:3]
['12', 23]
>>> List1[2:]
[23, '#', 'de45', 'rt%', '56!']
>>> List[2:2]
[]
>>> List1[2:11]
[23, '#', 'de45', 'rt%', '56!']
>>> List1[11]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    List1[11]
IndexError: list index out of range
>>> List1[7]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    List1[7]
IndexError: list index out of range
>>> List1[6]
'56!'
>>> Length=len(List)
>>> print(Length)
4
>>> print(List1[Length-1])
#
>>> Length=len(List1)
>>> print(Length)
7
