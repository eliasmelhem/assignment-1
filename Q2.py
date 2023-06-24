binary = input("Enter a binary number: ")

# Check if the input is a valid binary number
if not all(char in '01' for char in binary):
    print("Invalid input. Please enter a binary number (0s and 1s) only.")
else:
    decimal = 0
    power = len(binary) - 1

    # Calculate the decimal equivalent
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1

    print("The decimal equivalent of", binary, "is:", decimal)
