import sys
sys.stdin = open("input.txt")

T = int(input())


# 중위 순회로 서브트리의 크기를 구하는 함수 size
def size(node):
    global tree_size
    if node > 0:
        size(left_child[node])
        tree_size += 1
        size(right_child[node])


for tc in range(1, T+1):
    V, E, a, b = map(int, input().split())
    # 각 노드의 부모 노드를 기록할 parent_tree 리스트
    parent_tree = [0] * (V+1)
    # 각 노드의 왼쪽, 오른쪽 자식을 기록할 리스트들
    left_child = [0] * (V+1)
    right_child = [0] * (V+1)
    info = list(map(int, input().split()))
    
    # 트리를 리스트로 표현하기
    for _ in range(E):
        child = info.pop()
        parent = info.pop()
        # parent_tree 채워주기
        parent_tree[child] = parent
        # left, right_child 채워주기
        if left_child[parent] == 0:
            left_child[parent] = child
        else:
            right_child[parent] = child

    # a의 조상리스트 ancestors 만들기
    ancestors = []
    current = a
    while current != 1:
        ancestors.append(parent_tree[current])
        current = parent_tree[current]

    # b의 조상들을 확인하면서 가장 가까운 공통조상 찾기
    current = b
    while current != 1:
        if parent_tree[current] in ancestors:
            shared_ancestor = parent_tree[current]
            break
        else:
            current = parent_tree[current]

    # 공통조상을 루트로 하는 서브트리의 사이즈 구하기
    # 루트 노드가 공통조상인 경우 계산 생략
    if shared_ancestor == 1:
        tree_size = V
    else:
        tree_size = 0
        size(shared_ancestor)

    # 정답
    print("#{} {} {}".format(tc, shared_ancestor, tree_size))

