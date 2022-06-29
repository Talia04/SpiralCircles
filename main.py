#program that prints spiral circles with user-defined number
import turtle

user_number = int(input("How many circles do you want?:\t"))
r = 10
for i in range(0,user_number):
  turtle.circle(r)
  r += 10 