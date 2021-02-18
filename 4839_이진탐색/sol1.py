import sys
sys.stdin = open("input.txt")


# 전체 페이지 수, 타겟 페이지를 인자로 받아 타겟 페이지까지의 탐색 횟수를 반환하는 함수 binary_search
def binary_search(P, target):
    start = 1
    end = P
    cnt = 1
    while True:
        # mid 찾기
        mid = int((start + end) / 2)
        # mid가 타겟과 같다면 종료 후 탐색 횟수 반환
        if mid == target:
            return cnt
        # 타겟이 mid보다 크다면 mid를 시작점으로 갱신
        elif target > mid:
            start = mid
            cnt += 1
        # 타겟이 mid보다 작다면 mid를 끝점으로 갱신
        else:
            end = mid
            cnt += 1


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # A와 B가 페이지를 찾는데 사용한 횟수를 비교하여 result 값 설정
    if binary_search(P, A) < binary_search(P, B):
        result = 'A'
    elif binary_search(P, A) > binary_search(P, B):
        result = 'B'
    else:
        result = 0

    print("#{} {}".format(tc, result))

