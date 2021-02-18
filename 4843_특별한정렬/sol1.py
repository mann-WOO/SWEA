import sys
sys.stdin = open("input1.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(N-1):
        # 현재 인덱스의 값, 인덱스를 임시변수로 설정
        tmp_value = numbers[i]
        tmp_idx = i
        # 짝수인덱스: 현재 인덱스부터 마지막까지 중 최대를 찾아 바꾸기
        if i % 2 == 0:
            for k in range(i+1, N):
                if numbers[k] > tmp_value:
                    tmp_value = numbers[k]
                    tmp_idx = k
        # 홀수인덱스: 현재 인덱스부터 마지막까지 중 최소를 찾아 바꾸기
        if i % 2 == 1:
            for k in range(i+1, N):
                if numbers[k] < tmp_value:
                    tmp_value = numbers[k]
                    tmp_idx = k
        # 교환작업
        if tmp_idx != i:
            numbers[i], numbers[tmp_idx] = numbers[tmp_idx], numbers[i]

    # 10개만 결과 문자열로 만들기
    result = ' '.join(map(str, numbers[:10]))
    
    print("#{} {}".format(tc, result))

