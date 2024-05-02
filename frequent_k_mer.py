"""This code reads sequence data from a file, and using the value of the k-mers provided computes the frequency of k-mers in the sequence, and identifies the most frequent k-mers."""

from collections import Counter

# FIle path to the sequence file
file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/dataset_30274_5.txt"

# Read the file and strip whitespace
with open(file_path, "r") as file:
    sequence_lines = [line.strip() for line in file.readlines()]

# Extract the integer value from the second line of the file
sequence_values = sequence_lines[1].split()
sequence_value = [int(val) for val in sequence_values]

# Function to compute frequency table of k-mers in Text
def FrequencyTable(Text, k):
    # Use Counter to count the occurrences of k-mers in Text
    return Counter(Text[i:i+k] for i in range(len(Text) - k + 1))

# Function to find most frequent k-mers in Text
def BetterFrequentWords(Text, k):
    # Get frequency table of k-mers in Text
    freqMap = FrequencyTable(Text, k)
    # FInd th maximum frequency among the k-mers
    max_freq = max(freqMap.values())
    # Return k-mers with frequency equal to the maximum frequency
    return [pattern for pattern, freq in freqMap.items() if freq == max_freq]


# Print the most frequent k-mers in the sequence
print(BetterFrequentWords("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA", 3))
