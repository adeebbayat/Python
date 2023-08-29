# 1)
for i in range(0,151):
    print(i)

# 2)
for i in range(5,1001,5):
    print(i)

# 3)
for i in range(1,101):
    if (i % 10 == 0):
        print("Coding Dojo")
        continue
    elif (i % 5 == 0):
        print("Coding")
        continue
    else:
        print(i)

# 4)
sum = 0
for i in range(0,500001):
    if (i % 2 != 0):
        sum += i
print(sum)

#5)
for i in range(2018,0,-4):
    print(i)

#6)
lowNum = 3
highNum = 20
mult = 4

for i in range(lowNum,highNum+1):
    if (i % mult == 0):
        print(i)

