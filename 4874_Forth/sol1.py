import sys
sys.stdin = open("input.txt")

T = int(input())
operator = ['+', '-', '*', '/']

for tc in range(1, T+1):
    forth = input().split()
    stack = []
    result = 'error'
    # forth의 원소들에 대해
    for i in range(len(forth)):
        # 1. 원소가 연산자일때
        if forth[i] in operator:
            # stack에 2개 이상의 숫자가 쌓여있을 때 연산 실행
            if len(stack) >= 2:
                right = stack.pop()
                left = stack.pop()
                if forth[i] == '+':
                    stack.append(left+right)
                elif forth[i] == '-':
                    stack.append(left-right)
                elif forth[i] == '*':
                    stack.append(left*right)
                else:
                    stack.append(left/right)
            # stack에 숫자가 2개보다 적을 때 오류
            else:
                break
        # 2. 원소가 최종점일때
        elif forth[i] == '.':
            # 스택에 원소가 하나만 남았다면 결과값 설정
            if len(stack) == 1:
                result = int(stack.pop())
                break
            else:
                break
        # 3. 그 외의 경우(숫자) 스택에 추가해줌.
        else:
            stack.append(int(forth[i]))

    print("#{} {}".format(tc, result))
