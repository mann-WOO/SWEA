import sys
sys.stdin = open("input.txt")

T = int(input())


secret = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}


for tc in range(1, T+1):
    # 세로 N, 가로 M
    N, M = map(int, input().split())
    # 배열 입력받기
    lines = []
    for i in range(N):
        lines.append(input())
    # 배열 확인해서 코드 찾으면 break
    for i in range(N):
        if int(lines[i]) != 0:
            # k: 1로 끝나는 끝점
            k = 0
            for j in range(M):
                if lines[i][j] == '1':
                    k = j
            code = lines[i][k-55:k+1]
            break
    # 암호코드의 수 여덟개를 담을 리스트 numbers
    numbers = []
    # 암호코드 7자리씩 잘라 숫자그림과 비교 후 리스트에 추가
    for i in range(8):
        number = code[7*i:7*(i+1)]
        numbers.append(secret.get(number))
    # 검증코드 규칙에 맞을 때 결과 값은 숫자들의 함
    if (sum(numbers[::2])*3 + sum(numbers[1::2])) % 10 == 0:
        result = sum(numbers)
    # 검증코드 규칙에 맞지 않을 때 결과 값은 0
    else:
        result = 0
    print("#{} {}".format(tc, result))

