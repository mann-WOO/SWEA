import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 메모리 입력받기
    memory = input()
    # 현재 비트의 상태 current를 '0'으로 초기화
    current = '0'
    # 비트 조작 횟수 cnt
    cnt = 0
    # 모든 비트에 대해
    for bit in memory:
        # 검사한 비트가 현재 비트의 상태와 다를때, current 갱신 및 cnt에 1 합산
        if bit != current:
            current = bit
            cnt += 1

    print("#{} {}".format(tc, cnt))

