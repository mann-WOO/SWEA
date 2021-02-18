import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 입력 문자열 plan
    plan = input()
    # 괄호가 열린 지점을 담을 리스트 start_points 초기화
    start_points = []
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
            # cut 지점이 아니라면 몇 번 잘렸는지 확인
            else:
                # 파이프의 수 1로 초기화
                num_pipes = 1
                # 현재 파이프의 끝점과 가장 가까운 cut부터 확인
                for k in range(len(cuts)-1, -1, -1):
                    # cut이 satrt보다 뒤에 나왔다면 num_pipes에 1 합산
                    if cuts[k] > start:
                        num_pipes += 1
                    # cut이 start보다 작아지면 break
                    else:
                        break
                # result에 num_pipes 합산
                result += num_pipes

    print("#{} {}".format(tc, result))