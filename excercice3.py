Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Listx=["math","physics","arabic"]
>>> Listx.append("Algebra")
>>> print(Listx)
['math', 'physics', 'arabic', 'Algebra']
>>> Listx.append(45)
>>> print(Listx)
['math', 'physics', 'arabic', 'Algebra', 45]
>>> Listx.remove(45)
>>> Listx
['math', 'physics', 'arabic', 'Algebra']
>>> Listx.remove("arabic")
>>> Listx
['math', 'physics', 'Algebra']
>>> List.index("math")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    List.index("math")
NameError: name 'List' is not defined
>>> Listx.index("math")
0
>>> Listx.append("Math")
>>> Listx
['math', 'physics', 'Algebra', 'Math']
>>> Listx.count("math")
1
>>> Listx.count("algebra")
0
>>> List.extend(Listx)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    List.extend(Listx)
NameError: name 'List' is not defined
>>> Listx.extend(Listx)
>>> Listx
['math', 'physics', 'Algebra', 'Math', 'math', 'physics', 'Algebra', 'Math']
>>> print(Listx)
['math', 'physics', 'Algebra', 'Math', 'math', 'physics', 'Algebra', 'Math']
>>> Listx.extent(["English","chemistry"])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Listx.extent(["English","chemistry"])
AttributeError: 'list' object has no attribute 'extent'
>>> Listx.extend(["English","chemistry"])
>>> Listx
['math', 'physics', 'Algebra', 'Math', 'math', 'physics', 'Algebra', 'Math', 'English', 'chemistry']
>>> Listx.insert(4,"farsi")
>>> Listx
['math', 'physics', 'Algebra', 'Math', 'farsi', 'math', 'physics', 'Algebra', 'Math', 'English', 'chemistry']
>>> len(Listx)
11
>>> Listy=[1,4,9,2,3,7]
>>> Listy.sort()
>>> Listy
[1, 2, 3, 4, 7, 9]
>>> Listz=["d","a","z","s"]
>>> Listz.sort()
>>> Listz
['a', 'd', 's', 'z']
>>> Listx=["math","physics","Algebra","English","chemistry"]
>>> Listx
['math', 'physics', 'Algebra', 'English', 'chemistry']
>>> Listx.insert(4,"farsi")
>>> Listx
['math', 'physics', 'Algebra', 'English', 'farsi', 'chemistry']
>>> matrix=[[1,2,4,5],[2,0,4,5],[3,4,1,0]]
>>> matrix
[[1, 2, 4, 5], [2, 0, 4, 5], [3, 4, 1, 0]]
>>> matrix1=[[1,2,4,5],
	 [2,0,4,5],
	 [3,4,1,0]]
>>> matrix1
[[1, 2, 4, 5], [2, 0, 4, 5], [3, 4, 1, 0]]
>>> 
>>> matrix[0][0]
1
>>> matrix[1][1]
0
>>> m1=[[1,2]]
>>> m1[0][0]
1
>>> m1[0][1]
2
>>> m2=[[1,2],[4,5]]
>>> m2[1][2]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    m2[1][2]
IndexError: list index out of range
>>> m2[1][1]
5
>>> m3=[[[],[]]]
>>> m3
[[[], []]]
>>> m3[0][0]
[]
>>> m3[0][1]
[]
1
>>> m3[0][0]=m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0]
>>> m3
[[9, []]]
>>> m3[0][1]=m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1]
>>> print(m3)
[[9, 12]]
>>> 