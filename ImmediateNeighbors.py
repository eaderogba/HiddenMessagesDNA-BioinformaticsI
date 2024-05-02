file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/dataset_30274_5.txt"

# Read the file and strip whitespace
with open(file_path, "r") as file:
    sequence_lines = [line.strip() for line in file.readlines()]

def ImmediateNeighbors(Pattern):
    """This function creates a set of strings where each string is the same as the input string Pattern, but with one of its nucleotides changed. It does this for every position in the input string, generating all possible variations with one nucleotide difference."""
    Neighborhood = set() # An empty set is initialized to store the generated strings

    # Loop through each position in the pattern
    for i in range(len(Pattern)):
        symbol = Pattern[i] # Obtains the nucleotide at the current position

        # Generates the 3 possible nucleotides that can replace the symbol nucleotide
        replacements = {'A', 'B', 'C', 'G'} - {symbol}

        # Generates new strings by replacing the symbol nucleotide with the replacement
        for replacement in replacements:
            neighbor = Pattern[:i] + replacement + Pattern[i+1:] # Construct the new string
            Neighborhood.add(neighbor) # Add the new string to the set
    return Neighborhood
print(ImmediateNeighbors(Pattern=sequence_lines))
