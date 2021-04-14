# SWEA 제출 오류
# line 124 ~ 126: string 받을 때, 정확한 길이로 잘라서 받으니 작동, window 포맷 문제

import sys
sys.stdin = open("input.txt")


T = int(input())


dict_bin = {'0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111',
}


# 한 줄을 2진수로 바꿔주는 함수
def make_line_bin(line):
    # 이진수 스트링 초기화
    line_bin = ''
    # 한 문자씩 이진수로 만들어 이진수 스트링에 추가
    for char in line:
        line_bin += dict_bin.get(char)
    return line_bin


code_match = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}


# 2진수 스트링을 받아 암호코드의 합 출력하는 함수
def sum_of_secret_codes(bin_line):
    bin_line = list(bin_line)
    codes = []
    # 한 줄의 처음부터 끝까지 확인
    for x in range(len(bin_line)):
        if bin_line[x] == '1':
            # 1 시작점 찾기 one_start
            one_start = x
            current = x
            # 0 시작점 찾기 zero_start
            while current <= len(bin_line):
                current += 1
                if bin_line[current] == '0':
                    zero_start = current
                    break
            # 다음 1 시작점 찾기 last_start
            while current <= len(bin_line):
                current += 1
                if bin_line[current] == '1':
                    last_start = current
                    break
            # 끝점 찾기 last_end
            while current <= len(bin_line):
                current += 1
                if bin_line[current] == '0':
                    last_end = current - 1
                    break
                else:
                    last_end = current - 1
            # 검색한 부분 0으로 만들어주기
            for k in range(x, current):
                bin_line[k] = '0'
            # 표시한 점들로 길이 재서 암호 숫자 추가하기
            first_digit = zero_start - one_start
            second_digit = last_start - zero_start
            third_digit = last_end - last_start + 1
            # 비율로 만들기 위해 가장 작은 수로 나눠주기
            ratio_minimum = min([first_digit, second_digit, third_digit])
            first_digit = int(first_digit / ratio_minimum)
            second_digit = int(second_digit / ratio_minimum)
            third_digit = int(third_digit / ratio_minimum)
            # 스트링으로 만들어주기
            digits = str(first_digit) + str(second_digit) + str(third_digit)
            # 해독한 숫자를 추가해주기
            codes.append(code_match.get(digits))
    code_sum = 0
    # 암호코드 검증
    while codes:
        if ((sum(codes[0:8:2])) * 3 + sum(codes[1:8:2])) % 10 == 0:
            code_sum += sum(codes[0:8])
        codes = codes[8:]
    return code_sum


# 코드가 있는 줄에서 해당 코드를 모두 0으로 바꾸는 함수
def erase_code(line):
    for x in range(len(line)):
        if line[x] != '0':
            current = i
            while current < N and array[current][x] != '0':
                array[current][x] = '0'
                current += 1


for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = []
    # 2차원 배열 입력받기
    for i in range(N):
        info = input()
        info = info[0:M]
        array.append(list(info))
    # 16진수 코드 리스트 확인하며, 0이 아닌 것이 있다면 해당 줄에서 시행
    result = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] != '0':
                # string binary_line
                binary_line = make_line_bin(array[i])
                result += sum_of_secret_codes(binary_line)
                erase_code(array[i])

    print("#{} {}".format(tc, result))