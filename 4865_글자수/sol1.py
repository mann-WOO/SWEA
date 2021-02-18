import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # str1, str2를 입력받기
    str1 = input()
    str2 = input()

    # 가장 많은 글자의 개수를 할당할 max_cnt 초기화
    max_cnt = 0
    # str1의 모든 글자들을 확인
    for char1 in str1:
        cnt = 0
        # str1의 글자가 str2에 있는 만큼 cnt에 합산
        for char2 in str2:
            if char2 == char1:
                cnt += 1
        # 현재 글자의 cnt를 max_cnt와 비교해 갱신
        if cnt >= max_cnt:
            max_cnt = cnt
    
    print("#{} {}".format(tc, max_cnt))

