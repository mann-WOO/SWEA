import sys
sys.stdin = open("input.txt")


# 병합 함수
def merge(left, right):
    global count
    # 결과로 반환할 리스트
    merged_list = []
    # 현재 확인중인 원소를 표시한 _point
    left_point = 0
    left_len = len(left)
    right_point = 0
    right_len = len(right)
    # 왼쪽, 오른쪽에서 받은 리스트 둘 모두에 남은 원소가 있을 때
    while left_point != left_len and right_point != right_len:
        # 왼쪽에 첫 번째 원소가 오른쪽 첫 번째 원소보다 작거나 같을때
        if left[left_point] <= right[right_point]:
            # 결과 리스트에 추가, left_point를 한 칸 이동
            merged_list.append(left[left_point])
            left_point += 1
        # 오른쪽 첫 번째 원소가 더 작을 때
        else:
            # 결과 리스트에 추가, right_point를 한 칸 이동
            merged_list.append(right[right_point])
            right_point += 1
    # 왼쪽 리스트가 남아있을 때(오른쪽을 먼저 다 추가했을 때)
    if right_point == right_len:
        # 남은 원소를 모두 추가
        merged_list.extend(left[left_point:])
        # 문제 조건(왼쪽 원소의 마지막이 더 클 때) count에 1 합산
        count += 1
        # 결과 리스트를 반환
        return merged_list
    # 오른쪽 리스트가 남아있을 때
    else:
        # 남은 원소를 모두 추가
        merged_list.extend(right[right_point:])
        # 결과 리스트를 반환
        return merged_list


# 병합정렬 함수
def merge_sort(nums):
    # 원소의 수가 1개 이하라면 해당 리스트를 반환
    if len(nums) <= 1:
        return nums
    # 중간점 설정
    mid = len(nums) // 2
    # 왼쪽 리스트를 정렬
    left = merge_sort(nums[0:mid])
    # 오른쪽 리스트를 정렬
    right = merge_sort(nums[mid:len(nums)])
    # 병합한 리스트를 반환
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    # 인풋 받기
    N = int(input())
    nums = list(map(int, input().split()))
    # 왼쪽 마지막 원소가 오른쪽 마지막보다 큰 경우
    count = 0
    # 입력받은 리스트를 정렬
    result = merge_sort(nums)
    print("#{} {} {}".format(tc, result[N//2], count))

