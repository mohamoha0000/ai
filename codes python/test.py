class m:
    def __init__(self, x, y):
        self.x = x
        self.y = y
moha=m(5,6)
lis=[]
lis.append(moha)
moha.x=99
print(lis[0].x)
