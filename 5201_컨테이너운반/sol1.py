import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 컨테이너와 트럭 배열 입력하기
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    # 컨테이너와 트럭을 오름차순으로 정렬
    containers.sort()
    trucks.sort()
    # 컨테이너 무게 기록할 cnt
    cnt = 0
    # 트럭과 컨테이너가 남아있는 동안
    while containers and trucks:
        # 남아있는 컨테이너 중 가장 무거운 것 꺼내기
        container = containers.pop()
        # 남아있는 트럭 중 가장 큰 것 꺼내기
        truck = trucks.pop()
        # 컨테이너를 운반할 수 있다면 무게를 합산
        if truck >= container:
            cnt += container
        # 운반할 수 없다면 트럭은 다시 넣고, 컨테이너는 버리기
        else:
            trucks.append(truck)
    print("#{} {}".format(tc, cnt))

