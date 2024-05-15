prepared_textForRLE = (
    "Run Length Encoding (RLE):\n"
    "Bits after encoding: {}\n"
    "Compression ratio: {}\n\n"
)

prepared_textForLZW = (
    "Lempel–Ziv–Welch (LZW):\n"
    "Compressed Data: {}\n"
    "Bits after encoding: {}\n"
    "Average Length: {}\n"
    "Compression Ratio: {}\n"
    "Efficiency: {}\n"
)

prepared_textForHuffmanEncoding = (
    "Huffman-Encoding:\n"
    "Compressed Data: {}\n"
    "Code_Map: {}\n"
    "Huffman_Tree: {}\n"
    "Bits after encoding: {}\n"
    "Character_Probabilities: {}\n"
    "Average Length: {}\n"
    "Compression Ratio: {}\n"
    "Efficiency: {}\n"
)

prepared_textForGolomb= (
    "Golomb-Encoding:\n"
    "Compressed Data: {}\n"
    "RLE: {}\n"
    "Bits after encoding: {}\n"
    "Average Length: {}\n"
    "Compression Ratio: {}\n"
    "Efficiency: {}\n"
)

prepared_textForArithmetic= (
    "Arithmetic-Encoding:\n"
    "Compressed Value: {}\n"
    "Ranges: {}\n"
    "Last-Range: {}\n"
    "Bits after encoding: {}\n"
    "Average Length: {}\n"
    "Compression Ratio: {}\n"
    "Efficiency: {}\n"
)
prepared_beforeCopression= (
    "Metrics-Before-Encoding:\n"
    "Bits before encoding:\n{}\n"
    "Entropy:\n{}\n"
)
BestOftheWestVars= "{}\t ,{}\t ,{}\t"
BestOftheWestNumbers = ("Compression_Ratio: {}\t ,Efficiency: {}\t ,Time: {}\t")


RLEBest="AAAAABBBCCCCDDDDXXXXX"
LZWBest="ABABABACADADAEAEAFAFAF"
HuffmanBest="MISSISSIPPI RIVER"
GolombBest= "244555555511111"
ArithmeticBest="HELLO, HOW ARE YOU?"