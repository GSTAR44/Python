Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Set1={2,3,5,7}
>>> Set1ª
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Set1ª
NameError: name 'Set1a' is not defined
>>> Set1[2]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Set1[2]
TypeError: 'set' object is not subscriptable
>>> alphabet=["a","b","c","d"]
>>> alphabet_set=set(alphabet)
>>> print(alphabet_set)
{'d', 'a', 'c', 'b'}
>>> alphabet[2]
'c'
>>> type(alphabet)
<class 'list'>
>>> type(alphabet_set)
<class 'set'>
>>> 