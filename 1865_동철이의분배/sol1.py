import sys
sys.stdin = open("input.txt")


# 가장 큰 확률을 구하는 함수
def get_maximum_prob(k, prob):
    global max_prob
    # 현재까지의 확률이 최대 확률보다 작을 때 백트래킹
    if prob <= max_prob:
        return
    # 모든 일을 정해줬을 때 최대 확률을 갱신
    elif k == N:
        max_prob = prob
    # 진행
    else:
        # 배정되지 않은 일 중 하나를 배정하고, 다음 사람으로 넘어감
        for i in range(N):
            if not done[i]:
                done[i] = 1
                get_maximum_prob(k+1, prob*works[k][i]/100)
                # 배정 취소하고 다음 일로 넘어간다.
                done[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    works = []
    for _ in range(N):
        works.append(list(map(int, input().split())))
    # 일의 배정 여부를 기록하는 done 리스트
    done = [0 for x in range(N)]
    # 최대 확률 초기화
    max_prob = 0
    # 초기 확률 초기화
    prob = 100
    get_maximum_prob(0, prob)
    result = format(max_prob, ".6f")
    print("#{} {}".format(tc, result))

