import hamming_problem
file_path = "/home/eaderogba279/Bionformatics_Projects/Coursera_BioinformaticsI/dataset_30282_4.txt"
with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

sequence = lines[0]
number = int(lines[1])


def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    Neighborhood = set()

    # Obtains the suffix of 'Pattern' and find its neighbors within Hamming Distance 'd', storing these neighbors in a 'SuffixNeighbors'.
    SuffixNeighbors = Neighbors(Pattern[1:], d)

    # Generating Neighborhood: calculates the hamming distance between the suffix of 'Pattern' and 'Text' for each Text in SuffixNeighbors
    for Text in SuffixNeighbors:
        if hamming_problem.HammingDistance(Pattern[1:], Text) < d:
            # Add the string to the Neighborhood
            for x in ['A', 'C', 'G', 'T']:
                Neighborhood.add(x + Text)
        else:
            Neighborhood.add(Pattern[0] + Text)

    return Neighborhood

# print(Neighbors(Pattern=sequence, d=number))
