#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

#PREDITION print 5

##2
#def number_of_military_branches():
#    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#PREDICTION throw an error since the first function hasn't been initialized yet

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#PREDICTION prints 5 since the first return exits the loop


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#PREDICTION prints 5 sinw return call ends function

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

#PREDICTION error since number of great lakes doesn't have a defined value

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

#PREDICTION prints the sum of the two function calls which would be 8

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#PREDICTION prints 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#PREDICTION prints 100, then prints 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#PREDICTION prints 7, prints 14, prints 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#PREDICTION prints 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

#PREDICTION prints 500, prints 500, prints 300, prints 300

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#PREDICTION prints 500, prints 500, prints prints 300, prints 300

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#PREDICTION prints 500, prints 500, prints 300 and sets b to 300, prints 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#PREDICTIONS prints 1, prints 3, prints 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

#PREDICTIONS prints 1, prints 3 sets x to 5, prints 5, set y to 10, prints 10