import hamming_problem

file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/dataset_30278_6.txt"
with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]
input_pattern = lines[0]
input_genome = lines[1]
input_integer = int(lines[2])

def PatternWithMisMatches(pattern, genome, integer):
    positions = []
    n = len(genome)
    k = len(pattern)
    for i in range(0, n - k + 1):
        window = genome[i:i+k]
        distance = hamming_problem.hamming_distance(pattern, window)
        if distance <= integer:
            positions.append(window)
    return len(positions)


print(PatternWithMisMatches(genome=input_genome, pattern=input_pattern, integer=input_integer))
