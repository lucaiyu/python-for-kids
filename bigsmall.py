import sys
print('Please enter number1')
number1=sys.stdin.readline()
print('Please enter number2')
number2=sys.stdin.readline()
list1=number1.split('/')
list2=number2.split('/')
list1[1]=list1[1].strip('\n')
list2[1]=list2[1].strip('\n')
Number1_fenzi=list1[0]
Number1_fenmu=list1[1]
Number2_fenzi=list2[0]
Number2_fenmu=list2[1]
number1_fenzi=int(Number1_fenzi)
number2_fenzi=int(Number2_fenzi)
number1_fenmu=int(Number1_fenmu)
number2_fenmu=int(Number2_fenmu)
#print(number1_fenzi)
#print(number2_fenzi)
#print(number1_fenmu)
#print(number2_fenmu)


if number1_fenzi==number2_fenzi and number1_fenmu==number2_fenmu:
    print('number1=number2')

if number1_fenzi==number2_fenzi:
    if number1_fenmu==number2_fenmu:
        print('')

    if number1_fenmu>number2_fenmu:
        print('number1<number2')

    if number1_fenmu<number2_fenmu:
        print('number1>number2')

if number1_fenmu==number2_fenmu:
    if number1_fenzi==number2_fenzi:
        print('')

    if number1_fenzi>number2_fenzi:
        print('number1>number2')

    if number1_fenzi<number2_fenzi:
        print('number1<number2')

if number1_fenzi!=number2_fenzi and number1_fenmu!=number2_fenmu:
    new_fenmu=number1_fenmu*number2_fenmu
    new_fenzi_number1=number1_fenzi*number2_fenmu
    new_fenzi_number2=number2_fenzi*number1_fenmu
    number1_fenmu=new_fenmu
    number2_fenmu=new_fenmu
    number1_fenzi=new_fenzi_number1
    number2_fenzi=new_fenzi_number2
    if number1_fenzi==number2_fenzi:
        print('number1=number2')

    if number1_fenzi>number2_fenzi:
        print('number1<number2')

    if number1_fenzi<number2_fenzi:
        print('number1>number2')