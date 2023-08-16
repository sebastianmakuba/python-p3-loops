#!/usr/bin/env python3

def happy_new_year():
  
#     # count = 10
#     # while count >= 1:
#     #     print(count)
#     #     count -= 1
    for i in range(11):
        print(i)
    print("Happy New Year!")
    pass
happy_new_year()

def square_integers(int_list):
    # code goes here!
   squares = [i**2 for i in int_list]
   return (squares)
   print (squares)
   pass
square_integers([1,2,3,4,5])
    


def fizzbuzz():
    # code goes here!
    for i in range(1, 101) : 
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
      
        else :
            print(i)
    pass
fizzbuzz()
