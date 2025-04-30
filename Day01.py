#exampel1
'''
def count_vowels(user_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for i in user_string:
        if i.lower() in vowels:
            counter += 1
    print("Number of vowels in the string:", counter)


user_string = input("Enter a string: ")
count_vowels(user_string)
'''

#example2
'''
def location(user_string):
    char_i = 'i'
    for i in user_string:
        if i.lower() == char_i:
            print("The character 'i' is present in the index:", user_string.index(i))
            break
    else:
        print("The character 'i' is not present in the string")


user_string = input("Enter a string: ")

location(user_string)
'''

#example3
'''
def generate_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{i}x{j}={i*j}", end=" , ")
    print()

generate_multiplication_table(5)
'''

#example4
'''
def mario_pyramid(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * i
        print(spaces + stars)

mario_pyramid(5)
'''
#End Day01.py