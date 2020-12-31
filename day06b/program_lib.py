import re


def calculate():
    fo = open("data.txt", "r+")
    lines = fo.readlines()
    total = 0
    grp = []
    for line in lines:
        line = line.strip()
        if line == "":
            total += group_sum(grp)
            grp = []
        else:
            grp.append(line)

    total += group_sum(grp)
    return total

def group_sum(lines):
    group_results = 2**26 - 1
    for line in lines:
        group_results &= person_binary(line)
    return sum(int(b) for b in "{0:b}".format(group_results))

def person_binary(answers):
    hash = 0
    for letter in answers:
        hash |= 2**order_number(letter)
    return hash

def order_number(letter):
    return ord(letter) - ord('a')
