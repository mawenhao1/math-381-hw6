from player import player
import numpy as np
import random

totalnumber = 10000

run = 1000
result = []

n = 0
for j in range(run):
    
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
            b.stratA(rollb)
            if b.score >= b.winScore:
                break
            
            
    result.append(1.0*aWins/totalnumber)
with open("stratRan vs stratA.txt", "w") as f:
    f.write(str(result))
print("finish")