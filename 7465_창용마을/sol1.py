import sys
sys.stdin = open("input.txt")


# 그래프에 연결되었다면 대표노드를, 아니라면 자기 자신을 리턴하는 함수
def find_set(x):
    while roots[x] != x:
        x = roots[x]
    return x


T = int(input())
for tc in range(1, T+1):
    # 사람 수 N, 관계 수 M
    N, M = map(int, input().split())
    # 대표 노드 리스트: 자기 자신으로 초기화
    roots = [x for x in range(N+1)]
    # 서로 알고 있는 경우, 앞사람 그룹의 대표노드로 편입
    for i in range(M):
        frm, to = map(int, input().split())
        roots[find_set(to)] = find_set(frm)
    cnt = 0
    # 대표노드가 자기 자신인 경우만 숫자를 세서 출력
    # 두 집단이 따로 존재하다가 이어진 경우, roots에는 1, 2와 같이 두 집단이 존재할 수 있지만
    # roots[2]가 1이 되므로, 하나의 집단으로 처리된다.
    # 즉 위의 작업으로 대표노드가 자기 자신인 경우만 하나의 집단으로 처리됨.
    for i in range(1, N+1):
        if roots[i] == i:
            cnt += 1
    print("#{} {}".format(tc, cnt))

