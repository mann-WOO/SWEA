import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 단어퍼즐의 크기 N, 단어길이 K
    N, K = map(int, input().split())
    arr = []
    # 단어퍼즐 모양 만들기
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 결과 값을 가질 변수 result 초기화
    result = 0

    # 모든 row 탐색
    for i in range(N):
        # 흰 칸의 길이를 기록할 변수 cnt 초기화
        cnt = 0
        # 한 row씩 확인
        for j in range(N):
            # 흰 칸일때 흰 칸의 길이에 1 합산
            if arr[i][j] == 1:
                cnt += 1
            # 컴은 칸이 나오면
            else:
                # 이전까지의 흰 칸 길이가 K 와 같은지 확인후 result에 1 합산
                if cnt == K:
                    result += 1
                # 흰 칸의 길이 초기화
                cnt = 0
        # 한 행의 마지막 칸이 흰 칸일 때 확인
        if cnt == K:
                result += 1

    # 같은 방식으로 모든 col 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
                result += 1

    print("#{} {}".format(tc, result))

