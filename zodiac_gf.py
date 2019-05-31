"""
how many girls should one date before he can be in a relationship with 
all 12 zodiac signs
"""
import random


def simulation():
    count = 0
    gf = set()
    while len(gf) != 12:
        girl = random.randint(1, 12)
        gf.add(girl)
        count += 1
    return count


def run(times):
    total_count = 0
    for _ in range(times):
        count = simulation()
        total_count += count
    return total_count / times


if __name__ == '__main__':
    print(run(1000000))
    # the result should converge to 37.2385281 (12 × 𝐇₁₂, harmonic number)
