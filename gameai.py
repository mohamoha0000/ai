# دالة sigmoid

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# مشتقة دالة sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

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
print(predict(w,[1,1]))