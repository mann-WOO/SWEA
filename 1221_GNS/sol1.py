import sys
sys.stdin = open("input.txt")


T = int(input())
# 문자열로 된 숫자 리스트 planet
planet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T+1):
    # 각 숫자가 몇번 나왔는지 셀 count
    count = [0] * 10
    # 입력받는 숫자의 수 N
    N = int(input().split()[1])
    # 입력받은 숫자문자열을 리스트로 만든 nums
    nums = input().split()
    # 10 개의 숫자에 대해 반복
    for i in range(10):
        # 각 숫자가 nums에 몇번 등장하는지 count에 합산
        for j in range(N):
            if planet[i] == nums[j]:
                count[i] += 1

    # 결과문자열 result
    result = ''
    # count에 기록되어 있는 만큼씩 문자열에 추가
    for i in range(10):
        for _ in range(count[i]):
            result += planet[i] + ' '
    result = result.strip()
    
    print("#{}\n{}".format(tc, result))

