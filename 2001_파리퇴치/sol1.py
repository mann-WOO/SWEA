import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    # 2차원 배열 입력받기
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 파리를 죽일 수 있는 최댓값 max_kill을 초기화
    max_kill = 0
    # (0,0) ~ (N-M,N-M) 의 좌표를 가지는 원소에 대해 실행
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            # 한 구역에서 죽일 수 있는 파리의 수 kill을 초기화
            kill = 0
            # 해당 원소를 기준으로 파리채 크기 M 범위만큼 오른쪽, 아래쪽에 있는 값을 kill에 합산
            for k in range(M):
                for l in range(M):
                    kill += arr[i+k][j+l]
            # kill이 max_kill보다 높다면 갱신
            if kill > max_kill:
                max_kill = kill

    print("#{} {}".format(tc, max_kill))

