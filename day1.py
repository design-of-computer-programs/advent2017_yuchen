
def get_sum1(captcha):
    return sum(int(captcha[i]) for i in range(len(captcha)) if captcha[i] == captcha[i-1])


def get_sum2(captcha):
    half_len = len(captcha)//2
    return sum(int(captcha[i]) for i in range(len(captcha)) if captcha[i] == captcha[i - half_len])


assert get_sum1('91212129') == 9
assert get_sum1('11') == 2
assert get_sum1('1234') == 0
assert get_sum2('12131415') == 4
assert get_sum2('123123') == 12

print('All tests pass')



captcha = input()
print (get_sum1(captcha))
print (get_sum2(captcha))