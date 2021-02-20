import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    cards = input()
    cards_list = []
    result = ''
    SDHC =[1] * 52  # 0~12 13~25 26~38 39~51
    for i in range(int(len(cards)/3)):
        cards_list.append(cards[i*3:(i+1)*3])

    for card in cards_list:
        if card[0] == 'S':
            SDHC[int(card[1:]) - 1] -= 1
        elif card[0] == 'D':
            SDHC[13 + int(card[1:]) - 1] -= 1
        elif card[0] == 'H':
            SDHC[26 + int(card[1:]) - 1] -= 1
        else:
            SDHC[39 + int(card[1:]) - 1] -= 1

    if -1 in SDHC:
        result = 'ERROR'
    else:
        result += str(sum(SDHC[0:13])) + ' '
        result += str(sum(SDHC[13:26])) + ' '
        result += str(sum(SDHC[26:39])) + ' '
        result += str(sum(SDHC[39:]))

    print("#{} {}".format(tc, result))

