x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15

print(x)

students[0]['last_name'] = 'Bryant'

print(students)

sports_directory['soccer'][0] = 'Andres'

print(sports_directory)

z[0]['y'] = 30

print(z)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for index in range(len(some_list)):
        for each_key in some_list[index]:
            dicVal = f'{each_key}- {some_list[index][each_key]}'
            print(dicVal)



def iterateDictionary2(key_name, some_list):
    for index in range(len(some_list)):
        print(some_list[index][key_name])

iterateDictionary2('last_name', students)

iterateDictionary(students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for each_key in some_dict:
        print('-------')
        print(len(some_dict[each_key]), each_key)
        for index in range(len(some_dict[each_key])):
            print(some_dict[each_key][index])
        

printInfo(dojo)
