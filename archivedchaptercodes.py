for i in range(10):
    print(i)

for i in range(11):
    print(i)

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

for i in range(1, a//b):
    print(i)

print("""False:{0}{1}{2}{3}""".format(False,bool(None),bool(0),bool((()))))


for i in range(1,20):
    print(" i is now {}".format(i))

number = "9,223,372,036,854,775,807"

for i in range(0,len(number)):
    print(number[i])

number = "9,223,372,036,854,775,807"

for i in range(0,len(number)):
    if (number[i] in '0123456789'):
        print(number[i], end='')

number = "9,223,372,036,854,775,807"
cleanedNumber = ''
for i in range(0,len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber +number[i]
newNumber = int(cleanedNumber) # this throws error if cleaned number is an empty string ''

print("The number is {} ".format(newNumber))


even = [2,4,6,8]
odd = [1,3,5,7]

numbers = odd + even
print(numbers)

print(numbers.sort()) # this will print nothing as this is implemented by guido van rossum to sort on original object alone.
numbers.sort()
print(numbers)
