Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> stack = ["sprint"]
>>> stack.append("Summer")
>>> print(stack)
['sprint', 'Summer']
>>> stack.append("Fall")
>>> stack
['sprint', 'Summer', 'Fall']
>>> stack.append("Winter")
>>> stack
['sprint', 'Summer', 'Fall', 'Winter']
>>> sack
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sack
NameError: name 'sack' is not defined
>>> stack.pop()
'Winter'
>>> stack.pop()
'Fall'
>>> class stack1:
	def__init__(self):
		
SyntaxError: invalid syntax
>>> class stack1:
	def __init__(self):
		self.items = []
		