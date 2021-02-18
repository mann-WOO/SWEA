T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 2차원 배열을 담을 arr 리스트 설정
    arr = []
    # 요소와 이웃한 요소와의 차의 절대값을 합산할 result 변수 선언
    result = 0
    # 2차원 배열 input을 받아옴
    for i in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    # 우하좌상 순서의 방향 지정 리스트 dr, dc 선언
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 이중 for 문을 통해 모든 원소에 접근
    for i in range(N):
        for j in range(N):
            # 각 원소에서 상하좌우에 접근
            for k in range(4):
                # 인덱스가 유효하다면 그 차이를 result에 합산
                if 0 <= i + dr[k] < N and 0 <= j + dc[k] < N:
                    result += abs(arr[i][j] - arr[i + dr[k]][j + dc[k]])

    # 결과를 return
    print("#{} {}".format(tc, result))

