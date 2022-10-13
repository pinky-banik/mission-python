# single import
import function

sum = function.add(5,10)
print('sum in modules.py',sum)

# single function import
from function import add
res = add(5,10)
print(res)

# all function import
from function import *
res = add(5,10)
print(res)
