def find_occurrence(numbers, target):
    positive_indices = []
    negative_indices = []
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == target:
            positive_indices.append(i)
            negative_indices.append(-len(numbers) + i)
            count += 1

    return count, positive_indices, negative_indices

numbers = list(map(int, input("Enter the list of numbers :")))
target = int(input("Enter the element to be found: "))
occurrence, positive_indices, negative_indices = find_occurrence(numbers, target)
print("Element", target, "occurs", occurrence, "time(s) in the list.")
print("Positive Index:", ", ".join(map(str, positive_indices)))
print("Negative Index:", ", ".join(map(str, negative_indices)))
