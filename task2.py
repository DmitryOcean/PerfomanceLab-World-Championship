import math
import sys

x = float(sys.argv[1])  # первый аргумент 
y = float(sys.argv[2]) # второй аргумент
a = float(sys.argv[3])  # третий аргумент
b = float(sys.argv[4]) # четвёртый аргумент
r = float(sys.argv[5])  # пятый аргумент
(m) = (math.sqrt((x-a)**2+(y-b)**2)) 
if r == m:
    print('0')
if m < r:
    print('1')
if m > r:
    print('2')
