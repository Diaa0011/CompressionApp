import heapq
from collections import Counter
import math
import sys
import io
import graphviz
import matplotlib.pyplot as plt



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

    def lt(self, other):
        # Define how this node should compare to another node based on frequency
        # Compares two nodes based on their frequency
        return self.freq < other.freq

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
            # In a Huffman tree, nodes can be either internal (with children) or leaf nodes (without children).
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
    compressed_text = "".join(code_map[char] for char in text)

    return compressed_text, code_map, huffman_tree

# Example usage
# text = "Hello i'm Karim"
# compressed_text, code_map, huffman_tree = huffman_compress(text)

# Function to visualize Huffman Tree using graphviz
def visualize_huffman_tree(node, graph=None):
    if graph is None:
        graph = graphviz.Digraph()

    if node:
        # Add node to graph
        label = str(node.freq) if node.char is None else f"{node.char}: {node.freq}"
        graph.node(str(id(node)), label=label)

        if node.left:
            graph.edge(str(id(node)), str(id(node.left)), label="0")
            visualize_huffman_tree(node.left, graph)

        if node.right:
            graph.edge(str(id(node)), str(id(node.right)), label="1")
            visualize_huffman_tree(node.right, graph)

    return graph

# Visualize the Huffman tree
# graph = visualize_huffman_tree(huffman_tree)
# image_bytes = graph.pipe(format='png')

# Convert image bytes to a file-like object
# image_file = io.BytesIO(image_bytes)

# # Display the image
# plt.imshow(plt.imread(image_file), aspect='equal')
# plt.axis('off')
# plt.show()