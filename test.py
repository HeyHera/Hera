from sympy import re


flag = 0
def change():
    global flag
    flag = 1

change()
print(flag)