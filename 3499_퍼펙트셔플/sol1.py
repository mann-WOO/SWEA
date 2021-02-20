import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    if N % 2 == 0:
        first_half = cards[:N//2]
        second_half = cards[N//2:]
    else:
        first_half = cards[:N//2 + 1]
        second_half = cards[N//2 + 1:]
    result = []
    for i in range(N//2):
        result.append(first_half[i])
        result.append(second_half[i])
    if N % 2:
        result.append(first_half.pop())
    
    print("#{} {}".format(tc, ' '.join(result)))

