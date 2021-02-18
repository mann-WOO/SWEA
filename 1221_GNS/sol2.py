import sys

sys.stdin = open("input.txt")

T = int(input())
# 문자열로 된 숫자 리스트 planet
planet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T + 1):
    # 입력받는 숫자의 수 N
    N = int(input().split()[1])
    # 입력받은 숫자문자열을 리스트로 만든 nums
    nums = input().split()
    # 결과 문자열 result
    result = ''
    # 0부터 10 개의 숫자에 대해 반복
    for i in range(10):
        # 각 숫자가 등장할 때마다 결과 문자열에 해당 숫자의 문자열을 추가
        for j in range(N):
            if planet[i] == nums[j]:
                result += planet[i] + ' '

    result = result.strip()

    print("#{}\n{}".format(tc, result))