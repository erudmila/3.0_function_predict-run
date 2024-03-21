# Example Code 1

def say_hi():
  print("Why hello there!")

def offer_drink():
  print("Would you care for a spot of tea?")

def offer_food():
  print("Biscuit?")

def say_bye():
  print("Cheerio then.")


offer_drink() #the order is switched from what the written code is and what the statement is
say_hi()    #offer drink will be first, then greting, then offering food. but no goodbye
offer_food()

# Example code 2
def maths1():
  num1 = 50
  num2 = 5
  return num1 + num2  #the total is 55

def maths2():
  num1 = 50
  num2 = 5
  return num1 - num2   #the total is 45

def maths3():
  num1 = 50
  num2 = 5
  return num1 * num2   #the total is 250

outputNum = maths2()   #it will only print the total of maths2 which is 45
print(outputNum)

# Example Code 3
def location(country):
  print("I am from " + country)


location("Brazil")
#it will print "I am from Brazil"
