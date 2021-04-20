# 문제 설명을 잘 읽자

import sys
sys.stdin = open("input.txt")


# 번갈아 하는 이진탐색일때만 cnt에 1을 합산하는 함수
def binary_search(k):
    global cnt
    # 양 끝점 설정
    l, r = 0, N - 1
    # 이전 선택 구간을 기억하는 prev
    prev = 0
    # l, r 이 교차하기 전까지
    while l <= r:
        # 중앙값 설정
        mid = (l+r) // 2
        # 탐색 성공시
        if A[mid] == k:
            cnt += 1
            return
        # 왼쪽을 선택
        elif A[mid] > k:
            # 전에도 왼쪽을 선택했다면 그만함
            if prev == -1:
                return
            r = mid - 1
            prev = -1
        # 오른쪽을 선택
        else:
            # 전에도 오른쪽을 선택했다면 그만함
            if prev == 1:
                return
            l = mid + 1
            prev = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(M):
        binary_search(B[i])
    print("#{} {}".format(tc, cnt))

