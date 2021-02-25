import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = []
    for _ in range(N):
        students.append(list(map(int, input().split())))
    # 복도 배열 corridor
    corridor = [0] * 200
    # 학생 한명씩 확인
    for student in students:
        # 출발지점 복도 start, 도착지점 복도 end
        start = (student[0]-1) // 2
        end = (student[1]-1) // 2
        # 시작 지점을 항상 작은 값으로
        if start > end:
            start, end = end, start
        # 복도 이용 횟수를 더해줌
        for i in range(start, end+1):
            corridor[i] += 1
    # 가장 많이 이용된 복도 지점의 값을 결과로 출력
    max_cnt = corridor[0]
    for cnt in corridor:
        if cnt > max_cnt:
            max_cnt = cnt

    print("#{} {}".format(tc, max_cnt))

