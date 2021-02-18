import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 두 문자열 A, B 입력받기
    A, B = input().split()
    # A 를 검토하기 위한 A에서의 위치 current
    current = 0
    # A에서 B의 등장 횟수 count
    count = 0
    # A를 처음부터 훑어가며 확인
    while current < len(A) - len(B) + 1:
        # current에서 시작하는 부분 문자열이 B와 같다면
        if A[current:current+len(B)] == B:
            # count에 1합산, current를 부분 문자열의 끝점 뒤로 이동
            count += 1
            current += len(B)
        # 다른 경우는 current에 1 합산
        else:
            current += 1
    # 타이핑 횟수 계산
    result = len(A) - count*(len(B)-1)

    print("#{} {}".format(tc, result))

