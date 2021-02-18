# 부분집합을 만드는 또다른 방법
# 빈 리스트를 원소로 가지는 리스트에서 시작
subsets = [[], ]
# 1부터 원하는 수까지 반복
N = 12
for i in range(1, N+1):
    # 매 반복마다 그 순간 부분집합들의 수만큼 반복
    for k in range(len(subsets)):
        # 현재의 부분집합들에 새로운 수를 추가한 부분집합을 새로운 원소로 추가
        subsets.append(subsets[k] + [i])

print(subsets)