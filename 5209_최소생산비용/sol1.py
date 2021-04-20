import sys
sys.stdin = open("input.txt")


# 최소비용 구하는 함수
def get_minimum_cost(k, cost):
    global minimum_cost
    # 비용 계산 중 최소 비용보다 크다면 백트래킹
    if cost >= minimum_cost:
        return
    # 마지막 공장의 상품까지 정했다면 갱신
    elif k == N:
        minimum_cost = cost
    # 진행과정
    else:
        # 모든 상품 번호를 검토
        for i in range(N):
            # 아직 생산되지 않았다면
            if not used[i]:
                # 생산 기록
                used[i] = 1
                # 다음 공장의 생산 품목 결정하러 가기
                get_minimum_cost(k+1, cost+factories[k][i])
                # 생산 기록 지우고 다음 상품 확인
                used[i] = 0


T = int(input())
for tc in range(1, T+1):
    # 상품, 공장의 수 N
    N = int(input())
    # 만들어진 상품을 기록할 used 리스트
    used = [0 for x in range(N)]
    # 2차원 배열 factories에 공장별 상품의 생산비용을 기록
    factories = []
    for _ in range(N):
        factories.append(list(map(int, input().split())))
    # 생산비용 cost
    cost = 0
    # 최소 생산비용을 최댓값으로 초기화
    minimum_cost = 15*99
    # 최소비용 구하기
    get_minimum_cost(0, cost)
    print("#{} {}".format(tc, minimum_cost))

