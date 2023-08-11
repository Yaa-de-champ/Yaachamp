print(1>3)
print(5!=6)
weather="3"+"2"
print(weather)
cardiod=4+8
print(cardiod)
print(11>=11)
peace=3>=2
print(peace)
high=23
low=14
result=high>=low
print(result)
print("nana yaa:")
lowest_currency_had=675
print(lowest_currency_had)
papa=134
currency=papa>=200
print("siblings_money:")
print(currency)
solved=35
maximum=347
lost_streak=maximum>=solved
print(lost_streak)
print(high==high)
print(high!=low)
print("reasonable"=="reasonable")
print("reasonable"=="wise")
fruit_1="mango"
fruit_2="pawpaw"
print(fruit_1==fruit_2)
print("before"  +  "life")
print(f"{4} new shoes")
books=12
bags=15
print(f"total price={books-bags}")
print(f"cost increased by {16}%")
if True:
  print("NANA YAA")
if False:
  print("PAPA")
if True:
  print("DADDY")
  print("MUMMY")

Love = False;
if Love :
  print("PEACE")

Holy = True
if Holy:
  print("hi")

fat_oranges = "money" 
print(fat_oranges)

if True:
  print("THANKS FOR YOUR SERVICES")
answer="EIFFEL TOWER"
if answer == "EIFFEL TOWER":
  print(answer  +  " is correct! ")

answer="VENICE"
if answer != "EIFFEL TOWER":
  print(answer + " is wrong! ")

age = 43
if age >= 23:
   print ("Discount applied")

is_thursday = True
if is_thursday == True:
     print ("YAAYYY!")

    
marks=55.67
pass_grade = marks < 70
if pass_grade:
  print(pass_grade)


  game = "TEMPLE RUN"
  no_of_times_played = 456
  if no_of_times_played >= 400:
     print("Your top game played this week: ") 
     print(game) 
    
today = "its my birthday"
if today != "an ordinary day":
     print("happy birthday girlll!")

holy = True
if holy:
    print("VIRGIN")

online = True
if online:
    print("hey there!")

if not online:
     print("oops!")

indoors = False
if indoors:
    print("what happened")
else:
    print("finally home!")


marks = 78
if marks == 65:
  print("cool")
else:
   print("manageable")

points = 5600
points_needed = 8000
if points >= points_needed:
      print("GOOD JOB YOU ARE IN LEVEL 2!")
else:
     left = points_needed - points
     print("points to get to level 2:")
     print(left)

#conditonal statements 
hour=9
if hour < 12:
  print("Good Morning")
else:
  print("Good Night")

#if hour is greater than 12 but less than 17 
hour = 14 
if hour < 12:
   print("Good morning")
elif hour < 17:
   print("Good afternoon ")

  #elif statement runs its code block if the conditions before it were  False and its condition is like hour < 17 is true 
#also we can code an else to run its code block when the if and elif conditions are false.eg.

hour = 18
if hour < 12:
   print("Good morning ")
elif hour < 17:
   print("Good afternoon")
else:
   print("Good night")

  #as long as they go before the else statement we can add as many elif statements as we like
 
hour = 20
if hour < 12:
   print("Good morning ")
elif hour < 17:
   print("Good afternoon")
elif hour < 21:
  print("Good evening")
else:
   print("Good night") 

#there is no maximum number of elif statements we can add to an if statement

breakfast = "corn meal"
if breakfast == "rice pudding":
  print("Request Denied")
elif breakfast == "oat meal":
  print("Request Accepted")
else:
  print("Could not process request")

#we can also use operators like ==, <=, >= when writing our statements (if,elif,else)
age = 17
has_permit = True
if age > 16 and has_permit:
  print("Can Drive")
#we use the and operator to allow us to run code only if both conditions age > 16 and has_permit are True 
#the and operator skips the code block if one or more condtions are False like age > 18

age = 17
has_permit = True
is_insured = True
if age > 16 and has_permit and is_insured: 
  print("Can Drive")

  #we can add as many and that we like, and is used for linking multiple conditions

going_for_lectures = True
is_sunny = True
distance = "5km"
if going_for_lectures and is_sunny and distance > "5km":
  print("Will walk to school")
else:
  print("will board a taxi")

#next operator "or" is used to run a code when either one of the conditions is True 

average_grade = "A"
final_score = 1400
if average_grade == "A" or final_score >= 1300:
  print("certificate achieved")

  #with or a code gets skipped only if all conditions are False we can use as many or that we want

shoe = 5
shoe = shoe + 1
print(shoe)

shoe = 8
shoe = shoe + 5
shoe = shoe - 2
print(shoe)
#these are all known as self-assigning which helps let us track data that changes over time 

name = " account name: "
name = name + " Yaa "
name = name + " Adomaa "
print(name)

name = " Nana Yaa "
name = name + "Amponsah"
print(name)

bags = 5
bags += 1
print(bags)

bags = 8
bags -= 3
print(bags)
#we use the -= or the += operator when we want to add or subtract to a variable 

#PROJECT WORK

ride_type = "Black"
credits = 6

ride_price = 0
final_price = 0
#rideprice and final price will be updated later 
if ride_type == "Lambogini":
  ride_price = 20.45
elif ride_type == "Black":
  ride_price = 37.9
else:
#we dont have to forget the puntuation mark (:) after the conditional statements
  ride_price = 18.7 

print("Ride price:")
print(ride_price)

if credits > 0:
  final_price = ride_price - credits
print("Final price:")
print(final_price)

#I WILL BE A GREAT PROGRAMMER AND AN ENGINEER!

print("again")
print("again")
print("again")
print("again")
print("again")

#while True:
  #print("once shown ")
#to prevent printing the same function over and over again we use the while loop but without a limit the same thing keeps on printing to infinity

keep_moving = True
while keep_moving == True:
  print("had it all")
  keep_moving = False

keep_going = True
while keep_going == True:
  print("and again")
keep_going = False
print("one more time")

keep_going = True
while keep_going == True:
  print("and again")
keep_going = False
print("one more time")





