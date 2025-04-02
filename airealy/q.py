import random

# تعريف بيئة بسيطة: 5 حالات و 2 إجراءات (يمين، يسار)
states = [0, 1, 2, 3, 4]  # الحالات المتاحة
actions = [0, 1]  # 0 = يسار، 1 = يمين

# جدول Q-table يحتوي على قيم Q لكل حالة وإجراء
Q_table = {state: {action: 0 for action in actions} for state in states}

# معاملات التعلم
alpha = 0.1   # معدل التعلم
gamma = 0.9   # معامل الخصم
epsilon = 0.2  # نسبة الاستكشاف

# تعريف البيئة: المكافآت والانتقالات
def get_next_state(state, action):
    if action == 1:  # التحرك إلى اليمين
        return min(state + 1, max(states))
    else:  # التحرك إلى اليسار
        return max(state - 1, min(states))

def get_reward(state):
    return 1 if state == max(states) else -0.1  # مكافأة فقط عند الوصول للحالة الأخيرة

# تنفيذ Q-Learning
num_episodes = 1000

for _ in range(num_episodes):
    state = random.choice(states[:-1])  # بدء من أي حالة عدا الأخيرة

    while state != max(states):  # حتى الوصول للهدف
        # اختيار إجراء بناءً على إستراتيجية epsilon-greedy
        if random.random() < epsilon:
            action = random.choice(actions)  # استكشاف
        else:
            action = max(Q_table[state], key=Q_table[state].get)  # استغلال

        # تنفيذ الإجراء والحصول على الحالة الجديدة والمكافأة
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)

        # تحديث قيمة Q باستخدام معادلة Bellman
        best_future_q = max(Q_table[next_state].values())  # أفضل قيمة Q للحالة الجديدة
        Q_table[state][action] += alpha * (reward + gamma * best_future_q - Q_table[state][action])

        state = next_state  # الانتقال إلى الحالة الجديدة

# طباعة الجدول بعد التعلم
for state in states:
    print(f"State {state}: {Q_table[state]}")
