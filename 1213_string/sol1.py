import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    test_case = int(input())
    # 찾고자 하는 문자열 target
    target = input()
    # 전체 문자열 words
    words = input()
    # target 등장 횟수를 기록할 cnt
    cnt = 0
    # 전체 문자열 길이에서 찾고자 하는 문자열의 길이를 빼고 1을 더한 것 만큼 반복
    for i in range(len(words) - len(target) + 1):
        # i번째 ~ (i + target 문자열 길이 - 1) 까지의 문자열이 target과 같다면 cnt에 1 합산
        if words[i : i+len(target)] == target:
            cnt += 1

    print("#{} {}".format(tc, cnt))

