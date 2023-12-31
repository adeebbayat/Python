# Problem 1
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

#1
x[1][0] = 15
print(x)
#2
students[0]["last_name"] = "Bryant"
print(students)
#3
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
#4
z[0]["y"] = 30
print(z)



#Problem 2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(students):
    for n in range(len(students)):
        student = students[n]
        for i in student:
            print(i)
            print(student[i])


iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



#Problem 3

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary2(key_name,some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)


# Problem 4
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



def printInfo(some_dict):
    
    for i in dojo:
        print(len(dojo[f"{i}"]),i.upper())
        for n in range(0,len(dojo[f"{i}"])):
            print(dojo[f"{i}"][n])
        print("")

printInfo(dojo)