#1
def countdown(number):
    for i in range(number,-1,-1):
        print(i)
countdown(5)

#2
def print_and_return(number1,number2):
    print(number1)
    return number2
print_and_return(1,8)

#3
def first_plus_length(list1):
    sum1 = 0
    sum1 = sum1 + list1[0]
    sum1 = sum1 + len(list1)
    return sum1
print(first_plus_length([5,4,3,2,1]))

#4
def greater_than_second(list2):
    temp = []
    counter = 0
    for i in range(len(list2)):
        if (list2[i] > list2[1]):
            temp.append(list2[i])
            counter = counter + 1
    print(len(temp))
    return(temp)

print(greater_than_second([1,2,3,4,5]))

# 5
def this_that(len1,val1):
    list1 = []
    for i in range(len1):
        list1.append(val1)
    return list1

print(this_that(14,2))



