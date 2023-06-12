#Function in Python by Priscilla
#6.10.23

for hi in range(5):
  print(hi) #0,1,2,3,4
  
print("-"*10)

for lo in range(7, -7, -3):
  print(lo) #7,4,1,-2,-5
  
print("-"*10)

phrase = "monty python"
for letter in phrase:
  print(letter, end="-") #m-o-n-t-y- -p-y-t-h-o-n-
print() #no output

print("end") #

print("a", "b", "c" +"!") #a b c!

color = input("what is your fav color? ")
print("Cool! my fav color is", color + "!")

q2 = "on a scale of 1 to 10, how much do u like pizza?"
rating = eval(input(q2))
print("cool! I like it", rating*1.8, "!")




