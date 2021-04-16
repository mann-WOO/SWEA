import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    # 거스름돈 target
    target = int(input())
    # 지폐 종류
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 지폐 개수 기록 문자열 result
    result = ''
    # 몫과 나머지로 계산하여 지폐 개수 기록
    for i in range(len(money)):
        result += ' ' + str(target//money[i])
        target = target % money[i]
    print("#{}\n{}".format(tc, result.strip()))

