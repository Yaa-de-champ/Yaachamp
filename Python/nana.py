scores = [12, 47, 30, 29, 19, 35]
high_scores= [score for score in scores if score > 20]
print(high_scores)
"""
To copy each score element in the new list, we write score as our expression, without applying any operation
"""

item_prices = [120, 25, 40]
under_50 = [price for price in item_prices if price < 50]
print(under_50)


websites = ["nytimes.com", "lemonde.fr", "economist.com"]
french = [website for website in websites if website.count(".fr") > 0]
print(french)


book_codes = ["FH2010", "BV1999", "LB2010"]
books_2010 = [code for code in book_codes if code.count("2010") == 1]
print(books_2010)

# ------------------------------------------------
personal_info = {
    'name':'Nana Yaa Adomaa',
    'ID': 10947512,
    'age': 20,
    'home':'Pantang'
}
personal_info['height'] = 67.45 #to add a new key with a value
print(personal_info)

personal_info = {
    'name':'Nana Yaa Adomaa',
    'ID': 10947512,
    'age': 20,
    'home':'Pantang'
}
del personal_info['age'] #to remove a key valued pair
print(personal_info)

print(len(personal_info))
# -------------------------------------------------------

if 'name' in personal_info:
    print('key "name" is in the dictionary')
else:
    print('oops!')

if 'nage' in personal_info:
    print('key "name" is in the dictionary')
else:
    print('oops!')

if 'email' not in personal_info:
    print('the key "email" is not in the dictionary')

new_string = str(personal_info)
print(new_string)

print(type(personal_info))

sorted_keys = sorted(personal_info)
print(sorted_keys) #sort the keys in the dictionary

items = personal_info.items()
print(items)

that_name = personal_info.get('name')
print(that_name)

ourFavFruits = dict([('Papa', 'Pawpaw'), ('Kwame', 'Orange'), ('Kobby', 'Mango')])
print(ourFavFruits)

# ----------------------------------------------------------------

other_info = {
    'email':'Yaadoku@gmail.com',
    'contact': '0502317445'
}
personal_info.update(other_info)
print(personal_info) #updates the dictionary

# product = {'category': 'book',
#            'price': 4.99,
#            'in_shop': True}

# del product['in_shop']
# print(product)

# ---------------------------------------------------------------------
courses = ["thermodynamics", "anatomy", "linear algebra"]
"""
print(courses[-1])
courses[-3]="african studies" #updating the list
print(courses)
"""

del courses[-2] #remove an element with a specific index
print(courses)

# ----------------------------------------

data = ("Nana Yaa", 19, "9th September 2004")
name = data[0]
age = data[1]
date_of_birth = data[2]

print(f"My name is {name},I am {age} years of age. I was born on {date_of_birth}")

# =------------------------------------------------------------

cake_ingredients = ['eggs', 'flour', 'milk','flavour', 'margarine']
print(cake_ingredients[0:2]) #remember the last index will not be part
print(cake_ingredients[1:])
print(cake_ingredients[3:])
print(cake_ingredients[:2])

# We can also use a format with two colons, [start:stop:step] , where step determines how Python steps between start and end.

print(cake_ingredients[1:4:2])
print(cake_ingredients[::2])

name = "Nana Yaa"
for char in name:
    print(char)


countries = ["France", "Ghana", "Germany", "England"]
for country in countries:
    print(country)
    if country == "Germany":
        break

# ----------------------------------------
names = ["Nana", "Ama", "Kwame"]
scores = [95,  75, 50]
grades = ["A", "B+", "D"]

for name, score, grade in zip(names, scores, grades):
    print(f'{name} had {score} percent in the Thermodynamics Exams. She will see grade {grade} in her records.')


# -------------------------------------------
# begining with classes

# class names have their first letter capitalized

class Cars:
    color = "Black"
    print(color)
    brand = "Buggati"

class Phones:
    water_resistant = True
    case_colour = "Pink"
tecno = Phones()
print(tecno.case_colour)
print(tecno.water_resistant)
# Phones is the definition of the class, water_resistant is the variable, tecno is an instance of the class Phones, to access a class variable we use the format class.variable


class Champion:
    name = "Nana"
    age = 19

    def introduce(self):
        print("Hi!")
        print("I am " + self.name) 
Nana = Champion()
Nana.introduce()
# print(Nana.age)

class Fav_Pet:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
spooky = Fav_Pet("Brown", 4)
print(spooky.color)
print(spooky.legs) 
'''
# In Python, self is a reference to the instance of a class that is being created. When defining a class, the __init__ method is used to initialize the instance of the class. The self parameter is the first parameter of the __init__ method and is used to refer to the instance being created.
# the keyword self is used to access class variables or methods inside the class definition
'''

class MyFlower:
    def __init__(self, kind, color):
        self.kind = kind
        self.color = color
        
    def display_color(self):
        print(self.color)

flamboyant_flower =MyFlower("Flamboyant", "Orange")
print(flamboyant_flower.kind)
flamboyant_flower.display_color()


class MyCar:
    def __init__(self, looks, brand, color):
        self.looks = looks
        self.brand = brand
        self.color = color
    def CarColor(self):
        print(self.color)

Nanas_Car = MyCar("sleek", "Toyota", "black")
print(Nanas_Car.looks)
print(Nanas_Car.brand)
Nanas_Car.CarColor()


# ============================================SENG207================================================
#  SECTION ONE
# 1. Define a class for Person
# 2. Create a person object from the Person class
# 3. Use the constructor method to define attribute for the Person class
# 4. Write a full_name method that returns the full name of the object

'''
there are two ways in doing this: one will use return function (from instruction above) and one will use print function(my trial)'''
# 1st way
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return  self.first_name + ' ' + self.last_name
        
# creating person object
person = Person("Nana Yaa", "Doku-Amponsah")
# printing the full name
print(person.full_name())
print(person.first_name)
print(person.last_name)

# 2nd way

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        print(self.first_name + ' ' + self.last_name)

# creating person object
person = Person("Nana Yaa", "Doku-Amponsah")
# printing the full name
print(person.first_name)
print(person.last_name)
person.full_name()

# ===========================================================================
        
class Mum_Pastries:
    def __init__(self, shape, pastry):
        self.shape = shape
        self.pastry = pastry

    def somePastries(self):
        for p in self.pastry:
            print(p)

myChoice = Mum_Pastries("round",["apple", "orange", "strawberry", "Pear"])
myChoice.somePastries()

# -------------------------------------------------------------------
        
class Book_Series:
 def __init__(self, name, books):
    self.name = name
    self.books = books
    self.num_books = len(books)

 def print_name(self):
    print(self.name)    
  
 def print_books(self):
    print(self.books)

hg = Book_Series("Hunger Games", ["The Hunger Games", "Catching Fire", "Mockingjay"])

hg.print_books()
print(hg.num_books)

# --------------------------------------------------functions-----------------------------
def greet(name):
    print("Hello, " + name + "!")
greet("Nana Yaa")

def greet(name, greeting):
    print(greeting + " , " + name + "!")
greet("Cecil", "Hiiii")
greet(greeting="Hi",  name="Kwame")


# ---------------------------------------------------------------------
def greet(name="world", greeting="Hello"):
    print(greeting + "," + name + "!")
greet()
greet("Alice")

# -------------------------------------------------------------------------
def add(x, y):
    return x + y
result = add(56, 78)
print(result)

# -----------------------------------------------------------------------

def sum(x, *y):
    total = x
    for value in y:
        total += value
    return total
result = sum(1, 2, 3, 5)
print(result)

# =======================================================================

def outer(x):
    y = 10

    def inner(z):
        return x + y + z

    return inner

result = outer(5)(7)
print(result)

# ==================================================================================

add = lambda x, y: x + y
result = add(5, 9)
print(result)

# ------------------------------------------------------------------------------------

def apply(func, x, y):
    return func(x, y)
def add(x, y):
    return x + y

result = apply(add, 45, 10)
print(result)

# -----------------------------------------------------------------------------------------------
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print("Calling function:", func.__name__)
#         result = func(*args, **kwargs)
#         print("Result:", result)
#         return result
#     return wrapper

# @logger
# def add(x, y):
#     return x + y

print(add(3, 5)) #dont understand this lines of code

# ==========================================================================================================

# def outer(x):
#     y = 10

#     def inner(z):
#         return x + y + z

#     return inner
# add = outer(5)
# result = add(7)

# def outer(x):
#     def inner(y):
#         def innermost(z):
#             return x + y + z
#         return innermost
#     return inner

# add = outer(8)(7)
# result = add(7)


# # -------------------------------------------------------------------------------------------------------------------
def getDistance(mph, h):
    return mph*h
mph = 60
h = 2

distance = getDistance(mph, h)
print(distance)

class Car:
    mileage = 12000

    def drive(self, miles):
        self.mileage += miles

tesla = Car()
tesla.drive(100)
print(tesla.mileage)





# ===========================================================================================
#creating a virtual piggy bank🥰🥰
class Piggy:
    value = 0
    
    def addMoney(self, amount):
        self.value = self.value + amount

myPiggy = Piggy()
myPiggy.addMoney(300)

print(myPiggy.value)

# =------------------------------------------------------------------------------------------------------------------------------
class Fav_Books:
    def __init__(self, types, num_pages, author):
        self.types = types
        self.num_pages = num_pages
        self.shape = "cubic"
        self.author = author
    def num_of_pages(self):
        print(self.num_pages)
# Books = Fav_Books("science fictions", 123)
# Books = Fav_Books("Maths Book", 345)
Books = Fav_Books("literature", 600, "Dr.Kumi Ashong")

# Books.num_of_pages()
print(Books.types)
print(Books.num_pages)
print(Books.shape)
print(Books.author)



class Elevator:
    def __init__(self, starting_floor):
        self.make ="The Elevator company"
        self.floor = starting_floor
# to create the object

elevator = Elevator(1)
print(elevator.make)
print(elevator.floor)



# =============================================================================================

class Dog:
    name = "Scooby"
    hungry = True

    def eat(self): #eat() was used to update the value of hungry
        self.hungry= False

dog = Dog()

dog.eat() 
print(dog.hungry)

# =============================================================================================================
class Rectangle:
    base = 12
    height = 3

    def getArea(self): #getArea here is a method
        return self.base * self.height
rect = Rectangle()
area = rect.getArea()
print(area)


class Person:
    name = "Nana"

    def greet(self): #greet here is a method
        print(f"Hiiii!")

p = Person()
p.greet()


# -------------inheriting a class ----------------------

class Car:
    def start_car(self):
        print("Starting Car")

class Hybrid(Car):
    def charge(self):
        print("Using fuel to charge battery")

prius = Hybrid()
prius.start_car()
prius.charge()

# ------------------------------------------------------------------------------

class Parent:
    def __init__(self):
        self.eyes="green"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.age = 7
child = Child()
print(child.eyes)
print(child.age)

# __init__ : Classes contain a method called a constructor that sets the properties of new objects, known as instances.


# ---------------------------------------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Nana = Person("Nana", 19)
print(f'{Nana.name} is {Nana.age} years old')

# ============================================================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Good Afternoon")

class Doctor(Person):
    def __init__(self, name, age):
        super().__init__("Dr." + name, age)

    def intro(self):
        print(f" I'm {self.name}, I work at Rigde Hospital Accra")

person1 = Doctor("Doku-Amponsah", 23)
person2 = Doctor("Hayibor", 34)

person1.greet()
person1.intro()

person2.greet()
person2.intro()

# =================================================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi!")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

student = Student("Nana Yaa", 19, "Biomedical Engineering")

print(student.major)
student.greet()
print(f'My name is {student.name} and I major in {student.major}')

# ================================================================================================
# __init__ is a class method that sets the properties of instances

class Phone:
    def call(self, contact):
        print("Calling " + contact)

phone = Phone()
phone.call( "Mummy\n")


class Employee:
    def __init__(self, company):
        self.company = company
class Developer(Employee):
    def __init__(self, company, language):
        super().__init__(company)
        self.language = language
dev = Developer("Microsoft", "Python Language")

print(dev.language)
print(f'I will like to work in the {dev.company} company oneday, so I am intensively learning {dev.language}')


# ==========================================================================================
class Person:
    def my_self():
        my_info= {
            
            'Name':'Nana Yaa',
            'Age': 19,
            'Email': 'dokuamponsah123@gmail.com'
        }
        return my_info['Age'], my_info['Email'], my_info['Name']
    pass
    
    
print(Person.my_self())
# ----------------------------------------------------------------------------------------------

class IceCreamMaker:
    def churn(self):
        print('Churning cream')
    def freeze(self):
        print('Freezing cream')

    def makeIceCream(self):
        self.churn()
        self.freeze()
iceCreamMaker = IceCreamMaker()

iceCreamMaker.makeIceCream()



# =======================================================================================================

class Translator:
    def record(self):
        print('Recording audio')
    def transcribeRecording(self):
        print('Converting audio to text')
    def translateText(self):
        print('Translating text')
    def translateLive(self):
        self.record()
        self.transcribeRecording()
        self.translateText()
translator = Translator()
translator.translateLive()

# =============================================================================================

class Slideshow:
    def __init__(self, slides):
        self.slides = slides
        self.current = 1
    def viewNextSlides(self):
        self.current += 1
    def play(self):
        while self.current <= self.slides:
            print('Slide', self.current)
            self.viewNextSlides()
slideshow = Slideshow(5)
slideshow.play()


# *********Polymorphism in classes**********************************************************************************************************************
class Feline:
    def speak(self):
        print('Meow')
class Cat(Feline):
    def lick(self):
        print('licking paw')
cat = Cat()
cat.speak()
# cat.lick()

class Feline:
    def speak(self):
        print('Meow')
class Cat(Feline):
    def lick(self):
        print('licking paw')
class Lion(Feline):
    def prey(self):
        print('pounces on prey')

    def speak(self):
            print('ROARRR!!')
cat = Cat()
cat.speak()
lion = Lion()
lion.speak()

class Car:
    def drive(self):
        print('Vroomm!')
class Electric(Car):
    def drive(self):
        print('Whirrrr!')
tesla = Electric()
tesla.drive()

class Person:
    def greet(self):
        print('hello!')
class Professor(Person):
    def greet(self):
        print('salutations')
professor = Professor()
professor.greet()

class Bird:
    def speak(self):
        print('Chirp')
class Duck(Bird):   
    def speak(self):   #Overrides the method at the subclass level 
        print('Quack')
duck = Duck()
duck.speak()

class Bird:
    def speak(self):
        print("Chirp")

class Duck(Bird):
    def speak(self):
        print("Quack")
duck1 = Duck()
duck2 = Duck()
duck2.speak()
duck1.speak()