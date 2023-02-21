print( 'hello world')

# variables
name = 'spencer wind' # string
age = 19 # number (interger)
likes_chocolate = False # boolean

name = name.title()

print(name + ' is ' + str(age) + ' years old')

# IF statements

    # == is for compatison, = is to set values

if 1 == 1:
    print ('true')

if likes_chocolate:
    print (name,'likes chocolate')
else:
    print(name,'doesnt like chocolate')

count = 0 # 0 resolves to false in Python

if count:
    print('number is greater than 0')
else:
    print('number is less than 0')


#ternary operator (inline if statement)

print('like' if likes_chocolate else 'does not like')

if age <= 12:
    print(name, 'is a child')
elif age <=19:
    print(name,'is a teenager')
else:
    print(name, 'is an adult')