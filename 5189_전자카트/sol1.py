import sys
sys.stdin = open("input.txt")


# 관리구역 순회하며 배터리 소모 최솟값 갱신하는 함수
def cart(i, end, current, battery):
    global min_battery
    # 끝까지 돌았을 때
    if i == end:
        # 사무실로 돌아가는 배터리량 합산
        battery += office[current][0]
        # 최솟값과 비교해 갱신
        if battery < min_battery:
            min_battery = battery
        # 사무실로 돌아가는 배터리량 다시 빼주기
        battery -= office[current][0]
    for k in range(i, end):
        # 순열 생성 - 자리 바꿔주기
        perm[i], perm[k] = perm[k], perm[i]
        # 현재 위치에서 다음 위치로 가는 배터리량 합산
        battery += office[current][perm[i]]
        # 현재 위치 기억
        prev = current
        # 다음 위치를 현재 위치로 갱신
        current = perm[i]
        # 현재 배터리 소비량이 최소 배터리 소비량보다 작은 경우에만 진행
        if battery < min_battery:
            cart(i+1, end, current, battery)
        # 원상복구
        battery -= office[prev][current]
        current = prev
        perm[i], perm[k] = perm[k], perm[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 이동간 배터리 소모량 배열 office
    office = []
    for _ in range(N):
        office.append(list(map(int, input().split())))
    # 배터리 소모 최솟값 초기화
    min_battery = 100*N
    # 배터리 사용량 초기화
    battery = 0
    # 순열 생성
    perm = [x+1 for x in range(N-1)]
    # 현재 위치 0
    current = 0
    # 관리구역 순회하며 배터리 소모 최솟값 갱신
    cart(0, N-1, current, battery)
    print("#{} {}".format(tc, min_battery))

