import sys
sys.stdin = open("input.txt")


def calculate(node):
    if node > 0:
        # 왼쪽 자식 서브트리의 계산 결과
        left = calculate(left_child[node])
        # 오른쪽 자식 서브트리의 계산 결과
        right = calculate(right_child[node])
        # 리프노드(숫자)라면 그대로 숫자를 리턴
        if values[node].isdigit():
            return int(values[node])
        # 리프노드가 아니라면 연산자에 따라 계산하여 리턴
        else:
            if values[node] == '+':
                return left + right
            elif values[node] == '-':
                return left - right
            elif values[node] == '*':
                return left * right
            else:
                return left / right


T = 10
for tc in range(1, T+1):
    N = int(input())
    # 트리 노드의 관계 리스트
    left_child = [0] * (N+1)
    right_child = [0] * (N+1)
    # 노드의 값 리스트
    values = [0] * (N+1)

    for _ in range(N):
        info = input().split()
        if len(info) == 2:
            values[int(info[0])] = info[1]
        else:
            values[int(info[0])] = info[1]
            left_child[int(info[0])] = int(info[2])
            right_child[int(info[0])] = int(info[3])

    result = calculate(1)

    print("#{} {}".format(tc, int(result)))

