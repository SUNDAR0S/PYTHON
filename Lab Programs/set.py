program 1:

Write a program that generate a set of number that are prime numbers (1-50) and
another set of numbers divisible by 5 (1-50),then apply union, intersection,
difference and symmetric difference on the resultant sets

def generate_prime_numbers(start, end):
    prime_numbers = set()

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.add(num)

    return prime_numbers


def generate_numbers_divisible_by_5(start, end):
    divisible_by_5 = set()

    for num in range(start, end + 1):
        if num % 5 == 0:
            divisible_by_5.add(num)

    return divisible_by_5


# Generate prime numbers in the range 1-50

prime_set = generate_prime_numbers(1, 50)
print("Prime numbers:", prime_set)

# Generate numbers divisible by 5 in the range 1-50

divisible_by_5_set = generate_numbers_divisible_by_5(1, 50)
print("Numbers divisible by 5:", divisible_by_5_set)

# Union of the two sets

union_set = prime_set.union(divisible_by_5_set)
print("Union:", union_set)

# Intersection of the two sets

intersection_set = prime_set.intersection(divisible_by_5_set)
print("Intersection:", intersection_set)

# Difference between the two sets (prime_set - divisible_by_5_set)

difference_set = prime_set.difference(divisible_by_5_set)
print("Difference:", difference_set)

# Symmetric difference of the two sets

symmetric_difference_set = prime_set.symmetric_difference(divisible_by_5_set)
print("Symmetric Difference:", symmetric_difference_set)



o/p:
Prime numbers: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
Numbers divisible by 5: {35, 5, 10, 40, 45, 15, 25, 20, 30}
Union: {2, 3, 5, 7, 10, 11, 13, 15, 17, 19, 20, 23, 25, 29, 30, 31, 35, 37, 40, 41, 43, 45, 47}
Intersection: {5}
Difference: {2, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
Symmetric Difference: {2, 3, 7, 10, 11, 13, 15, 17, 19, 20, 23, 25, 29, 30, 31, 35, 37, 40, 41, 43, 45, 47}




program 2:

Write a program that generates a set of squares of numbers in the range(1-30) and
another list generates numbers that are divisible by 3 in the range(1-30). Generate a
newset from a square set, which should not contain the numbers that are divisible
by 3


def generate_squares(start, end):
    squares_set = set()

    for num in range(start, end + 1):
        squares_set.add(num ** 2)

    return squares_set


def generate_numbers_divisible_by_3(start, end):
    divisible_by_3_list = []

    for num in range(start, end + 1):
        if num % 3 == 0:
            divisible_by_3_list.append(num)

    return divisible_by_3_list


# Generate squares of numbers in the range 1-30
squares_set = generate_squares(1, 30)
print("Squares set:", squares_set)

# Generate numbers divisible by 3 in the range 1-30
divisible_by_3_list = generate_numbers_divisible_by_3(1, 30)
print("Numbers divisible by 3:", divisible_by_3_list)

# Create a new set from the squares set excluding numbers divisible by 3
new_set = squares_set - set(divisible_by_3_list)
print("New set:", new_set)


o/p:

Squares set: {256, 4, 1024, 9, 16, 289, 784, 25, 36, 900, 676, 144, 169, 1764, 784, 1936, 1225, 324, 36, 196, 529, 625, 1024, 1444, 400, 49, 441, 900, 1764, 961}
Numbers divisible by 3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
New set: {256, 4, 1024, 16, 289, 784, 25, 144, 169, 784, 1936, 1225, 324, 36, 196, 529, 625, 1024, 1444, 400, 49, 441, 961}



program 3

Write a Python Program to Count the Number of Vowels in a Given String Using Sets.
Don’t use any built in string functions.
Hint: Create a set that contains VOWELS

def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for char in string:
        if char.lower() in vowels:
            count += 1

    return count

input_string = input("Enter a string: ")
num_vowels = count_vowels(input_string)
print("Number of vowels:", num_vowels)



o/p:

Enter a string: Hello World
Number of vowels: 3




program 4

Consider the given list and find the common elements of the three given lists USING
SET.
List1 = [10, 45, 34, 20, 11]
List2 = [11, 25, 45, 20]
List3 = [20, 25, 11, 14, 45, 65]

def find_common_elements(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    common_elements = set1.intersection(set2, set3)
    return common_elements


# Example usage
list1 = [10, 45, 34, 20, 11]
list2 = [11, 25, 45, 20]
list3 = [20, 25, 11, 14, 45, 65]

common_elements = find_common_elements(list1, list2, list3)
print("Common elements:", common_elements)


o/p:
Common elements: {11, 20, 45}























