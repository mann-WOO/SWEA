import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # s, e 쌍 works 리스트에 입력
    works = []
    for _ in range(N):
        works.append(list(map(int, input().split())))
    # 끝나는 시간 기준으로 정렬
    works.sort(key=lambda x: x[1])
    # 가장 빨리 끝나는 작업의 index를 현재 수행 작업으로
    current = 0
    # 작업 수행 횟수 1로 초기화
    cnt = 1
    # 작업 수 범위 내에서 반복
    while current < N:
        # 작업 변경 여부 초기화
        change = False
        # 현재 작업의 다음 작업들 중
        for i in range(current+1, N):
            # 시작 시각이 현재 작업의 끝나는 시각과 같거나 뒤인 가장 첫 작업을 선택
            # 끝나는 시간 기준으로 정렬했기 때문에 가장 첫 작업이 가장 빨리 끝남
            if works[i][0] >= works[current][1]:
                # 현재 작업, 작업 수행 횟수, 작업 변경 여부 갱신
                current = i
                cnt += 1
                change = True
                break
        # 더 이상 작업의 변경이 일어나지 않으면 break
        if not change:
            break
    print("#{} {}".format(tc, cnt))

