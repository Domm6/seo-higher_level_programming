#!/usr/bin/python3
def max_integer(my_list=[]):
  biggest = my_list[0]
  for num in range(len(my_list)):
    if biggest > my_list[num]:
      biggest = num 
  return biggest
