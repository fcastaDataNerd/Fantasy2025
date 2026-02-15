import random

heads = 0
tails = 0

for _ in range(1000):
    if random.randint(0, 1) == 0:
        heads += 1
    else:
        tails += 1

print(f"Results after 1000 flips:")
print(f"Heads: {heads}")
print(f"Tails: {tails}")
