import math

def Golomb_Encoding_Text(text, M):

    # Initialize variables
    i = 0
    RLE = []
    encoded_text = ''
    
    # Run Length Encoding
    while i < len(text):
        count = 1
        while (i + 1 < len(text) and text[i] == text[i + 1]):
            i += 1
            count += 1
        RLE.append(count)
        i += 1

    # Golomb Encoding for Run Length Codes
    for N in RLE:
        quotient = N // M
        remainder = N % M

        # Quotient with unary code by adding the number of ones followed by zero
        q_code = '1'*quotient + '0'

        floor = math.floor(math.log2(M)) 
        ceil = math.ceil(math.log2(M))
        X = 2**ceil - M      # Calculate the number of values


        if X == 0 :     # if M = 2² (2 of any power) , the number of values (X) will equal zero
            r_code = bin(remainder)[2:]    # add values from index 2 because at index 0,1 the values "0b" is present
            l = len(r_code)       # represent r by log2(M) bits

            if l < math.log2(M):    # if the length of r_code less than math.log2(M) , add the rest of values as 'zeros' on the left
                r_code = '0'*(int(math.log2(M)-l)) + r_code


        elif remainder < X :      # if M not equal 2² (2 of any power) and r less than the number of values (X)
            r_code = bin(remainder)[2:]       # represent r by (Floor log2(M)) bits 
            l = len(r_code)

            if l < floor:      # if the length of r_code less than Floor , add the rest of values as 'zeros' on the left
                r_code = '0'*(floor-l) + r_code
            

        else:             # if M not equal 2² (2 of any power) and r greater than the number of values (X)
            r_code = bin(remainder + X)[2:]      # represent ( r + X ) by Ceil log2(M) bits
            l = len(r_code)

            if l < ceil:     # if the length of r_code less than Ceil , add the rest of values as 'zeros' on the left
                r_code = '0'*(ceil-l) + r_code

        encoded_text += q_code + r_code

    return encoded_text, RLE



def calculate_metrics(text_input,encoded_text, RLE, M):
    bits_before = len(text_input) * 8
    bits_after = len(encoded_text) + len(RLE) * (1 + M.bit_length())
    compression_ratio = bits_before / bits_after

    # Calculate average length
    total_bits = len(encoded_text)
    total_symbols = sum(RLE)
    average_length = total_bits / total_symbols

    # Calculate probabilities of symbols in the source text
    symbol_counts = {}
    for symbol in text_input:
        symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
    symbol_probabilities = [count / len(text_input) for count in symbol_counts.values()]

    # Calculate entropy
    entropy = -sum(p * math.log2(p) for p in symbol_probabilities if p != 0)

    # Calculate efficiency
    efficiency = entropy / average_length

    return bits_before, bits_after, compression_ratio, average_length, entropy, efficiency


# Example usage
# text_input = '''
# aaaabbbbccccddd
# vasfvdgeawfssdf
# dsafadsfasdcsdc '''
# M = 100
# encoded_text, RLE = Golomb_Encoding_Text(text_input, M)
# calculated = calculate_metrics(text_input,encoded_text, RLE, M)
# print("RLE: ",RLE)
# print("Original text:", text_input)
# print("Golomb encoded text:", encoded_text)
# print("Bits before compression:", calculated[0])
# print("Bits after compression:", calculated[1])
# print("Compression ratio:", calculated[2])
# print("Average length:", calculated[3])
# print("Entropy:", calculated[4])
# print("Efficiency:", calculated[5])