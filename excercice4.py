Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Tuple=("d",12,"s34","34!")
>>> Tuple1="f","g","d",12
>>> type(Tuple)
<class 'tuple'>
>>> type(Tuple1)
<class 'tuple'>
>>> print(Tuple[2])
s34
>>> print(Tuple[:])
('d', 12, 's34', '34!')
>>> print(Tuple[1:3])
(12, 's34')
>>> print(Tuple[1:6])
(12, 's34', '34!')
>>> print(Tuple[-1])
34!
>>> print(Tuple[-1:-3])
()
>>> T1=(20)
>>> type(T1)
<class 'int'>
>>> T2=30
>>> T3=30,
>>> type(T3)
<class 'tuple'>
>>> T4=30
>>> type(T4)
<class 'int'>
>>> Tuple4=(45,)
>>> type(Tuple4)
<class 'tuple'>
>>> T5="e"
>>> type(T5)
<class 'str'>
>>> T5="e",
>>> type(T5)
<class 'tuple'>
>>> 