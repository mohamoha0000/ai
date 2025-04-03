# دالة sigmoid

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# مشتقة دالة sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)
"""
# البيانات
X = [[1, 0], [1, 1], [0, 0], [0, 1]]
y = [[0, 1],[0, 0],[0, 0],[1, 0]]  # القيم الفعلية
# أوزان عشوائية مبدئية وإزاحة

w=[[0.1, 0.1, 0.1],[0.1, 0.1, 0.1]]
# معدل التعلم
learning_rate = 0.01

# عدد التكرارات
epochs = 10000

# التدريب
for epoch in range(epochs):
    for i in range(len(X)):
        for nn in range(len(w)):
            # المعادلة الخطية
            z = w[nn][0] * X[i][0] + w[nn][1] * X[i][1] + w[nn][2]
            # تفعيل النتيجة
            y_pred = sigmoid(z)
            # حساب الخطأ
            error = y[i][nn] - y_pred
            # تحديث الأوزان
            w[nn][0] += learning_rate * error * X[i][0] * sigmoid_derivative(y_pred)
            w[nn][1] += learning_rate * error * X[i][1] * sigmoid_derivative(y_pred)
            w[nn][2] += learning_rate * error * sigmoid_derivative(y_pred)

def predict(w,input):
    pedict=[]
    for x in range(len(w)):
        z = w[x][0] * input[0] + w[x][1] *input[1] + w[x][2]
        y_pred = sigmoid(z)
        pedict.append(y_pred)
    return pedict
print(w)
print(predict(w,[1,1]))"
"""

import random
import copy
import time
import pickle
class player:
    def __init__(self,hidden_layer,input):
        self.hidden_layer=hidden_layer
        self.output=hidden_layer[-1]
        self.input=input
        self.input_value=[]
        self.w=[[]]
        self.game=[0,0,0,
                   0,0,0,
                   0,0,0]
        for i in range(hidden_layer[0]):
            self.w[0].append([random.uniform(0, 1) for x in range(input)]+[1])
        for x in range(1,len(hidden_layer)):
            self.w.append([])
            for i in range(hidden_layer[x]):
                self.w[x].append([random.uniform(0, 1) for x in range(hidden_layer[x-1])]+[1])
    def predict(self,input_value):
        last_layer=[[]]
        for x in self.w[0]:
            last_layer[0].append(sigmoid(sum(input_value[e]*x[e] for e in range(len(input_value)))+x[-1]))
        for i in range(1,len(self.w)):
            last_layer.append([])
            for x in self.w[i]:
                last_layer[i].append(sigmoid(sum(last_layer[i-1][e]*x[e] for e in range(len(last_layer[i-1])))+x[-1]))
        return last_layer[-1]
    def update(self):
        for x in range(len(self.w)):
            for i in range(len(self.w[x])):
                for e in range(len(self.w[x][i])):
                    self.w[x][i][e]+=random.uniform(-1, 1)
    def get_model(self):
        return self.w
    def save(self):
        with open("data.pkl", "wb") as file:
            pickle.dump(self.w, file)
    def load(self,path):
        with open(path, "rb") as file:
            self.w= pickle.load(file)
    
models=[]
bestmodel=[[],[],[],[],[],[],[],[],[]]
bestscore=0
hidden_layer=[10,10,9]
for i in range(100):
    models.append(player(hidden_layer,9))


def startgame(x):
    m=0
    score=0
    for e in range(9):
        pred=x.predict(x.game)
        valid_values = [value for value in pred if 0.5 < value < 1]
        if len(valid_values) == 1:
            x.game[pred.index(valid_values[0])]=1
    score=x.game.count(1)
    chayta=len(valid_values)
    return score,chayta

for ep in range(10000):
    m=0
    eq=9999
    eq_=9999
    for x in models:
        pred=x.predict(x.game)
        m=0
        score=0
        chayta=0
        for e in range(len(pred)):
            if pred[e]>0.5 and pred[e]<1 and x.game[e]==0:
                m+=1
        if m==1:
            score,chayta=startgame(x)
            
        if m<eq and m>0 and score == 0:
            eq=m
            bestmodel[m-1].append(x)
        elif score>bestscore:
            bestmodel[m-1].append(x)
            bestscore=score
        elif score==bestscore and chayta<eq_:
            eq_=chayta
            bestmodel[0].append(x)


    if ep%50==0:
        print("epouche n:",ep)
        print("best score is :",bestscore)
    if ep==10000 or bestscore==9:
        break
    models=[]
    for e in reversed(bestmodel):
        if len(e)>0:
            new_model_m = copy.deepcopy(e[-1])
    #new_model_m.game=[0,0,0,0,0,0,0,0,0]
    for x in range(100):
        new_model=copy.deepcopy(new_model_m)
        new_model.update()
        models.append(new_model)
bestmodel=[]

bestmodel.append(new_model_m)
lis=[0,0,0,
    0,0,0,
    0,0,0]
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
print("best score is :",bestscore)

bestmodel[-1].save()

while True:


    print_board(lis)
    a=int(input("entre number:"))
    lis[a-1]=1
    print_board(lis)
    print("ai think ...")
    time.sleep(5)
    pred=bestmodel[-1].predict(lis)
    valid_values = [value for value in pred if 0.5 < value < 1]
    if len(valid_values) == 1:
        lis[pred.index(valid_values[0])]=1


"""
for x in range(9):
    print_board(lis)
    print("ai think ...")
    time.sleep(5)
    pred=bestmodel[-1].predict(lis)
    valid_values = [value for value in pred if 0.5 < value < 1]
    if len(valid_values) == 1:
        lis[pred.index(valid_values[0])]=1
"""