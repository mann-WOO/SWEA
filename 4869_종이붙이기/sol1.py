import sys
sys.stdin = open("input.txt")


def rectangles(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return (rectangles(n-1) * 2) + 1
    else:
        return (rectangles(n-1) * 2) - 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N/10

    print("#{} {}".format(tc, rectangles(n)))

