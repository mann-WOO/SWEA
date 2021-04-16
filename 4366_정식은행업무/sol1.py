import sys
sys.stdin = open("input.txt")


# 2진수 리스트를 10진수로 바꿔 경우의수 리스트에 추가하는 함수
def bin_to_dec(bin_list):
    dec_value = 0
    exp = 0
    copied_list = bin_list[:]
    for _ in range(len(bin_list)):
        bin_digit = copied_list.pop()
        dec_value += int(bin_digit) * (2**exp)
        exp += 1
    bin_possible.append(dec_value)


# 3진수 리스트를 10진수로 바꿔 경우의수 리스트에 추가하는 함수
def tri_to_dec(tri_list):
    dec_value = 0
    exp = 0
    copied_list = tri_list[:]
    for _ in range(len(tri_list)):
        tri_digit = copied_list.pop()
        dec_value += int(tri_digit) * (3**exp)
        exp += 1
    tri_possible.append(dec_value)


T = int(input())
for tc in range(1, T+1):
    # 2진수, 3진수 리스트로 입력받기
    bin_incorrect = list(input())
    tri_incorrect = list(input())
    # 가능한 경우의수 담을 리스트
    bin_possible = []
    tri_possible = []
    # 2진수에서 가능한 경우의수 만들기
    for i in range(len(bin_incorrect)):
        if bin_incorrect[i] == '0':
            bin_incorrect[i] = '1'
            bin_to_dec(bin_incorrect)
            bin_incorrect[i] = '0'
        else:
            bin_incorrect[i] = '0'
            bin_to_dec(bin_incorrect)
            bin_incorrect[i] = '1'
    # 3진수에서 가능한 경우의수 만들기
    for i in range(len(tri_incorrect)):
        if tri_incorrect[i] == '0':
            tri_incorrect[i] = '1'
            tri_to_dec(tri_incorrect)
            tri_incorrect[i] = '2'
            tri_to_dec(tri_incorrect)
            tri_incorrect[i] = '0'
        elif tri_incorrect[i] == '1':
            tri_incorrect[i] = '0'
            tri_to_dec(tri_incorrect)
            tri_incorrect[i] = '2'
            tri_to_dec(tri_incorrect)
            tri_incorrect[i] = '1'
        else:
            tri_incorrect[i] = '0'
            tri_to_dec(tri_incorrect)
            tri_incorrect[i] = '1'
            tri_to_dec(tri_incorrect)
            tri_incorrect[i] = '2'
    # 일치하는 것 찾기
    for num in bin_possible:
        if num in tri_possible:
            result = num
            break
    print("#{} {}".format(tc, result))

