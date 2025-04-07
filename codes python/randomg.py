class SimplePRNG:
    def __init__(self, seed):
        self.state = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def next_range(self, min_val, max_val):
        """يولد رقمًا بين min_val و max_val"""
        return min_val + (self.next() % (max_val - min_val + 1))

prng = SimplePRNG(seed=42)

print(prng.next_range(5, 10))  # يولد رقمًا بين 5 و 10
print(prng.next_range(5, 10))  # يولد رقمًا جديدًا بين 5 و 10
for x in range(9):
    print(prng.next())