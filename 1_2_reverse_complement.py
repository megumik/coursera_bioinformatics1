# 2020/5/20 megumik
# coding: utf-8

def ReverseComplement(Pattern):
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    rc = ""
    for letter in Pattern[::-1]:
        rc += pairs[letter]
    return rc


if __name__ == '__main__':
    with open("data/dataset_3_2.txt") as f:
        rc = ReverseComplement(f.read().rstrip("\n"))
    with open("answer/dataset_3_2_answer.txt", "w") as fout:
        fout.write(rc+"\n")