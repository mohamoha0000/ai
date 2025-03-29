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
class player:
    def __init__(self,hidden_layer,input):
        self.hidden_layer=hidden_layer
        self.output=hidden_layer[-1]
        self.input=input
        self.input_value=[]
        self.w=[[]]
        for i in range(hidden_layer[0]):
            self.w[0].append([random.uniform(0, 1) for x in range(input)]+[1])
        for x in range(1,len(hidden_layer)):
            self.w.append([])
            for i in range(hidden_layer[x]):
                self.w[x].append([random.uniform(0, 1) for x in range(hidden_layer[x-1])]+[1])
    def predict(self,input_value):
        last_layer=[[]]
        for x in self.w[0]:
            last_layer[0].append(sum(input_value[e]*x[e] for e in range(len(input_value)))+x[-1])
        for i in range(1,len(self.w)):
            last_layer.append([])
            for x in self.w[i]:
                last_layer[i].append(sum(last_layer[i-1][e]*x[e] for e in range(len(last_layer[i-1])))+x[-1])
        return last_layer[-1]
    def update():
        pass
    def get_model(self):
        return self.w
    

hidden_layer=[5,2]
moha1=player(hidden_layer,3)
#print(moha1.get_model())
print(moha1.predict([5,56,6]))

