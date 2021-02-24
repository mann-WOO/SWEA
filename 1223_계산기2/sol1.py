import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()
    stack = []
    postfix = ''
    priority = {'+': 1,
                '*': 2}

    # 후위표기식으로 변환
    for i in range(N):
        if '0' <= infix[i] <= '9':
            postfix += infix[i]
        else:
            if stack:
                while stack:
                    prev = stack.pop()
                    if priority[prev] > priority[infix[i]]:
                        postfix += prev
                    else:
                        stack.append(prev)
                        break
                stack.append(infix[i])
            else:
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()

    # 후위표기식 계산
    for i in range(N):
        if '0' <= postfix[i] <= '9':
            stack.append(postfix[i])
        elif postfix[i] == '+':
            stack.append(str(int(stack.pop()) + int(stack.pop())))
        else:
            stack.append(str(int(stack.pop()) * int(stack.pop())))
    result = stack.pop()
    
    print("#{} {}".format(tc, result))

