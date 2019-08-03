import os
array = list()
num = input()
for i in range(int(num)):
    n =input()
    array.append(str(n))
    sum=os.path.commonprefix(array)
print (sum)
