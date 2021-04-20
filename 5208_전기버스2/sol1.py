import sys
sys.stdin = open("input.txt")


# 정류장 위치, 교환횟수, 배터리 잔량을 인자로 받는 함수
def get_minimum_change(k, change, energy):
    global minimum_change
    # 교환 횟수가 최소 교환 횟수보다 많거나, 배터리를 전 칸에서 다 썼을 경우 백트래킹
    if change >= minimum_change or energy < 0:
        return
    # 마지막 정류장에 도달하면 교환 횟수 갱신
    elif k == N-1:
        minimum_change = change
    # 진행과정
    else:
        # 배터리를 바꾼 경우
        get_minimum_change(k+1, change + 1, batteries[k]-1)
        # 배터리를 바꾸지 않은 경우
        get_minimum_change(k+1, change, energy-1)


T = int(input())
for tc in range(1, T+1):
    # 정류장의 수  N, 충전지 리스트 batteries
    batteries = list(map(int, input().split()))
    N = batteries.pop(0)
    # 교환횟수 change
    change = 0
    # 다음 정류장에서의 배터리량 energy
    energy = batteries[0] - 1
    # 최소 교환횟수를 최댓값으로 초기화
    minimum_change = N-1
    # 최소 교환 횟수 구하기
    get_minimum_change(1, change, energy)
    print("#{} {}".format(tc, minimum_change))

