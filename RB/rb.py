from player import player
import random

totalnumber = 100000

run = 10

n = 0
for bnum in range(14, 20):
    result = []
    for j in range(run):
        limitb = bnum
        aWins = 0
        for i in range(totalnumber):
            a = player(0, None)
            b = player(0, a)
            a.setOp(b)
            while True:
                rolla = random.randint(1, 6)
                a.stratRan(rolla)
                if a.score >= a.winScore:
                    aWins += 1
                    break
                rollb = random.randint(1, 6)
                b.stratB(rollb, limitb)
                if b.score >= b.winScore:
                    break
        result.append(1.0*aWins/totalnumber)
    with open("stratRan " + " vs stratB"+ str(limitb) +".txt" , "w") as f:
            f.write(str(result))
print("finish")