import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 16진수 숫자 입력받기
    N, hex_nums = input().split()
    N = int(N)
    hex_nums = list(hex_nums)
    # 결과값 저장할 스트링 선언
    bin_string = ''
    # 각 16진수 숫자에 대해
    for i in range(N):
        # 10진수 변환
        oct_num = int(hex_nums[i], 16)
        # 2진수 저장할 빈 스트링
        bin_number = ''
        # 첫 번째 자리부터 채우기(2**n으로 나누고 몫을 입력)
        bin_number += str(oct_num // 8)
        oct_num = oct_num % 8
        bin_number += str(oct_num // 4)
        oct_num = oct_num % 4
        bin_number += str(oct_num // 2)
        oct_num = oct_num % 2
        bin_number += str(oct_num)
        # 결과값 스트링에 추가
        bin_string += bin_number

    print("#{} {}".format(tc, bin_string))

