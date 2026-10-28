
def to_binary(n):
    return format(n & 255, '08b')


def to_signed(n):
    if n >= 128:
        return n - 256
    return n


def add_binary(a, b):
    a_bin = to_binary(a)
    b_bin = to_binary(b)

    a_8 = a & 255
    b_8 = b & 255

    result = (a_8 + b_8) & 255
    result_bin = to_binary(result)
    decimal_result = to_signed(result)

    overflow = (
        ((a_8 ^ b_8) & 128) == 0
        and ((a_8 ^ result) & 128) != 0
    )

    print("\nFirst Number :", a)
    print("Binary       :", a_bin)

    print("Second Number:", b)
    print("Binary       :", b_bin)

    print("Binary Addition:")
    print("  ", a_bin)
    print("+ ", b_bin)
    print("-----------")
    print("  ", result_bin)

    print("Binary Result :", result_bin)
    print("Decimal Result:", decimal_result)

    if overflow:
        print("Arithmetic Overflow: YES")
    else:
        print("Arithmetic Overflow: NO")


print("8-bit 2's Complement Arithmetic")

print("\nExpression 1: 120 + 62")
add_binary(120, 62)

print("\nExpression 2: -120 + (-62)")
add_binary(-120, -62)
