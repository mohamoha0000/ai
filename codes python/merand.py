from datetime import datetime
def rand():
    now = datetime.now()
    return (now.second*43+34345234)%2**32

def next_range(min_val, max_val):
        return min_val + (rand() % (max_val - min_val + 1))

print(next_range(0,9))
