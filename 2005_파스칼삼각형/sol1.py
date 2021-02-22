import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 첫번째 줄, 첫 번째 스택은 완성되어 있음.
    stack = [1]
    # 완성된 한 줄을 담을 row
    row = []
    # 결과 row들을 담을 result
    result = [[1]]
    # 두 번째 줄부터 완성시켜 추가한다.
    for i in range(1, N):
        # 줄의 길이 설정: 2, 3, 4 ...
        row = [0] * (i + 1)
        # n번째 줄이라면, 그 위의 줄의 원소 개수인 n-1만큼 반복한다.
        for j in range(i):
            tmp = stack.pop()
            row[j] += tmp
            row[j + 1] += tmp
        # 완성된 줄을 결과에 추가
        result.append(list(row))
        # 스택을 이번에 완성시킨 줄로 갱신
        stack = list(row)

    print("#{} ".format(tc))
    for row in result:
        print(' '.join([str(num) for num in row]))

