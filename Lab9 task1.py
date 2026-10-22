value=[]
spisok=[1, 2, 3]
x=10
v=2.5
d="елемент"
value.extend([x, v, d])
value.append(spisok)
T=tuple(value)
for i in T:
    print(i, ":", type(i).__name__)
print(T)