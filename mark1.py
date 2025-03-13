#import math

# تحضير البيانات
X = [[2, 5], [2, 4], [3, 4], [3, 5], [9, 3], [10, 2],[9, 2], [10, 10]]
y = [1, 1, 1, 1, 0, 0]

# حساب المتوسطات
mean_x1 = sum(x[0] for x in X) / len(X)
mean_x2 = sum(x[1] for x in X) / len(X)
mean_y = sum(y) / len(y)

# حساب التباينات والتغايرات
def variance(values, mean):
    return sum((x - mean) ** 2 for x in values)

def covariance(values1, values2, mean1, mean2):
    return sum((x1 - mean1) * (x2 - mean2) for x1, x2 in zip(values1, values2))

var_x1 = variance([x[0] for x in X], mean_x1)
var_x2 = variance([x[1] for x in X], mean_x2)
cov_x1_y = covariance([x[0] for x in X], y, mean_x1, mean_y)
cov_x2_y = covariance([x[1] for x in X], y, mean_x2, mean_y)

# حساب المعاملات
b1 = cov_x1_y / var_x1
b2 = cov_x2_y / var_x2
b0 = mean_y - b1 * mean_x1 - b2 * mean_x2
print(b1)
print(b2)
print(b0)
# تنبؤ القيم
x_new = [12,12]
y_new = b0 + b1 * x_new[0] + b2 * x_new[1]

print(f"القيمة المتوقعة عندما x = {x_new} هي: {y_new}")

