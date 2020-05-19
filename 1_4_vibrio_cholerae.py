# 2020/5/20 megumik
# coding: utf-8


def PatternMatching(Pattern, Genome):
    loc = []
    for idx in range(len(Genome) - len(Pattern) + 1):
        if Genome[idx: idx+len(Pattern)] == Pattern:
            loc.append(idx)
    return loc


if __name__ == '__main__':
    with open("data/Vibrio_cholerae.txt", "r") as f:
        genome = f.read().strip()
    pattern = "CTTGATCAT"
    print(*PatternMatching(pattern, genome), sep=" ")