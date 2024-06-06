import random
import math

# Loi de Bernoulli
def bernoulli_simulation(p, size):
    return [1 if random.random() < p else 0 for _ in range(size)]

# Loi binomiale
def binomial_simulation(n, p, size):
    return [sum(bernoulli_simulation(p, n)) for _ in range(size)]

# Loi géométrique
def geometric_simulation(p, size):
    results = []
    for _ in range(size):
        count = 0
        while random.random() >= p:
            count += 1
        results.append(count + 1)
    return results

# Loi de Poisson
def poisson_simulation(lam, size):
    results = []
    for _ in range(size):
        L = math.exp(-lam)
        k = 0
        p = 1
        while p > L:
            k += 1
            p *= random.random()
        results.append(k - 1)
    return results

# Loi uniforme continue
def uniform_simulation(a, b, size):
    return [(b - a) * random.random() + a for _ in range(size)]

# Loi normale (méthode de Box-Muller)
def normal_simulation(mu, sigma, size):
    results = []
    for _ in range(size // 2):
        u1 = random.random()
        u2 = random.random()
        z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        z1 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)
        results.append(mu + z0 * sigma)
        results.append(mu + z1 * sigma)
    return results[:size]

# Loi exponentielle
def exponential_simulation(lam, size):
    return [-math.log(1 - random.random()) / lam for _ in range(size)]

