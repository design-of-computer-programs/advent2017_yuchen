import math

def Manhattan_Distance(input_number):
    distance, n = 0, 0
    if input_number == 1 :return 0
    while input_number > math.pow((2*n+1), 2):
        n += 1

    r_btm = int(math.pow((2*n+1), 2))
    l_btm, l_top ,r_top= r_btm - 2*n, r_btm - 4*n, r_btm - 6*n
    if input_number in range(l_btm, r_btm+1): #input_number in bottom line
        mid = (l_btm + r_btm)/2
        return abs(input_number-mid) +n
    elif input_number in range(r_top, l_top+1): #input_number in top line
        mid = (r_top + l_top)/2
        return abs(input_number-mid) + n

    elif input_number in range(l_top, l_btm+1): #input_number in left line
        mid = (l_top + l_btm)/2
        return abs(input_number-mid)/2

    else: #input_number in right line
        if input_number != r_btm:
            mid = (r_top + math.pow((2*(n-1)+1), 2))/2
            return abs(input_number - mid) + n





print (Manhattan_Distance(289326))