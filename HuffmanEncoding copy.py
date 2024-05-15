import heapq
from collections import Counter, defaultdict
import math
import sys



class Node:
    def __init__(self, char, freq):
        self.char = char  # Character stored in the node
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child node
        self.right = None  # Right child node

    def __lt__(self, other):
        # Define how this node should compare to another node based on frequency
        # Compares two nodes based on their frequency
        return self.freq < other.freq


# In[33]:


def build_huffman_tree(frequencies):
    # Create a priority queue (min-heap) of leaf nodes
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Combine nodes until there's only one left, forming the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    return heap[0]  # The root of the Huffman Tree

def generate_huffman_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if node:
        if node.char is not None:
            # If it's a leaf node, save the code
            #In a Huffman tree, nodes can be either internal (with children) or leaf nodes (without children). 
            code_map[node.char] = prefix
        else:
            # Recur to the left and right children with updated prefix
            generate_huffman_codes(node.left, prefix + "0", code_map)
            generate_huffman_codes(node.right, prefix + "1", code_map)

    return code_map 



def huffman_compress(text):
    # Step 1: Calculate frequency of characters in the text
    frequencies = Counter(text)

    # Step 2: Build the Huffman Tree
    huffman_tree = build_huffman_tree(frequencies)

    # Step 3: Generate Huffman codes
    code_map = generate_huffman_codes(huffman_tree)

    # Step 4: Compress the text using the generated codes
    #With the Huffman codes generated, the function compresses the original text by replacing each character with its corresponding Huffman code.
    #This step creates the compressed version of the text, where each character is replaced by its Huffman code, resulting in a shorter representation of the text.
    #Example: If the original text is "hello" and the Huffman codes are {'h': '00', 'e': '01', 'l': '10', 'o': '11'}, the compressed text would be '0001101011'.
    
    compressed_text = "".join(code_map[char] for char in text)

    return compressed_text, code_map, huffman_tree

# Example usage
# text = "Hello i'm Karim"
# compressed_text, code_map, huffman_tree = huffman_compress(text)
# print("Huffman Codes:", code_map)
# print("Compressed Text:", compressed_text)


# Function to calculate various metrics
def calculate_metrics(text):
    # Original bits before encoding
    bits_before = len(text) * 8

    # Huffman compression
    compressed_text, code_map, huffman_tree = huffman_compress(text)

    # Bits after encoding
    bits_after = len(compressed_text)

    # Compression ratio
    compression_ratio = (bits_before/bits_after)

    # Character probabilities
    total_chars = len(text)
    frequencies = Counter(text)
    probabilities = {char: freq / total_chars for char, freq in frequencies.items()}

    # Entropy
    entropy = -sum(prob * math.log2(prob) for prob in probabilities.values())

    # Average length of Huffman codes
    average_length = sum(probabilities[char] * len(code_map[char]) for char in probabilities)

    # Efficiency (ratio of entropy to average length)
    efficiency = entropy / average_length

    return  bits_before, bits_after, compression_ratio,probabilities,entropy,average_length,efficiency


# Example usage
text = "Hello i'mqwreqeafas"
metrics = huffman_compress(text)

print("Huffman Codes:", huffman_compress(text)[2])



# print("Metrics:", metrics)
# print("calculate_metrics: bits before: ",calculate_metrics(text)[0])
# print("calculate_metrics: bits after: ",calculate_metrics(text)[1])

# # print("calculate_metrics: CR: ",calculate_metrics(text)[2])

# compressed = huffman_compress(text)[0]
# print("Huffman Codes:", compressed)
# print("Compresed Using sys: ", sys.getsizeof(compressed))





