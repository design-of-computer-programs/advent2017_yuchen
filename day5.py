
ls_order = []
for line in open("/Users/yuchenchu/Desktop/advent2017_yuchen/puzzle_input.txt"):
    ls_order.append(int(line.split()[0]))

cur_pos, count = 0, 0

while cur_pos in range(0,len(ls_order)):
    temp = cur_pos
    cur_pos += ls_order[cur_pos]
    if ls_order[temp] < 3: ls_order[temp] += 1
    else:ls_order[temp] -= 1

    count += 1



print (count)
