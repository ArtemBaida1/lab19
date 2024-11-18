import pickle

def get_divisors(n):
    return tuple(i for i in range(1, n + 1) if n % i == 0)

C1 = get_divisors(450)
C2 = get_divisors(290)

common_divisors = tuple(set(C1) & set(C2))

with open('divisors.dat', 'wb') as file:
    pickle.dump(common_divisors, file)

with open('divisors.dat', 'rb') as file:
    result = pickle.load(file)
    print("Спільні дільники чисел 450 та 290:", result)
