file_path = input()
with open(file_path, "r") as file:
    genome = [line.strip() for line in file.readlines()]
sequence_1 = genome[0]
sequence_2 = genome[1]

def HammingDistance(sequence_1, sequence_2):
    if len(sequence_1) != len(sequence_2):
        raise ValueError("Sequence must have the same length")
    diff = 0
    for nucleotide_1, nucleotide_2 in zip(sequence_1, sequence_2):
        if nucleotide_1 != nucleotide_2:
            diff += 1
    return diff

#print(hamming_distance(sequence_1, sequence_2))
