import sys
def moon_weight():
    print('Plsase enter your current Earth weight(kg)')
    Ew=float(sys.stdin.readline())
    print('Please enter the amont your weight might increase each year(kg)')
    wmiey=float(sys.stdin.readline())
    print('Please enter the number of years')
    noy=int(sys.stdin.readline())
    for x in range(1,noy+1):
        print(x,Ew*0.165+wmiey+noy,'kg')

moon_weight()