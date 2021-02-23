import sys
sys.stdin = open("input.txt")

T = int(input())
# 괄호 쌍의 딕셔너리 brackets 선언
brackets = {'(': ')',
            '{': '}'
            }


# 문자열을 인자로 받는 검사함수 check
def check(str_in):
    # 여는 괄호를 쌓을 stack
    stack = []
    # 모든 문자열에 대해 검사
    for i in range(len(str_in)):
        # 여는 괄호라면 stack에 추가
        if str_in[i] == '(' or str_in[i] == '{':
            stack.append(str_in[i])
        # 닫는 괄호일 때 검사
        if str_in[i] == ')' or str_in[i] == '}':
            # 스택이 비어있다면 0을 반환
            if not stack:
                return 0
            # 가장 최근 추가된 열린 괄호와 쌍이 맞지 않다면 0을 반환
            open_bracket = stack.pop()
            if brackets[open_bracket] != str_in[i]:
                return 0
    # 모든 문자열 검사 뒤 stack에 남은 열린 괄호가 있다면 0을 반환
    if stack:
        return 0
    # 검사를 통과하면 1을 반환
    return 1


for tc in range(1, T+1):
    str_in = input()
    print("#{} {}".format(tc, check(str_in)))

