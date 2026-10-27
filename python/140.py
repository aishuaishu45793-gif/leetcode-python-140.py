try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    unique_numbers = list(dict.fromkeys(numbers))

    print("Original list:", numbers)
    print("List without duplicates:", unique_numbers)

except ValueError:
    print("Invalid input! Please enter integers only.")