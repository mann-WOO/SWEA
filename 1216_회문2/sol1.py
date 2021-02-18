import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    test_case = input()
    # 100 x 100의 텍스트를 입력받는다
    texts = []
    for _ in range(100):
        texts.append(input())
    # 가장 긴 회문의 길이를 기록할 longest
    longest = 1

    # 마지막 열과 행을 제외한 모든 점에 대해
    for i in range(99):
        for j in range(99):
            # 가로행 회문의 길이, 세로행 회문의 길이 row/col_pal_len
            row_pal_len = 1
            col_pal_len = 1
            # 가로행 문자열  row, 세로행 문자열 col
            row = texts[i][j]
            col = texts[j][i]
            # texts[i][j]를 시작점으로 하는 모든 가로 길이 문자를 점검
            for k in range(1, 100 - j):
                row = row + texts[i][j+k]
                # 회문이라면 가로행 회문 길이를 갱신
                if row == row[::-1]:
                    row_pal_len = len(row)
            # 모든 세로 길이 문자를 점검
            for k in range(1, 100 - j):
                col = col + texts[j+k][i]
                # 회문이라면 세로행 회문 길이를 갱신
                if col == col[::-1]:
                    col_pal_len = len(col)
            # 가로, 세로행의 회문 길이를 가장 긴 회문 길이와 비교해 갱신
            if row_pal_len > longest:
                longest = row_pal_len
            if col_pal_len > longest:
                longest = col_pal_len
    
    print("#{} {}".format(tc, longest))

