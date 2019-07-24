'''
Created on Jul. 23, 2019

@author: Brunilda Sequeira
'''
import datetime
from dateutil.relativedelta import relativedelta

current_year = datetime.datetime.now()

name = input('Enter your name: ')
age = input('Enter your age: ')

print(f'Hi {name} your will turn 100 years in year {current_year + relativedelta(years=int(age))}')