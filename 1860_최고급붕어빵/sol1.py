import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N명의 사람들 오는 시간 입력
    ppl = list(map(int, input().split()))
    # 마지막 손님이 오는 시간 last
    last = max(ppl)
    # 시간에 따라 오는 사람의 수를 리스트로 작성
    ppl_list = [0] * (last+1)
    for i in range(N):
        ppl_list[ppl[i]] += 1
    # 시간, 붕어빵 수, 결과변수 초기화
    time = 0
    food = 0
    result = 'Possible'
    # 0에 찾아오는 손님이 있다면 불가능
    if ppl_list[0] != 0:
        result = 'Impossible'
    # 0에 찾아오는 손님이 없다면
    else:
        # 1 ~ 마지막 손님이 오는 시간까지 반복
        for i in range(1, last+1):
            # 시간에 1 합산
            time += 1
            # 붕어빵이 만들어지는 시간에는 food에 K 합산
            if time % M == 0:
                food += K
            # 해당 시간의 손님 수만큼 food 차감
            food -= ppl_list[i]
            # food가 음수가 되면 불가능
            if food < 0:
                result = 'Impossible'
                break

    print("#{} {}".format(tc, result))

