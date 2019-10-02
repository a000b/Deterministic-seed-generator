lineList = [line.rstrip('\n') for line in open('bip39_en_words.txt')]
p = 31 #słowo startowe
s = 78 #skok
for i in range(24):
    try:
        print(i + 1, p, lineList[p - 1])
        p += s
    except IndexError:
        print("poza zakresem, dostosuj parametry")
        break 


