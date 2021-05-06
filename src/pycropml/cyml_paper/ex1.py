import pycropml
def sum_(x):
    y = 0
    for i in x:
        y = y + i
    return y
from datetime import datetime
toto=datetime(2000, 10, 12)
print(toto.year)
print(sum_([15,20]))