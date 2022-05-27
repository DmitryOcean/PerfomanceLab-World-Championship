import math
import sys

data =[]

argfile1 = str(sys.argv[1])  # первый аргумент 
argfile2 = str(sys.argv[2])  # второй аргумент 

file1 = open(argfile1)
str1 = file1.readline()
str2 = file1.readline()
a = float(str1.split(' ', 2)[0])
b = float(str1.split(' ', 2)[1])
r = float(str2)

file2 = open(argfile2)

while True:
    str = file2.readline()
    if not str:
        break
    x1 = float(str.split(' ', 2)[0])
    y1 = float(str.split(' ', 2)[1])
    data.append([x1,y1])

file1.close
file2.close

for i1 in range(len(data)):
    x = data[i1][0]
    y = data[i1][1]
    m = (math.sqrt((x-a)**2+(y-b)**2))
    if r == m:
        print('0')
    if m < r:
        print('1')
    if m > r:
        print('2')

