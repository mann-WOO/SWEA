import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 힙 생성
    heap = [0]
    # 하나씩 힙에 추가
    while nums:
        heap.append(nums.pop(0))
        current = len(heap)-1
        # 부모와 대소 비교해 자리 바꿔주기
        while current // 2 > 0:
            # 자리 바꾸면 바꾼 자리의 부모와 비교
            if heap[current//2] > heap[current]:
                heap[current//2], heap[current] = heap[current], heap[current//2]
                current = current//2
            # 자리가 바뀌지 않았다면 다음 원소를 추가
            else:
                break
    # 부모 노드들의 합 구하기
    last = len(heap)-1
    result = 0
    while last // 2 > 0:
        result += heap[last//2]
        last = last // 2
    print("#{} {}".format(tc, result))

