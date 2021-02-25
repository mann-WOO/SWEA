import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # 박스 배열 boxes
    boxes = [0] * N
    # Q번 바꾸기
    for i in range(1, Q+1):
        # L, R 입력받기
        L, R = map(int, input().split())
        # L부터 R번 박스 번호 바꾸기
        for j in range(L-1, R):
            boxes[j] = i
    result = ' '.join(list(map(str, boxes)))
    print("#{} {}".format(tc, result))

