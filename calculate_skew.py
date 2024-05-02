file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/dataset_30277_10.txt"
with open(file_path, "r") as file:
    genome = [line.strip() for line in file.readlines()]

def calculate_skew(sequence):
    skew = [0]  # Skew0 is 0

    for nucleotide in sequence:
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    return skew

skew_values = calculate_skew(sequence=genome[0])
print(skew_values)

def min_skew(skew_values):
    min_value = min(skew_values)
    min_positions = [i for i, value in enumerate(skew_values) if value == min_value]
    return min_positions
print(min_skew(skew_values))