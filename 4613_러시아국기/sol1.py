import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    # 깃발의 높이 N, 너비 M
    N, M = map(int, input().split())
    # 깃발 입력받기
    flag = []
    for _ in range(N):
        flag.append(input())
    # 색 바꾸는 최소 횟수 min_change
    min_change = N*M
    # 흰색의 끝줄 idx는 0 ~ N-3의 값을 가짐
    for we in range(0, N-2):
        # 파란색의 끝줄 idx는 we+1 ~ N-2의 값을 가짐
        for be in range(we+1, N-1):
            # 흰색 끝줄, 파란색 끝줄 경우의 수마다 바꾸는 횟수 change
            change = 0
            # 흰색 끝줄까지 W가 아닌 원소들의 수를 change에 합산
            for i in range(0, we+1):
                change += M - flag[i].count('W')
            # 파란색에서 합산
            for i in range(we+1, be+1):
                change += M - flag[i].count('B')
            # 붉은색에서 합산
            for i in range(be+1, N):
                change += M - flag[i].count('R')
            # 색 바꾸기 횟수의 최솟값 갱신
            if change < min_change:
                min_change = change
    print("#{} {}".format(tc, min_change))

