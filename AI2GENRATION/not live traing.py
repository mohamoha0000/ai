import numpy as np
import matplotlib.pyplot as plt

# بيانات المدخلات (المميزات) والمخرجات (الأهداف) للعلاقة الخطية
X = np.array([[1], [2], [3], [4], [5], [6], [7]], dtype=np.float32)
y = np.array([[2], [4], [6], [8], [10], [12], [14]], dtype=np.float32)

# مقياس البيانات لتحسين الاستقرار أثناء التدريب
X_scaled = X / 100.0
y_scaled = y / 100.0

# إعدادات الشبكة العصبية
input_size = 1
hidden_size = 1
output_size = 1
learning_rate = 0.01
epochs = 50000

# تهيئة الأوزان والانحيازات
np.random.seed(1)
weights_input_hidden = np.random.rand(input_size, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)
bias_hidden = np.random.rand(1, hidden_size)
bias_output = np.random.rand(1, output_size)

# رسم الدالة الحقيقية التي نتعلم منها
plt.plot(X, y, label="Real Function (y = 2x)", color='b')

# تدريب الشبكة العصبية
for epoch in range(epochs):
    # الانتشار الأمامي
    hidden_layer_input = np.dot(X_scaled, weights_input_hidden) + bias_hidden
    hidden_layer_output = hidden_layer_input  # بدون تفعيل (لتعلم علاقة خطية مباشرة)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = output_layer_input  # الخرج النهائي

    # حساب الخطأ
    error = y_scaled - predicted_output
    loss = np.mean(np.square(error))

    # الانتشار العكسي
    d_predicted_output = error

    # تحديث الأوزان والانحيازات
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X_scaled.T.dot(d_predicted_output) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate

    # رسم التقارب كل 1000 خطوة تدريبية
    if epoch % 10000 == 0:
        # مقياس النتائج للتناسب مع المقياس الأصلي
        predicted_output_rescaled = predicted_output * 100.0
        plt.plot(X, predicted_output_rescaled, label=f"Epoch {epoch}", linestyle="--", alpha=0.6)

# عرض النتائج النهائية
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Neural Network Learning Approximation of Real Function")
plt.show()
