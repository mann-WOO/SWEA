import sys
sys.stdin = open("input.txt")

# 큐를 이용하기
T = 10
for tc in range(1, T+1):
    test_case = int(input())
    # 숫자 입력받기
    nums = list(map(int, input().split()))
    # while문을 컨트롤할 running
    running = True
    while running:
        # 1~5의 수 i에 대해 반복
        for i in range(1, 6):
            # deQueue한 원소에 i를 뺀 tmp
            tmp = nums.pop(0) - i
            # tmp가 0 이하가 되면 0을 nums에 추가하고 작업 끝
            if tmp <= 0:
                tmp = 0
                nums.append(tmp)
                running = False
                break
            # tmp가 1 이상이라면 nums에 추가
            else:
                nums.append(tmp)
    result = ' '.join(list(map(str, nums)))
    print("#{} {}".format(tc, result))

