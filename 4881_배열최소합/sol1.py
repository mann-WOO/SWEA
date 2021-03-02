# 풀리긴 하는데 너무 느리다

# dfs 함수
def dfs(n, k, arr):
    # 마지막 줄까지 확인하면 stack의 합을 sums에 추가
    if n == k:
        sums.append(sum(stack))
    else:
        # 각 줄에서 모든 원소 확인
        for j in range(k):
            # 해당 원소의 인덱스가 사용되지 않았다면
            if j not in idx_stack:
                # 스택에 해당 원소 추가, 사용한 인덱스에 해당 인덱스 추가
                stack.append(arr[n][j])
                idx_stack.append(j)
                # 재귀
                dfs(n+1, k, arr)
                # 재귀 후 새로운 탐색을 위해 사용한 원소 제거
                stack.pop()
                idx_stack.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 배열 입력받기
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    # 합들을 추가할 빈 배열 선언
    sums = []
    # 첫 번째 줄의 원소들을 시작으로 dfs
    for i in range(N):
        stack = [arr[0][i]]
        idx_stack = [i]
        dfs(1, N, arr)

    print("#{} {}".format(tc, min(sums)))