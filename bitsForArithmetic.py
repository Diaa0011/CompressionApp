def decimal_to_binary(decimal, precision=64):
    # Separate integer and fraction parts
    integer_part = int(decimal)
    fraction_part = decimal - integer_part

    # Convert integer part to binary
    binary_integer = bin(integer_part)[2:]

    # Convert fraction part to binary with specified precision
    binary_fraction = ""
    while fraction_part and precision > 0:
        fraction_part *= 2
        bit = int(fraction_part)
        binary_fraction += str(bit)
        fraction_part -= bit
        precision -= 1

    # Calculate lengths
    integer_length = len(binary_integer)
    fraction_length = len(binary_fraction)

    return binary_integer, binary_fraction, integer_length, fraction_length


# Test the function with 5.375
# decimal_number = 0.00861343002679208
# binary_integer, binary_fraction, integer_length, fraction_length = decimal_to_binary(decimal_number)

# print("Binary Integer Part:", binary_integer)
# print("Binary Fraction Part:", binary_fraction)
# print("Length of Integer Part:", integer_length)
# print("Length of Fraction Part:", fraction_length)
