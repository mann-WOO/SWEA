import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 거듭제곱수로 만들 수 A
    A = int(input())
    # 2부터 A까지의 수 i에 대해
    for i in range(2, A+1):
        if A < i ** 2:
            break
        if A % i ** 2 == 0:
            A = A // i ** 2

    current = 2
    while A < current ** 2:
        if A % (current ** 2) == 0 :
            A = A // (current ** 2)

    print("#{} {}".format(tc, A))

