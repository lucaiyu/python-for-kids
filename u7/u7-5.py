#!/usr/bin/env python3
import sys
def silly_age_joke(age):
    print('how old are you?')
    age=int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('What is 13+49+84+155+97? A headache!')

    else:
        print('Huh')

silly_age_joke(1)
