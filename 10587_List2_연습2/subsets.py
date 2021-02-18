def subsets(arr):
    # 부분집합들의 리스트 result
    result = []
    for i in range(1 << len(arr)):
        # 부분집합을 담을 임시변수 tmp
        tmp = []
        for j in range(len(arr)):
            if i & (1 << j):
                tmp.append(arr[j])
        result.append(tmp)
    return result

print(subsets([1, 2, 3, 4, 5]))