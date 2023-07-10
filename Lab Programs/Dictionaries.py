Program 1:
Write a python program to generate the following dictionary
Num = { 1 : 1, 2 : 8, 3 : 27, 4 : 64, 5 : 125 ….. , 20 : 8000}

num = {}
for i in range(1, 21):
    num[i] = i ** 3

print("Num =", num)

o/p:
Num = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000, 11: 1331, 12: 1728, 13: 2197, 14: 2744, 15: 3375, 16: 4096, 17: 4913, 18: 5832, 19: 6859, 20: 8000}


program 2:

 Write a program that inverts a dictionary. I.e., it makes key of one dictionary value of
another and vice versa
Sample Input:
Dict={‘Reg.No”:123, ‘Name’:’abc’,Course’:’CSE’}
Sample Output:
Inv Dict={123:’Reg.No’, ‘abc’ : ‘Name’, ‘CSE’: ‘Course’}

def invert_dict(dictionary):
    inverted_dict = {}

    for key, value in dictionary.items():
        inverted_dict[value] = key

    return inverted_dict


# Example usage
dict = {'Reg.No': 123, 'Name': 'abc', 'Course': 'CSE'}

inverted_dict = invert_dict(dict)
print("Inverted Dict =", inverted_dict)

o/p:
Inverted Dict = {123: 'Reg.No', 'abc': 'Name', 'CSE': 'Course'}


program 3:

Generate a dictionary where keys are numbers and values consist of a set of its
factors in a specified range.
Factors = {1:{1} , 2:{1,2}, 3: {1,3}, 4:{1,2,4} , 5:{1,5}, 6:{1,2,3,6}, 7:{1,7}, 8:{1,2,4,8},
9:{1,3,9,}}


def generate_factors_dict(start, end):
    factors_dict = {}

    for num in range(start, end + 1):
        factors = set()
        for i in range(1, num + 1):
            if num % i == 0:
                factors.add(i)
        factors_dict[num] = factors

    return factors_dict


start_range = int(input("enter the starting no:")
end_range = int(input("enter the ending no:")

factors = generate_factors_dict(start_range, end_range)
print("Factors =", factors)

o/p:
enter the starting no:1
enter the ending no:9
Factors = {1: {1}, 2: {1, 2}, 3: {1, 3}, 4: {1, 2, 4}, 5: {1, 5}, 6: {1, 2, 3, 6}, 7: {1, 7}, 8: {8, 1, 2, 4}, 9: {1, 3, 9}}



program 4:

Digit_word = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

# Read integer from user
num = input("Enter an integer: ")

# Convert each digit to word and join them
result = " ".join(Digit_word[int(digit)] for digit in num)

# Display the result
print(result)


o/p:
Enter an integer: 324
Three Two Four


program 5:

code:


Cricketer = {
    "VinayKumar": [102, 5],
    "Yuzvendra Chahal": [89, 10],
    "Sandeep Sharma": [95, 8],
    "Umesh Yadav": [85, 6],
    "BhuvaneswarKumar": [106, 10],
    "Basil Thampi": [70, 5]
}

# Calculate Bowling Average and replace the values in the dictionary
for player, stats in Cricketer.items():
    runs_conceded, wickets = stats
    bowling_average = runs_conceded / wickets
    Cricketer[player] = [bowling_average]

# Sort the dictionary based on the Bowling Average
sorted_dict = sorted(Cricketer.items(), key=lambda x: x[1])

# Display the sorted dictionary
for player, average in sorted_dict:
    print(player + ":", average)

o/p:

Yuzvendra Chahal: [8.9]
Basil Thampi: [14.0]
Umesh Yadav: [14.166666666666666]
Sandeep Sharma: [11.875]
BhuvaneswarKumar: [10.6]
VinayKumar: [20.4]




