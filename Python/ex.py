# import math
# value = math.pi
# square = math.sqrt(16)
# print(f'The value of pi is:{value}')
# print(f'The square root of 16 is: {square}')

# # import pygal
# # pie = pygal.Pie()
# # pie.title = 'Time spent on social networks'
# # pie.add('Twitter', 47)
# # pie.add('Facebook', 23)
# # pie.add('Instagram', 30)

# # pie.render_in_browser()

# '''
# help(math) #used to find the functionality of a module 
# '''

# import math
# print('Rounded up to the nearest number')
# rounded = math.ceil(22.7324)
# print(rounded)


# import statistics
# scores = [90, 45, 88, 67, 88]
# mean =statistics.mean(scores)
# print(f'Mean score is {mean}')


# import statistics, math
# diameters = [9, 7, 8, 4]
# result = statistics.mean(diameters)
# print(f'Mean diameter is {result}')
# print('value of pi is:')
# print(math.pi)


# from math import pi
# print('value of pi is:')
# print(pi)


# from statistics import mean
# test_scores = [33, 7, 4, 6]
# result = mean(test_scores)
# print(f'Mean result is {result}')


# from statistics import mean
# ages = [22, 26, 18, 35]
# result = mean(ages)
# print(f'Mean age is {result}')


# import statistics as stats
# sales = [23, 34, 56, 67, 78, 98, 47, 68]
# median = stats.median(sales)
# print(median)

# import math as math_constants

# math = 'Grade 12 constants'
# print(math)
# print('pi:')
# print(math_constants.pi)
# print("Euler's constants:")
# print(math_constants.e)

import math as m
print(m.floor(44.32))

# ---------------------------detecting errors---------------------------------------

# details = {'name': "Paul", 'score':55}
# try:
#     details['email']
# except:
#     raise KeyError('email not found in the dictionary')


access = ['John', 'Aziz', 'Cecil', 'Fred']
member = 'Jennifer'
if member not in access:
    raise LookupError('member not recognised')


details = {
    'name': 'Nana Yaa',
    'occupation': 'Engineer',
    'age': 23
}
try:
    age = details['age']
except:
    raise NameError('No age value in record')

else:
    print(f'Maximum heart rate is{220 - age}')



