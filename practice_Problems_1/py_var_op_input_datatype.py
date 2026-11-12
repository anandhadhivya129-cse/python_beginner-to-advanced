#Variables
name="Arun"
age=23
College="JIT"
CGPA=9.34
print(name)
print(age)
print(College)
print(CGPA)

#Input and Output & arithmetic operations
a=int(input("Enter first number: "))
b=int(input("Enter second number:"))
print("Sum:",a+b)
print("Difference:",a-b)
print("Product:",a*b)
print("Quotient:",a/b)
print("Remainder:",a%b)

#Total and average
mat=int(input("Enter marks in maths:"))
phy=int(input("Enter marks in physics:"))
chem=int(input("Enter marks in chemistry:"))
Total_marks=mat+phy+chem
Average_marks=Total_marks/3
print("Total marks:",Total_marks)
print("Average marks:",Average_marks)

#Swapping
a=10
b=20
print("Before swapping:",a,b)
a=b
b=a
print("After swapping:",a,b)

number = 12345
# Extract and print the last digit directly
print(number % 10)

number = 12345
first_number = number // 10
print("First digit:", first_number)
number = 12345
# 2nd digit: 12345 // 1000 = 12 -> 12 % 10 = 2
second_digit = (number // 1000) % 10
# 3rd digit: 12345 // 100 = 123 -> 123 % 10 = 3
third_digit = (number // 100) % 10
print("2nd digit:", second_digit)
print("3rd digit:", third_digit)
#reverse
number = 12345
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = (reversed_num * 10) + digit
    number = number // 10

print("Reversed number:", reversed_num)


