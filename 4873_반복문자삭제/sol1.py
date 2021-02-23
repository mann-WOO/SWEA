import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 문자열을 리스트로 입력받기
    word = list(input())
    # 반복 문자를 제외하고 넣을 stack
    stack = []
    # 문자열의 각 문자에 대해 반복
    for i in range(len(word)):
        # stack에 문자가 있다면
        if len(stack) >= 1:
            # 마지막 문자를 꺼내 last에 할당
            last = stack.pop()
            # last와 현재 문자가 같지 않을 때만 둘 다 stack에 추가
            if last != word[i]:
                stack.append(last)
                stack.append(word[i])
        # stack에 문자가 없다면 현재 문자를 추가
        else:
            stack.append(word[i])

    print("#{} {}".format(tc, len(stack)))

