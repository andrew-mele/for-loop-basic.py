# QUESTION 1
for i in range(0, 151):
    print(i)

# QUESTION 2
for i in range(5, 1005, 5):
    print(i)

# QUESTION 3
for i in range(1, 101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

# QUESTION 4
sum = 0
for i in range(1, 500000, 2):
    sum = sum + i
print(sum)

# QUESTION 5
for i in range(2018, -2, -4):
    print(i)

# QUESTION 6
lowNum = 6
highNum = 18
multi = 3

for i in range(lowNum, highNum + 1, multi):
    print(i)