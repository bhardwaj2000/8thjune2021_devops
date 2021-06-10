# get value for address of veriable. 

import ctypes
a=5
y=id(a)
print(y)
print(ctypes.cast(id(a), ctypes.py_object).value)
