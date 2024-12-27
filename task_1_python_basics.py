# import function to generate random numbers
import random

# random list without any values is created
random_list = []
# we set the number of numbers we need = 100
n = 100
# we use for _ in for generation range of numbers from 1 to 1000
for i in range(n):
   random_list.append(random.randint(1, 1000)) # we use append to add each new value to the list and use random for generation random values
print(random_list) # we print our results in the console

# Sorting
for i in range(len(random_list) -1): #external loop created to run each iteration
    for j in range(len(random_list) -1): # internal loop created to compare pairs of adjacent elements
        if random_list[j] > random_list[j + 1]: # here we're making sure if the previous elements before the next in asc order
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j] # here we exchange values if there are in incorrect order
print(random_list) # we print the results in the console

# average calculation for even and odd numbers
even_numbers = [] # empty list for even numbers created
odd_numbers = [] # empty list for odd numbers created
for i in random_list: # loop for running in random_list
    if i%2 == 0: # to find the even and odd numbers
        even_numbers.append(i) # here we add even numbers to the even_numbers list
    else:
        odd_numbers.append(i) # here we add odd numbers to the odd_numbers list
# print(even_numbers)
# print(odd_numbers)
avg_even_number = sum(even_numbers) / len(even_numbers) # here we're finding the average for even numbers by dividing the sum from the list by the number
avg_odd_number = sum(odd_numbers) / len(odd_numbers) # hee the same
print(avg_even_number) # print average of even numbers in the console
print(avg_odd_number) # print average of odd numbers in the console
