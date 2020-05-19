# 2020/mm/dd megumik
# coding: utf-8


def PatternMatching(Pattern, Genome):
    loc = []
    for idx in range(len(Genome) - len(Pattern) + 1):
        if Genome[idx: idx+len(Pattern)] == Pattern:
            loc.append(idx)
    return loc


if __name__ == '__main__':
    with open("data/dataset_3_5.txt") as f:
        pattern, genome = f.read().rstrip().split()
        loc = PatternMatching(pattern, genome)

    with open("answer/dataset_3_5_answer.txt", "w") as fout: 
        fout.write(" ".join(map(str, loc)) + "\n")

    print(loc)