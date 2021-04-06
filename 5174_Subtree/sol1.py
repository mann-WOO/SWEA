import sys
sys.stdin = open("input.txt")

T = int(input())


# 중위순회하면서 노드 수 더하는 함수
def tree_search(node):
    global count
    if node > 0:
        tree_search(left[node])
        count += 1
        tree_search(right[node])


for tc in range(1, T+1):
    E, N = map(int, input().split())
    info = list(map(int, input().split()))
    # 두 개의 리스트로 트리 구현
    left = [0] * (E+2)
    right = [0] * (E+2)
    # 인덱스: 부모, 값: 자식
    while info:
        child = info.pop()
        parent = info.pop()
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child
    # 노드 수 count 초기화
    count = 0
    # 중위순회
    tree_search(N)

    print("#{} {}".format(tc, count))

