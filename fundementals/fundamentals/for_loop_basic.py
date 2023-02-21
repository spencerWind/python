# 1

for index in range(151):
    print(index)

#2

for index in range(0,1001, 5):
    print(index)

#3

for index in range(101):
    if(index%10 == 0):
        print('coding dojo')
    elif(index%5 == 0):
        print('coding')
    else:
        print(index)

#4

def odd_sum():
    num_sum = 0
    for index in range(5001):
        if(index%2 == 1):
            num_sum += index
    print(num_sum)

odd_sum()

#5

for index in range(2018, 0, -4):
    print(index)

#6

def flexible_counter(lowNum, highNum, mult):
    for index in range(lowNum,highNum):
        if(index%mult == 0):
            print(index)

flexible_counter(7,100,3)
