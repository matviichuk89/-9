import numpy as np
sites = {"google.com", "youtube.com", "github.com", "wikipedia.org"}
T=tuple(sites)
L=list(sites)
A=np.array(list(sites))
print("Кортеж:", T)
print("Лист:", L)
print("Массив:", A)
print("Множина", sites)
print("Множина у рядок:")
for i in sites:
    print(i, end=" ")
print()
print("Множина у стовпчик:")
for i in sites:
    print(i)