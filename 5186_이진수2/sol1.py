import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 입력받은 float
    dec_num = float(input())
    # 정답 이진수 숫자의 문자열 bin_num
    bin_num = ''
    # 소수점 12자리까지 확인
    for i in range(1, 13):
        # 나눠줄 수 1/2, 1/4 ...
        d = 2**(-i)
        # 입력받은 float을 나눈 몫을 정수화하고, 이를 문자열로 정답 문자열에 추가
        bin_num += str(int(dec_num // d))
        # 나머지를 다음 루프에서 쓸 수로 지정
        dec_num = dec_num % d
        # 나머지가 0이라면 break
        if dec_num == 0:
            break
    # 12번 확인 후에도 나머지가 0이 아니라면 overflow
    if dec_num > 0:
        bin_num = 'overflow'
    print("#{} {}".format(tc, bin_num))

