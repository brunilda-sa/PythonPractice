'''
Created on Jul. 23, 2019

@author: Brunilda
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = input(f'Enter a number among this list {a}: ')

less_than = [a[i] for i in range(len(a)) if a[i] < int(number)]

print(f'The new list containing numbers less than {number} is {less_than}')