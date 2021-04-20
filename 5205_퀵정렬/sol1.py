import sys
sys.stdin = open("input.txt")

 
# 피벗 위치가 바뀔 때까지 정렬하고, 피벗 인덱스를 반환하는 함수
def get_pivot(nums, start, end):
    # 첫 번째 원소를 피벗으로 설정
    pivot = nums[start]
    left = start + 1
    right = end

    # left, right가 교차하지 않는 동안 반복
    while left <= right:
        # left를 피벗 값과 비교하면서 한 칸씩 오른쪽으로
        while left <= N-1 and nums[left] <= pivot:
            left += 1
        # right를 피벗 값과 비교하면서 한 칸씩 왼쪽으로
        while right >= 0 and nums[right] > pivot:
            right -= 1
        # 교차하지 않았다면 left, right를 교환
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    # 교차했을 때 피벗과 right를 교환
    nums[start], nums[right] = nums[right], nums[start]

    # right를 피벗 위치로 반환
    return right


# 퀵 정렬 함수
def quick_sort(nums, start, end):
    if start < end:
        # 피벗 위치를 구하고
        pivot = get_pivot(nums, start, end)
        # 왼쪽, 오른쪽을 나누어 퀵정렬 실행
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, N-1)
    print("#{} {}".format(tc, nums[N//2]))

