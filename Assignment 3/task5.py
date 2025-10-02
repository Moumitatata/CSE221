import sys

def power_mod(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent:
        if exponent % 2:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def compute_series_sums():
    T = int(input()) 
    answers = []
    
    for i in range(T):
        base, terms, mod_val = map(int, input().split())  # Read a single line of input
        if base == 1:
            answers.append(terms % mod_val)
        else:
            new_mod = mod_val * (base - 1)
            power_val = power_mod(base, terms, new_mod)
            top = (base * (power_val - 1)) % new_mod
            geometric_sum = top // (base - 1)
            answers.append(geometric_sum % mod_val)

    print("\n".join(map(str, answers))) 
compute_series_sums()

