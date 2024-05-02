file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/Vibrio_cholerae.txt"
pattern = "ATGATCAAG"
with open(file_path, "r") as file:
    sequence_lines = [line.strip() for line in file.readlines()]

def pattern_checker(pattern, genome):
    pattern_len = len(pattern)
    genome_len = len(genome)
    positions = []

    # Initialize the window
    window = genome[:pattern_len]

    # Slide the window through the text
    for i in range(0, genome_len - pattern_len + 1):

        # Remove the leftmost character and add the next character
        window = window[1:] + genome[i + pattern_len - 1]
        # Compare the initial window with the pattern
        if window == pattern:
            positions.append(i)
    return ' '.join(map(str, positions))

print(pattern_checker("ATA", "GACGATATACGACGATA"))
