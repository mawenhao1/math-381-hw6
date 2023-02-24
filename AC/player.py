import random
class player:
    winScore = 20
    
    def __init__(self, myScore, opponent):
        self.score = myScore
        self.opponent = opponent
        

    
    def setOp(self, opponent):
        self.opponent = opponent
        
    def add(self, number):
        self.score += number
        
    def sub(self, number):
        self.score -= number
        if (self.score < 0):
            self.score = 0
        
    def stratA(self, roll):
        self.score += roll
            
    def stratB(self, roll, limit):
        if self.score + roll >= self.winScore:
            self.score += roll
        elif self.opponent.score >= limit:
            self.opponent.sub(roll)
        else:
            self.score += roll
    
    def stratC(self, roll, limit):
        if self.score + roll >= self.winScore:
            self.score += roll
        elif self.opponent.score - self.score >= limit:
            self.opponent.sub(roll)
        else:
            self.score += roll
            
    def stratRan(self, roll):
        num = random.random()
        if self.score + roll >= self.winScore:
            self.score += roll
        elif num < 0.5:
            self.opponent.sub(roll)
        else:
            self.score += roll