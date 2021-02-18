import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = []
    # 10*10의 0으로 이루어진 2차원 리스트 생성
    for _ in range(10):
        arr.append([0]*10)
    # N번 정보를 입력받아 색칠하기
    for i in range(N):
        info = list(map(int, input().split()))
        # 왼쪽 꼭지점 row 좌표부터 오른쪽 꼭지점 row 좌표까지
        for j in range(info[0], info[2]+1):
            # 왼쪽 꼭지점 col 좌표부터 오른쪽 꼭지점 col 좌표까지
            for k in range(info[1], info[3]+1):
                # 주어진 색을 합산
                arr[j][k] += info[4]

    # 보라색(3)인 칸 수 세기
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt+=1

    print("#{} {}".format(tc, cnt))

