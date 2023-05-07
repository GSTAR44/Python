Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Dic={1:"one",2:"two",3:"three"}
>>> type(Dic)
<class 'dict'>
>>> print(Dic)
{1: 'one', 2: 'two', 3: 'three'}
>>> T1=(19,20,16,14)
>>> math,physics,arabic,english=T1
>>> Scores={"math":19,"physics":20,"arabic":16}
>>> Scores{"arabic"}
SyntaxError: invalid syntax
>>> Scores["arabic"]
16
>>> Scores[1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Scores[1]
KeyError: 1
>>> Scores[19]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    Scores[19]
KeyError: 19
>>> Scores["math"]
19
>>> Dic2{}
SyntaxError: invalid syntax
>>> Dic2={}
>>> Dic2["first"]="one"
>>> print(Dic2)
{'first': 'one'}
>>> Dic2
{'first': 'one'}
>>> Dic2["second"]="two"
>>> Dic2
{'first': 'one', 'second': 'two'}
>>> print(Dic2)
{'first': 'one', 'second': 'two'}
>>> Dic2["third"]="three"
>>> print(Dic2)
{'first': 'one', 'second': 'two', 'third': 'three'}
>>> 