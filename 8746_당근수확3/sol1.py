import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = []
    # N x M의 2차원 밭 입력 받기
    for _ in range(N):
        field.append(list(map(int, input().split())))
    # 당근의 총 개수로 min_diff를 초기화
    min_diff = 0
    for i in range(N):
        for j in range(M):
            min_diff += field[i][j]
    # 첫 일꾼 수확영역의 오른쪽 아래 꼭지점을 (i,j)로 설정
    for i in range(N-1):
        for j in range(M-1):
            # 각 일꾼의 작업량 초기화
            worker1, worker2, worker3 = 0, 0, 0
            # 해당 지점에서 첫 일꾼의 작업량 합산
            for k in range(0, i+1):
                for l in range(0, j+1):
                    worker1 += field[k][l]
            # 두 번째 일꾼의 작업량 합산
            for k in range(0, i+1):
                for l in range(j+1, M):
                    worker2 += field[k][l]
            # 세 번째 일꾼의 작업량 합산
            for k in range(i+1, N):
                for l in range(M):
                    worker3 += field[k][l]
            # 세 일꾼의 작업량의 차이 계산 (세 명중 최대 - 최소)
            works = [worker1, worker2, worker3]
            max_work, min_work = worker1, worker1
            for w in works:
                if w < min_work:
                    min_work = w
                if w > max_work:
                    max_work = w
            diff = max_work - min_work
            # 작업량 차이가 현재까지의 최소 차보다 작다면 갱신
            if diff < min_diff:
                min_diff = diff

    print("#{} {}".format(tc, min_diff))

