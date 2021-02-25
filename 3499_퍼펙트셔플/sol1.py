import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 카드의 수 N
    N = int(input())
    cards = input().split()
    # 카드를 반으로 나눔, 홀수 짝수 경우 나누어
    if N % 2 == 0:
        first_half = cards[:N//2]
        second_half = cards[N//2:]
    else:
        first_half = cards[:N//2 + 1]
        second_half = cards[N//2 + 1:]
    # 결과 리스트 result
    result = []
    # 카드를 교대로 result에 추가
    for i in range(N//2):
        result.append(first_half[i])
        result.append(second_half[i])
    # 카드가 홀수개 일때는 남은 하나를 result에 추가
    if N % 2:
        result.append(first_half.pop())
    
    print("#{} {}".format(tc, ' '.join(result)))

