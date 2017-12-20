## first question
def checksum1(row):
    return max(row)-min(row)

total_sum = 0
for row in open("/Users/yuchenchu/Desktop/advent2017_yuchen/xxx.txt"):
    row = [int(i) for i in row.split()]
    total_sum += checksum1(row)

print (total_sum)


## second question
def checksum2(row):
    for i in row:
        for j in row:
            if i >j and i//j == i/j:return  i//j

total_sum = 0
for row in open("/Users/yuchenchu/Desktop/advent2017_yuchen/xxx.txt"):
    row = [int(i) for i in row.split()]
    total_sum += checksum2(row)

print (total_sum)






