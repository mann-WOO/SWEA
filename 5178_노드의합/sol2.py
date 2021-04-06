import sys
sys.stdin = open("input.txt")

T = int(input())

def make_tree(node):
    if node > N:
        return 0
    left = make_tree(node*2)
    right = make_tree(node*2+1)
    if tree[node]:
        return tree[node]
    else:
        tree[node] = left + right
        return tree[node]

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # 노드의 수 N, 트리 구성
    tree = [0] * (N+1)
    # 리프 노드 채워주기
    for _ in range(M):
        index, val = map(int, input().split())
        tree[index] = val
    # 트리 구성
    make_tree(1)
    print("#{} {}".format(tc, tree[L]))

