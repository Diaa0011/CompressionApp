#!/usr/bin/env python
# coding: utf-8

# In[5]:


import collections
import math
def Ord_lzw_compress(input_string):
    # Initialize dictionary with single character ASCII values
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ""
    compressed_data = []

    # Iterate over characters in the input string
    for c in input_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            # Add new string to the dictionary
            compressed_data.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w if not empty
    if w:
        compressed_data.append(dictionary[w])

    return compressed_data

# Function to calculate entropy
def calculate_entropy(char_freq):
    total_chars = sum(char_freq.values())
    entropy = -sum((freq / total_chars) * math.log2(freq / total_chars) for freq in char_freq.values())
    return entropy

# Function to calculate compression ratio and other metrics
def calculate_metrics(input_string, compressed_data):
    # Calculate character frequencies
    char_freq = collections.Counter(input_string)

    # Calculate entropy
    entropy = calculate_entropy(char_freq)

    # Calculate bits before and after encoding
    bits_before_encoding = len(input_string) * 8  # ASCII: 8 bits per character
    bits_after_encoding = sum(math.ceil(math.log2(code + 1)) for code in compressed_data)  # Bits in LZW-compressed data

    # Calculate compression ratio
    compression_ratio = bits_before_encoding/bits_after_encoding

    # Calculate average length
    average_length = bits_after_encoding / len(input_string)

    # Calculate efficiency
    efficiency = entropy / average_length

    return bits_before_encoding, bits_after_encoding, compression_ratio, entropy, average_length, efficiency



# In[11]:


# # Example input string
# input_string = "wabbawabba"

# # Compress using LZW
# compressed_data = lzw_compress(input_string)

# # Calculate metrics
# bits_before_encoding, bits_after_encoding, compression_ratio, entropy, average_length, efficiency = calculate_metrics(
#     input_string, compressed_data
# )

# Output results
# print("Original Input String:", input_string)
# print("Compressed Data:", compressed_data)
# print("Bits Before Encoding:", bits_before_encoding)
# print("Bits After Encoding:", bits_after_encoding)
# print("Compression Ratio:", compression_ratio, "%")
# print("Entropy:", entropy)
# print("Average Length:", average_length)
# print("Efficiency:", efficiency)


# In[15]:


# Doctor ASCII
import collections
import math

def Doctor_lzw_compress(input_string):
    # Initialize dictionary with ASCII characters from 0 to 127
    initial_dict_size = 128
    dictionary = {chr(i): i for i in range(initial_dict_size)}
    compressed_data = []

    # This variable will keep track of where to add new dictionary entries
    new_entry_index = 128
    w = ""

    # Iterate over characters in the input string
    for c in input_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            # Add code for `w` to the compressed data
            compressed_data.append(dictionary[w])
            # Add `wc` to the dictionary starting from 128
            dictionary[wc] = new_entry_index
            new_entry_index += 1
            # Reset `w` to `c`
            w = c

    # If `w` is not empty, add its code to the compressed data
    if w:
        compressed_data.append(dictionary[w])

    return compressed_data


# In[16]:


# # Example input string
# input_string = "wabbawabba"

# # Compress using LZW
# compressed_data = lzw_compress(input_string)
# print("Compressed Data:", compressed_data)


# In[18]:


# Example input string
# input_string = "wabbawabba"

# # Compress using LZW
# compressed_data = lzw_compress(input_string)

# # Calculate metrics
# bits_before_encoding, bits_after_encoding, compression_ratio, entropy, average_length, efficiency = calculate_metrics(
#     input_string, compressed_data
# )

# Output results
# print("Original Input String:", input_string)
# print("Compressed Data:", compressed_data)
# print("Bits Before Encoding:", bits_before_encoding)
# print("Bits After Encoding:", bits_after_encoding)
# print("Compression Ratio:", compression_ratio, "%")
# print("Entropy:", entropy)
# print("Average Length:", average_length)
# print("Efficiency:", efficiency)





