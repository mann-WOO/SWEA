import sys

sys.stdin = open("input.txt")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    infix = input()
    stack = []
    postfix = ''
    # 우선순위
    priority = {'(': 0,
                '+': 1,
                '*': 2}

    # 후위표기식으로 변환
    for i in range(N):
        # 숫자라면 후위표기식에 추가
        if '0' <= infix[i] <= '9':
            postfix += infix[i]
        else:
            # 열린 괄호라면 스택에 추가
            if infix[i] == '(':
                stack.append(infix[i])
            # 닫힌 괄호라면 스택에서 열린 괄호가 나올때까지 pop하며 후위표기식에 추가
            elif infix[i] == ')':
                while True:
                    tmp = stack.pop()
                    if tmp == '(':
                        break
                    else:
                        postfix += tmp
            # 덧셈 혹은 곱셈 기호라면 우선순위에 따라 처리
            else:
                while stack:
                    tmp = stack.pop()
                    if priority[tmp] > priority[infix[i]]:
                        postfix += tmp
                    else:
                        stack.append(tmp)
                        break
                stack.append(infix[i])
    # 스택에 남은 덧셈, 곱셈 기호를 모두 후위표기식에 추가
    while stack:
        postfix += stack.pop()

    # 후위표기식 계산
    for i in range(len(postfix)):
        if '0' <= postfix[i] <= '9':
            stack.append(int(postfix[i]))
        else:
            right = stack.pop()
            left = stack.pop()
            if postfix[i] == '+':
                stack.append(left+right)
            else:
                stack.append(left*right)
    result = stack.pop()

    print("#{} {}".format(tc, result))

