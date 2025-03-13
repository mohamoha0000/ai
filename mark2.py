#import math

# تحضير البيانات
X = [1,2,3,4,5,6,7]
y = [1, 1, 1, 0, 0, 0,0]

# حساب المتوسطات
mean_x1 = sum(x for x in X) / len(X)
mean_y = sum(y) / len(y)

# حساب التباينات والتغايرات
def variance(values, mean):
    return sum((x - mean) ** 2 for x in values)

def covariance(values1, values2, mean1, mean2):
    return sum((x1 - mean1) * (x2 - mean2) for x1, x2 in zip(values1, values2))

var_x1 = variance([x for x in X], mean_x1)
cov_x1_y = covariance([x for x in X], y, mean_x1, mean_y)

# حساب المعاملات
b1 = cov_x1_y / var_x1
b0 = mean_y - b1 * mean_x1 
print(b1)
print(b0)
# تنبؤ القيم
x_new = 99
y_new = b0 + b1 * x_new

print(f"القيمة المتوقعة عندما x = {x_new} هي: {y_new}")

