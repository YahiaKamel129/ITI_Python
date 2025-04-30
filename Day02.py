# Day 2
#exercise 1
'''
arr = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

asc = sorted(arr)
desc = sorted(arr, reverse=True)

print("Original array:", arr)
print("Ascending order:", asc)
print("Descending order:", desc)
'''
#example 2
'''
n = int(input("Enter a number: "))

result = []
for i in range(1, n + 1):
    row = [i * j for j in range(1, n + 1)]
    result.append(row)

print("Multiplication Table (List of Lists):")
print(result)
'''

#example 3
'''
import re

def is_valid_name(name):
    return name.strip() != "" and not name.isdigit()

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

while True:
    name = input("Enter your name: ")
    if is_valid_name(name):
        break
    else:
        print("Invalid name. Please enter a non-empty, non-numeric name.")

email = input("Enter your email: ")

print("\n--- User Data ---")
print(f"Name: {name}")
print(f"Email: {email}")

if is_valid_email(email):
    print("Email is valid ✅")
else:
    print("Email is NOT valid ❌")
'''