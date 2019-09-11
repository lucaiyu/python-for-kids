import random
import sys
import time
number=random.randint(0,100)
t1=time.time()
while True:
    print('Guess the number beteen 0 and 100')
    guess_number=sys.stdin.readline()
    guess=float(guess_number)
    if guess==number:
        t2=time.time()
        print("You're guessed right")
        time=t2-t1
        string='You took%s seconds'
        print(string % time)
        break

    if guess>number:
        print('Try height')

    if guess<number:
        print('Try lower')
        t3=time.time()
    if t3-t1>300:
        print('Game over')
        break


