import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T+1):
    # 목표 패턴 단어 target 입력받기
    target = input()
    # 전체 문자열 word 입력받기
    word = input()
    # 결과를 할당할 변수 result
    result = 0
    # words의 부분 문자열을 한 칸씩 밀면서 target과 비교
    for i in range(len(word)-len(target)+1):
        if word[i:i+len(target)] == target:
            # target과 일치하는 부분 문자열이 나온다면 result에 1을 할당하고 종료
            result = 1
            break
    print("#{} {}".format(tc, result))

