# 2020/5/20 megumik
# coding: utf-8

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count


def FrequentWords(Text, k):
    frequent_patterns = set()
    count = []
    for i in range(len(Text) - k + 1):
        pattern = Text[i: i+k]
        #print(pattern)
        count.append(PatternCount(Text,pattern))
    max_count = max(count)
    for i in range(len(Text) - k + 1):
        if count[i] == max_count:
            frequent_patterns.add(Text[i: i+k])
    return list(frequent_patterns)


if __name__ == '__main__':
    with open("data/dataset_2_10.txt") as f:
        text, k = f.read().strip().split("\n")
        freq_words = FrequentWords(text, int(k))

    print(freq_words)