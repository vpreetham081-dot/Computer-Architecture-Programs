def display_binary(n):
    return format(n & 255, '08b')


def left_shift(binary, positions):
    number = int(binary, 2)

    print("\nOriginal Binary:", binary)
    print("Logical Left Shift:")

    for i in range(positions):
        number = (number << 1) & 255
        print("Step", i + 1, ":", display_binary(number))

    print("Final Result:", display_binary(number))


def right_shift(binary, positions):
    number = int(binary, 2)

    print("\nOriginal Binary:", binary)
    print("Logical Right Shift:")

    for i in range(positions):
        number = number >> 1
        print("Step", i + 1, ":", display_binary(number))

    print("Final Result:", display_binary(number))


print("8-bit Logical Shift Operations")

print("\n1. Left Shift of 10110110 by 3 positions")
left_shift("10110110", 3)

print("\n2. Right Shift of 11010100 by 3 positions")
right_shift("11010100", 3)
