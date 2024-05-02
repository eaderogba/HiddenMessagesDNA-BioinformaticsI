import Neighbors

file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/dataset_30278_9.txt"
with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]
sequence = lines[0]
k_int = int(lines[1][0])
d_int = int(lines[1][2])

def FrequentWordsWithMismatches(Text, k, d):
    """This function finds the most frequent substrings of length k in the input Text, allowing for up to d mismatches."""
    Patterns = [] # An empty array that stores the most frequent substrings
    freqMap = {} # An empty map that stores the frequency of each substring
    n = len(Text)
    # Iterate through each starting position in Text
    for i in range(1, n - k + 1):
        pattern = Text[i:i+k] # Extracts a substring of lenght k starting at position i
        # Generating Neighborhood
        # Get the set of al strings within d mismatches of Pattern using the 'Neighbors' function
        neighborhood = Neighbors.Neighbors(Pattern, d)
        for neighbor in neighborhood:
            # Counting frequencies
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] += 1
    # Finding maximum frequency from the values store in 'freqMap'      
    m = max(freqMap.values())
    for Pattern in freqMap.items():
        if freqMap[Pattern] == m:
            Patterns.append(Pattern)
    return ' '.join(Patterns)

FrequentWordsWithMismatches(Text=sequence, k=k_int, d=d_int)
