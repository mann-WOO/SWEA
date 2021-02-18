import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 입력 문자열 plan
    plan = input()
    # 괄호가 열린 지점을 담을 리스트 start_points 초기화
    start_points = []
    # 파이프 쌍을 담을 pipes 초기화
    pipes = []
    # 자르는 지점을 담을 cuts 초기화
    cuts = []
    # 최종 파이프 수의 합 result 초기화
    result = 0
    # plan의 모든 문자열에 대해
    for i in range(len(plan)):
        # 여는 괄호라면 그 인덱스를 start_points에 추가
        if plan[i] == '(':
            start_points.append(i)
        # 닫는 괄호일 경우
        elif plan[i] == ')':
            # 가장 마지막으로 추가된 여는 괄호의 인덱스를 start로 선언
            start = start_points.pop()
            # 현재의 닫는괄호 위치를 end로 선언
            end = i
            # start, end가 연달아 나왔다면 start만 자르는 지점 cut에 추가
            if end == start + 1:
                cuts.append(start)
            # cut 지점이 아니라면 시작, 끝 쌍 튜플을 pipes에 추가
            else:
                pipes.append((start, end))

    # 모든 파이프들을 확인
    for start, end in pipes:
        # 현재 파이프의 개수
        num_pipes = 1
        # 파이프 사이에 cut 지점이 있다면 파이프 개수에 1 합산
        for cut in cuts:
            if start < cut < end:
                num_pipes += 1
        # 파이프 개수를 result에 합산
        result += num_pipes

    print("#{} {}".format(tc, result))

