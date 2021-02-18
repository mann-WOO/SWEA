import sys
sys.stdin = open("input.txt")


# 회문을 찾아서 반환하는 함수 생성
def find_palindrome(N, M, words):
    # 정사각형 배열이므로 가로 세로 동시 진행
    for i in range(N):
        for j in range(N-M+1):
            # 가로 방향의 단어 row와 세로 방향의 단어 col 초기화
            row = ''
            col = ''
            # 역순 단어 row_reverse, col_reverse 초기화
            row_reverse = ''
            col_reverse = ''
            # 단어의 길이 M만큼 각 위치에서 row, col, row_reverse, col_reverse 생성
            for k in range(M):
                row += words[i][j+k]
                col += words[j+k][i]
                row_reverse = words[i][j+k] + row_reverse
                col_reverse =  words[j+k][i] + col_reverse
            # 회문이라면 해당 단어를 반환
            if row == row_reverse:
                return row
            if col == col_reverse:
                return col


T = int(input())
for tc in range(1, T+1):
    # 단어의 길이와 개수 N, 회문의 길이조건 M
    N, M = map(int, input().split())
    # 길이 N의 string를 N번 입력받아 words에 추가
    words = []
    for _ in range(N):
        words.append(input())

    print("#{} {}".format(tc, find_palindrome(N, M, words)))

