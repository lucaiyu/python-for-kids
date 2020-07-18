a=[]
def prime(num):
    for i in range(2,num):
        if num%i==0:
            a.append('Yes')
        else:
            a.append('No')

import sys
print('Please enter the number\n')
num=sys.stdin.readline()
prime(int(num))
if 'Yes' in a:
    print('No')
else:
    print('Yes')
