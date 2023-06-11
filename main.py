#Function in Python by Priscilla
#6.10.23

# for hi in range(5):
#   print(hi) #0,1,2,3,4
  
# print("-"*10)

# for lo in range(7, -7, -3):
#   print(lo) #7,4,1,-2,-5
  
# print("-"*10)

# phrase = "monty python"
# for letter in phrase:
#   print(letter, end="-") #m-o-n-t-y- -p-y-t-h-o-n-
# print() #no output

# print("end") #

# print("a", "b", "c" +"!") #a b c!

# color = input("what is your fav color? ")
# print("Cool! my fav color is", color + "!")

# q2 = "on a scale of 1 to 10, how much do u like pizza?"
# rating = eval(input(q2))
# print("cool! I like it", rating*1.8, "!")

# #movie_rating.py
# userRating = eval(input("Between 1 and 5 stars, rate your favorite movie:"))
# myMovieRating = 4
# print("our ratings have a difference of", myMovieRating - userRating, "stars b/c i chose 4.")

# #grandiose.py
# adjective = input("enter a synonym for 'faster': ")
# print("my laptop is so much", adjective, "than yours, i'm surprised that your laptop can run this program.")

# #poem.py
# noun = input("give me a plural noun: ")
# adj = input("give me an adjective: ")

# print(noun.title(), "are red. Violets are blue")
# print("Monty Python is", adj.lower(), ", woohoo!")

#madfun.py
import math
num = eval(input("please enter a number: ")) #user inputs a decimal
#print absolute value of the number
print("the absolute value is", abs(num))
#print The number rounded to 0 decimal places
print("the number rounded is", round(num, 0))
#print The square root of the rounded number’s absolute value
print("the square root of the rounded number's absolute value is", math.sqrt(abs(round(num, 0))))
