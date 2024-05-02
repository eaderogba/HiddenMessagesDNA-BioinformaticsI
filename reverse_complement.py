"""
Find the reverse complement of a DNA string
"""
file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/dataset_30273_2.txt"

with open(file_path, "r") as file:
    sequence_lines = [line.strip() for line in file.readlines()]
    

def reverse_complement(text):
    reverse = text[::-1]
    reverse_string = ""

    for char in reverse:
        if char == 'A':
            reverse_string += "T"
        elif char == 'T':
            reverse_string += "A"
        elif char == 'G':
            reverse_string += "C"
        elif char == 'C':
            reverse_string += "G"
    return reverse_string


print(reverse_complement("TTGTGTC"))
