import sys
sys.stdin = open("input.txt")

T = 10

# 트리 탐색 함수
def tree_search(node, N):
    # 존재하지 않는 노드의 경우 리턴
    if node > N:
        return
    # 왼쪽 자식 탐색
    tree_search(node*2, N)
    # 정점의 값을 결과에 추가
    result.append(tree[node])
    # 오른쪽 자식 탐색
    tree_search(node*2+1, N)


for tc in range(1, T+1):
    # 입력받기: 하나의 리스트로 구성
    N = int(input())
    tree = [0]*(N+1)
    for _ in range(N):
        info = input().split()
        index = int(info[0])
        val = info[1]
        tree[index] = val
    # 결과 저장할 리스트
    result = []
    # 탐색
    tree_search(1, N)

    print("#{} {}".format(tc, ''.join(result)))

