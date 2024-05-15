import tkinter as tk
from tkinter import messagebox
import math

def run_length_encoding(message):
    encoded_message = ""
    count = 1
    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            encoded_message += message[i - 1] + str(count)
            count = 1
    encoded_message += message[-1] + str(count)
    return encoded_message


def calculate_bits(message):
    return len(message) * 8


def calculate_compression_ratio(original_bits, encoded_bits):
    return (original_bits/encoded_bits)



def compress_message(input):
    input = str(input).strip()
    message = input
    # message = text_input.get("1.0", tk.END).strip()

    # Original bits
    original_bits = calculate_bits(message)

    # Run Length Encoding
    rle_encoded = run_length_encoding(message)
    rle_encoded_bits = calculate_bits(rle_encoded)

    # Calculate compression ratio
    rle_compression_ratio = calculate_compression_ratio(original_bits, rle_encoded_bits)

    # Display the results
    # results_text.delete("1.0", tk.END)
    # results_text.insert(tk.END, "Original Message:\n{}\n\n".format(message))
    # results_text.insert(tk.END, "Compression Techniques:\n")

    # results_text.insert(tk.END, "Run Length Encoding (RLE):\n")
    # results_text.insert(tk.END, "Bits before encoding: {}\n".format(original_bits))
    # results_text.insert(tk.END, "Bits after encoding: {}\n".format(rle_encoded_bits))
    # results_text.insert(tk.END, "Compression ratio: {}%\n\n".format(rle_compression_ratio))
    return rle_encoded_bits,rle_compression_ratio
