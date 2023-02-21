def countdown(start_val):
    new_list = []
    for index in range(start_val, 0, -1):
        new_list.append(index)
    return new_list
print(countdown(9))

def print_and_return(a,b):
    print(a)
    return(b)
print_and_return(3,6)

def first_plus_length(list=[]):
    return(list[0] + len(list))
print(first_plus_length([7,8,9]))

def values_greater_than_second(list=[]):
    if(len(list)<2):
        return False
    new_list = []
    print(list[1])
    for index in range(len(list)):
        if list[index] > list[1]:
            new_list.append(list[index])
    return new_list
print(values_greater_than_second([13, 8, 6, 4, 23, 19, 27]))

def length_and_value(len, val):
    list = []
    for index in range(len):
        list.append(val)
    return list
print(length_and_value(5,3))
