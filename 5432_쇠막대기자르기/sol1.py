import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 쇠자르기 계획 문자열 입력받기
    plan_picture = input()
    # 결과 값을 출력할 result
    result = 0
    # 계획 문자열의 첫번째 부터 마지막 두번째 문자까지 확인
    for i in range(len(plan_picture) - 1):
        # 레이저 발사 지점에서는 아무 것도 하지 않고 다음 문자 확인
        if plan_picture[i:i + 2] == '()':
            continue
        # 막대기 시작 지점이라면 확인 시작
        elif plan_picture[i:i + 2] == '((':
            # 막대기 왼쪽 끝의 수 오른쪽 끝의 수를 left_end와 right_end로 초기화
            # 처음의 왼쪽 끝은 확인했으므로 1
            left_end = 1
            right_end = 0
            # 막대기 시작 지점부터 계획 문자열 끝까지 확인
            for k in range(i+1, len(plan_picture)):
                # 막대기 혹은 레이저 발사 시작점이 나오면 left_end에 1 합산
                if plan_picture[k] == '(':
                    left_end += 1
                # 막대기 혹은 레이저 발사 끝점이라면 right_end에 1 합산
                else:
                    right_end += 1
                # 왼쪽, 오른쪽 끝점 수가 같을 때
                # 자른 횟수를 확인하고 result에 막대기 수 합산
                if left_end == right_end:
                    # 현재 막대기의 처음부터 끝까지 문자열을 pipe에 할당
                    pipe = plan_picture[i:k + 1]
                    # 막대기 길이에서 레이저 발사 지점 등장 횟수 cut
                    cut = 0
                    # 막대기에 레이저 발사 지점을 확인해 cut에 합산
                    for j in range(len(pipe)-1):
                        if pipe[j:j+2] == '()':
                           cut += 1
                    # 잘라진 막대기의 개수를 result에 합산
                    result += cut + 1
                    break

    print("#{} {}".format(tc, result))

