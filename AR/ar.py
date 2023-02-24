from player import player
import random

totalnumber = 100000

run = 10
result = []
n = 0
for limit in range(1):
    for j in range(run):
        aWins = 0
        for i in range(totalnumber):
            a = player(0, None)
            b = player(0, a)
            a.setOp(b)
            while True:
                rolla = random.randint(1, 6)
                a.stratA(rolla)
                if a.score >= a.winScore:
                    aWins += 1
                    break
                rollb = random.randint(1, 6)
                b.stratRan(rollb)
                if b.score >= b.winScore:
                    break
        result.append(1.0*aWins/totalnumber)
    with open("stratA vs stratR.txt", "w") as f:
        f.write(str(result))
print("finish")