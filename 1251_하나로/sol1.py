import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    # 섬의 개수
    N = int(input())
    # 섬들의 x좌표
    xs = list(map(int, input().split()))
    # 섬들의 y좌표
    ys = list(map(int, input().split()))
    # 세율
    E = float(input())

    # 거리의 제곱을 모두 최대로 설정한 리스트
    length_squares = [(1000000**2 + 1000000**2)]*N
    # mst 추가 여부 리스트
    mst = [0]*N
    # mst 추가 카운트
    cnt = 0
    # mst 간선 가중치(거리의 제곱)의 합
    sum_length_square = 0

    # 0번 섬을 mst에 추가, 현재 노드로 설정
    length_squares[0] = 0
    mst[0] = 1
    cnt += 1
    current = 0

    # 0번 섬을 시작으로 mst 만들기
    while cnt < N:
        # length_squares 갱신
        for i in range(N):
            length_square = (xs[i] - xs[current])**2 + (ys[i] - ys[current])**2
            if length_square < length_squares[i]:
                length_squares[i] = length_square
        # 다음 연결할 섬 결정하기: 다음섬 min_next
        # 방문하지 않은 가장 첫번째 섬 찾기
        for i in range(N):
            if not mst[i]:
                min_next = i
                break
        # 거리를 비교하며 가장 가까운 섬으로 갱신하기
        for i in range(min_next+1, N):
            if length_squares[i] < length_squares[min_next] and not mst[i]:
                min_next = i
        # 다음 섬 연결, 기록 및 비용의 길이의제곱 합산
        mst[min_next] = 1
        cnt += 1
        sum_length_square += length_squares[min_next]
        # 현재 노드를 갱신
        current = min_next

    result = round(sum_length_square * E)

    print("#{} {}".format(tc, result))

