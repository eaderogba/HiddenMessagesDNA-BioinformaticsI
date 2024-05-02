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


print(PatternWithMisMatches(
    genome="AACAAGCTGATAAACATTTAAAGAG", pattern="AAAAA", integer=2))