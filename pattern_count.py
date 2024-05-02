file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/dataset_30272_6.txt"

# Initialize empty list
sequence_lines = []

# Open the file in read mode
with open(file_path, "r") as file:
    for line in file:
        # Remove any leading/trailing whitespace and add the line to the list
        sequence_lines.append(line.strip())

sequence_pattern = sequence_lines[1]

def PatternCount(text, pattern):
    pattern_len = len(pattern)
    text_len = len(text)
    count = 0

    # Initialize the window
    window = text[:pattern_len]

    # Slide the window through the text
    for i in range(1, text_len - pattern_len + 1):

        # Remove the leftmost character and add the next character
        window = window[1:] + text[i + pattern_len - 1]
        # Compare the initial window with the pattern
        if window == pattern:
            count += 1
    return count


print(PatternCount(
    "ACTGTACGATGATGTGTGTCAAAG", "TGT"))

