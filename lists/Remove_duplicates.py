#remove duplicates 
numbers = [1, 2, 3, 2, 4, 5, 1, 3, 6, 5]

new_numbers = []

for number in numbers:
    if number in new_numbers:
        continue

    new_numbers.append(number)
