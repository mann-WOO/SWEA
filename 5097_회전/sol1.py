import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 숫자 리스트 입력받기
    nums = list(map(int, input().split()))
    # M번 앞에서 빼서 뒤에 추가하기
    for i in range(M):
        nums.append(nums.pop(0))

    print("#{} {}".format(tc, nums.pop(0)))
