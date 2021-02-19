import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    words = []
    # 가로 단어들 입력받기
    for _ in range(5):
        words.append(input())
    # 결과 문자열 result
    result = ''

    # 한 단어의 최대 길이 15만큼 반복
    for i in range(15):
        # 입력받은 다섯 줄의 단어에 대해 반복
        for j in range(5):
            # 단어에 현재 확인중인 세로열의 문자가 존재할 때 결과에 추가
            if len(words[j]) >= i + 1:
                result += words[j][i]
    
    print("#{} {}".format(tc, result))

