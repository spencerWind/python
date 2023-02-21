num1 = 42 #variable decleration, number
num2 = 2.3 #variable decleration, number
boolean = True #variable decleration, boolean
string = 'Hello World' #variable decleration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #initialize tuple
print(type(fruit)) #acess value tuple
print(pizza_toppings[1]) #access value list
pizza_toppings.append('Mushrooms') #add value to list
print(person['name']) #access value dictionary
person['name'] = 'George' #change value dictionary
person['eye_color'] = 'blue' #change value dictionary
print(fruit[2]) #access value tuple

if num1 > 45: #if statement
    print("It's greater") #print
else: #else statement
    print("It's lower") #print

if len(string) < 5: #if statement
    print("It's a short word!") #print
elif len(string) > 15: #else if statement
    print("It's a long word!") #print
else: #else statement
    print("Just right!") #print

for x in range(5): #for incriment 0 -> 5
    print(x) #print
for x in range(2,5): #for incriment 2 -> 5
    print(x) #print
for x in range(2,10,3): #for incriment by 3 from 2 -> 10
    print(x) #print
x = 0 #variable decleratiom
while(x < 5): #while loop start at 0
    print(x) #print
    x += 1 #incriment x by 1

pizza_toppings.pop() #remove klast item from pizza toppings
pizza_toppings.pop(1) #remove second item in pizza toppings

print(person) #print a dictionary
person.pop('eye_color') #remove eye color from person dictionary
print(person) #print new dictionary

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if
        continue #continue
    print('After 1st if statement') #print
    if topping == 'Olives': #if
        break #break

def print_hello_ten_times(): #function
    for num in range(10): #fror statement runs through 10 times
        print('Hello') #print

print_hello_ten_times() #calls function print_hello_ten_times() and prints hello 10 times

def print_hello_x_times(x): #parameter is x
    for num in range(x): #for, prints hello x number of times
        print('Hello') #print

print_hello_x_times(4) #prints hello 4 times

def print_hello_x_or_ten_times(x = 10): #parameter is x whihc by default is 10
    for num in range(x): #for loop thqt runs x number of times
        print('Hello') #prints hello x times

print_hello_x_or_ten_times() #prints hello 10 times
print_hello_x_or_ten_times(4) #peints hello 4 times


"""
Bonus section
"""

# print(num3) - NameError: name <variable name> is not defined
# num3 = 72  
# fruit[0] = 'cranberry'  - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'