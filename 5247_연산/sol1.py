import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    # 시작 숫자 N, 목표 숫자 M
    N, M = map(int, input().split())
    # 시작 숫자와 연산 수를 튜플로 추가
    q = [(N, 0)]
    # 사용 기록
    used = [0] * 10000001
    # pop(0)보다 시간이 빠른 front 인덱스 사용 위해 current 설정
    current = -1
    # bfs
    while q:
        # front를 한칸 이동
        current += 1
        # front의 튜플을 이용
        value, cnt = q[current]
        # 값을 찾았다면 result 할당 후 break
        if value == M:
            result = cnt
            break
        # 찾는 값이 아니라면 네 가지 연산 하여 값 및 연산 횟수를 튜플로 큐에 추가
        for next_val in [value+1, value-1, value*2, value-10]:
            if 0 < next_val <= 1000000 and not used[next_val]:
                q.append((next_val, cnt+1))
                used[next_val] = 1
    print("#{} {}".format(tc, result))

