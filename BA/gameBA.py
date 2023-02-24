from player import player
import random

totalnumber = 100000

run = 10
result = []
n = 0
limit = 13
for j in range(run):
    aWins = 0
    for i in range(totalnumber):
        a = player(0, None)
        b = player(0, a)
        a.setOp(b)
        while True:
            rolla = random.randint(1, 6)
            a.stratB(rolla, limit)
            if a.score >= a.winScore:
                aWins += 1
                break
            rollb = random.randint(1, 6)
            b.stratA(rollb)
            if b.score >= b.winScore:
                break
    result.append(1.0*aWins/totalnumber)
with open("stratA vs stratB" + str(limit) + ".txt", "w") as f:
    f.write(str(result))
print("finish")