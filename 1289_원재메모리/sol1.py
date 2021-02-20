import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 원래 메모리를 입력
    memory = input()
    # 메모리를 검토하며 연속된 0, 1의 변화를 기록할 current를 기본값 0으로 초기화
    current = '0'
    # 0,1의 변화 횟수 cnt
    cnt = 0
    # 메모리의 비트 하나씩 확인
    for i in range(len(memory)):
        # 기본값 0에서 다른 값이 나올때마다 그 값으로 초기화, cnt에 1 합산
        # current는 0과 1의 값을 번갈아 가짐
        if memory[i] != current:
            current = memory[i]
            cnt += 1

    print("#{} {}".format(tc, cnt))

