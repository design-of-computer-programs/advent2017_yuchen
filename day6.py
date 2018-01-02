ls_order = [int(x) for x in input().split()]
empty_collection = []
empty_collection.append(tuple(ls_order))
step = 0
while True:
    max_num, max_index = max(ls_order), ls_order.index(max(ls_order))
    ls_order[max_index] = 0
    cur = max_index+1
    while max_num > 0:
        if cur <= len(ls_order)-1:
            ls_order[cur] += 1; cur+=1 ; max_num-=1

        else:
            cur = 0;ls_order[cur]+=1;cur+=1;max_num-=1


    step += 1
    if tuple(ls_order) in empty_collection:
        break
    else:
        empty_collection.append(tuple(ls_order))

print (step)
print(step-empty_collection.index(tuple(ls_order)))



