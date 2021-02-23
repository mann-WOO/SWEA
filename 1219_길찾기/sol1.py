import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    test_case, N = map(int, input().split())
    # 순서쌍 입력받기
    roads = list(map(int, input().split()))
    # 길의 방향 입력받기
    first_data = [0] * 100
    second_data = [0] * 100
    for i in range(1, len(roads), 2):
        if first_data[roads[i-1]] == 0:
            first_data[roads[i-1]] = roads[i]
        else:
            second_data[roads[i-1]] = roads[i]

    # 결과 변수 result를 0으로 초기화
    result = 0
    # 시작점을 stack에 추가
    stack = [0]
    # 스택을 비울때까지 dfs
    while stack:
        # 가장 마지막에 쌓은 지점을 pop하여 n으로 선언
        n = stack.pop()
        # n에서 도착지에 갈 수 있다면 result에 1을 할당
        if first_data[n] == 99 or second_data[n] == 99:
            result = 1
        # n에서 다른 곳으로 갈 수 있다면 스택에 추가
        if first_data[n]:
            stack.append(first_data[n])
        if second_data[n]:
            stack.append(second_data[n])


    print("#{} {}".format(tc, result))

