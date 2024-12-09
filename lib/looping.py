#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0: 
        print(i)
        i -= 1
    else:
        print("Happy New Year!")

def square_integers(int_list):
    int_list = [number * number for number in int_list]
    return int_list

def fizzbuzz():
    for i in range(1, 101):
        fizz = False
        buzz = False
        if i % 3 == 0:
            fizz = True
        if i % 5 == 0:
            buzz = True
        if fizz==True and buzz==True:
            print("FizzBuzz")
        elif fizz==True:
            print("Fizz")
        elif buzz==True:
            print("Buzz")
        else:
            print(i)
        
fizzbuzz()