import itertools
def passphrases1(line):
    if len(line) == len(set(line)):return 1
    return 0

def passphrases2(line):
    if len(line) != len(set(line)):return 0
    for word in line:
        temp = set(["".join(i) for i in itertools.permutations(word)])
        temp.remove(word)
        for i in line:
            if i in temp:return 0
    return 1


total_sum = 0
for line in open("/Users/yuchenchu/Desktop/advent2017_yuchen/puzzle_input.txt"):
    line = [i for i in line.split()]
    total_sum += passphrases1(line)
print ('passphrases1',total_sum)

total_sum = 0
for line in open("/Users/yuchenchu/Desktop/advent2017_yuchen/puzzle_input.txt"):
    line = [i for i in line.split()]
    total_sum += passphrases2(line)


print ('passphrases2',total_sum)

