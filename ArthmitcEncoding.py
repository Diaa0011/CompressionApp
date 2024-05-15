import copy
import struct
import sys
import math
from bitsForArithmetic import decimal_to_binary
def calculate_character_probability(input_string):
    char_count = {}
    total_chars = len(input_string)
    
    # Count occurrences of each character
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Calculate probabilities
    char_probabilities = {}
    for char, count in char_count.items():
        char_probabilities[char] = round(count / total_chars, 4)
    
    return char_probabilities

def arithmetic_coding(text, probability):
    ranges = {}
    cdf = 0
    start = 0
    for i in probability:
        cdf += probability[i]
        ranges[i] = [round(start, 4), round(cdf, 4)]
        start = cdf
    updated_ranges = copy.deepcopy(ranges)
    for i in text[:-1]:
        min_val = updated_ranges[i][0]
        max_val = updated_ranges[i][1]
        start = min_val
        for j in updated_ranges:
            updated_ranges[j][0] = start
            updated_ranges[j][1] = min_val + ((max_val - min_val) * ranges[j][1])
            start = updated_ranges[j][1]
    encoded_value = (updated_ranges[text[-1]][0] + updated_ranges[text[-1]][1]) / 2
    return ranges, updated_ranges[text[-1]], len(text)*8, encoded_value

def calculate_metrics(original_size,compressed_value,probability):

    #Calculate entropy
    entropy = 0
    bits_after_compression = decimal_to_binary(compressed_value)[3]
    for prob in probability.values():
        entropy -= prob * math.log2(prob)
    #Calculation of Compression Ration
    compression_ratio = original_size / bits_after_compression
    #Calculate AverageLength 
    average_length = 0
    for char, prob in probability.items():
        length = len(bin(int(1 / prob))) - 2  # Length of binary representation
        average_length += prob * length
    efficiency = entropy/average_length
    return entropy,average_length,compression_ratio,efficiency
# Example usage:
# original_text = "jhtgfdsghetwaegf"
# probabilities = calculate_character_probability(original_text)

# ranges, encoded_size, original_size, compressed_value = arithmetic_coding(original_text, probabilities)

# calculated_Data = calculate_metrics(original_size,compressed_value,probabilities)
# compressed_size = decimal_to_binary(compressed_value)[3]

# print("Original Size:", original_size)
# print("Compressed Size:", compressed_size)
# print("Compressed Value: ",compressed_value)
# print("probablities: ",probabilities)
# print("entropy: ",calculated_Data[0])
# print("average_length: ",calculated_Data[1])
# print("Compression_Ratio: ",calculated_Data[2])
# print("efficiency: ",calculated_Data[3])

# print("Encoded Size: ",encoded_size)