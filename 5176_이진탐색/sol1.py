import sys
sys.stdin = open("input.txt")

T = int(input())


# 이진탐색트리 만들기
def make_bst(node):
    global value
    # 노드 번호가 N을 넘어가면 리턴
    if node > N:
        return
    # 왼쪽 탐색
    make_bst(node*2)
    # 노드에 값 부여 1씩 증가
    tree[node] = value
    value += 1
    # 오른쪽 탐색
    make_bst(node*2+1)


for tc in range(1, T+1):
    N = int(input())
    # 트리의 크기 설정
    tree = [0] * (N+1)
    # 노드에 부여하는 값 초기화
    value = 1
    # 이진 탐색트리 생성
    make_bst(1)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))