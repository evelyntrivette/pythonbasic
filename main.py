# text, variables, and boolean expressions
print("Hello World")
age = 25
print(age)
price = 19.95
first_name = 'Mosh'
print(first_name)
is_online = True

# recveiving input
name = input("What is your name? ")
print("Hello " + name)

#type conversation
birth_year = input("Enter your birthyear: ")
age = 2023 - int(birth_year)
print(age)

#basic calculator
first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))

#strings
course = 'Python Basics'
print(course.find('y'))
print(course.upper())
print(course.replace('y', 'Y'))
print('Python' in course)

#arithmetic operations
    # // int, / decim, % remainder, ** expo, += augmen assign opr
x = 10
x += 3

#operator precedence and comparison and logical operators
x = 10 + 3 * 2
x = 3 > 2
print(x) #true, boolean and != not equal
price = 25
print(price > 10 and price < 21) #false (sheffer stroke)

#if statements
temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It is a cold day")
    print("Wear a sweater")

#while loops
i = 1
while i <= 6:
    print(i * '*')
    i = i + 1

#lists
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"#edit name
print(names[0:3])#will print index between 0 and 2

#list methods
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)
numbers.remove(3)
    #numbers.clear() clears all values
print(1 in numbers) #returns boolean value
print(len(numbers))
print(' break ')

#for loops
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
print(' break ')

#therange()Function
numbers = range(5, 10, 2)#passing two steps
for number in numbers:
    print(number)

#tuples
numbers = (1, 2, 3)


