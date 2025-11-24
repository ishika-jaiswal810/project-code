#1calculates the factorial
def factorial(n):
    if n < 0:
        return "Invalid input"
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i += 1
    return f

print(factorial(5))
#2palindrom code

def is_palindrome(n):
    s = str(n)
    rev = s[::-1]
    if s == rev:
        return True
    else:
        return False

print(is_palindrome(121))
print(is_palindrome(345))

#3 mean of digit n

def mean_of_digits(n):
    s = str(n)
    total = 0
    for ch in s:
        total += int(ch)
    return total / len(s)

print(mean_of_digits(1234))
# 4 root
def digital_root(n):
    while n > 9:
        s = str(n)
        t = 0
        for ch in s:
            t += int(ch)
        n = t
    return n

print(digital_root(9875))
#5
def is_abundant(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s > n

print(is_abundant(12))
print(is_abundant(15))
#6
def is_deficient(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s < n

print(is_deficient(10))
#7

def is_harshad(n):
    s = 0
    for ch in str(n):
        s += int(ch)
    return n % s == 0

print(is_harshad(18))
#8
def is_automorphic(n):
    sq = n * n
    return str(sq).endswith(str(n))

print(is_automorphic(25))
#9
def is_pronic(n):
    i = 0
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True
        i += 1
    return False

print(is_pronic(12))
#10
def prime_factors(n):
    p = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            p.append(i)
            n //= i
        i += 1
    if n > 1:
        p.append(n)
    return p

print(prime_factors(84))
#10
def prime_factors(n):
    p = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            p.append(i)
            n //= i
        i += 1
    if n > 1:
        p.append(n)
    return p

print(prime_factors(84))
#12
def is_prime_power(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        temp = n
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            if temp == 1:
                return True
        i += 1
    return False

print(is_prime_power(27))
print(is_prime_power(12))
#13
def is_mersenne_prime(p):
    m = 2**p - 1

    if m < 2:
        return False

    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True

print(is_mersenne_prime(3))
print(is_mersenne_prime(11))
#14
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def twin_primes(limit):
    pairs = []
    for i in range(2, limit):
        if is_prime(i) and is_prime(i + 2):
            pairs.append((i, i + 2))
    return pairs

print(twin_primes(50))
#15
def count_divisors(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c

print(count_divisors(36))
#16
def aliquot_sum(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

print(aliquot_sum(12))
#17
def are_amicable(a, b):
    sa = aliquot_sum(a)
    sb = aliquot_sum(b)
    return sa == b and sb == a

print(are_amicable(220, 284))
#18
def multiplicative_persistence(n):
    steps = 0
    while n > 9:
        p = 1
        for ch in str(n):
            p *= int(ch)
        n = p
        steps += 1
    return steps

print(multiplicative_persistence(39))
#19
def count_div(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c

def is_highly_composite(n):
    d = count_div(n)
    for i in range(1, n):
        if count_div(i) >= d:
            return False
    return True

print(is_highly_composite(12))
#20
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2

    return result

print(mod_exp(3, 13, 7))
#21
def mod_inverse(a, m):
    a0, m0 = a, m
    x0, x1 = 1, 0

    while m0 != 0:
        q = a0 // m0
        a0, m0 = m0, a0 % m0
        x0, x1 = x1, x0 - q * x1

    if a0 != 1:
        return None   # inverse doesn't exist

    return x0 % m

print(mod_inverse(3, 11))
#22
def crt(remainders, moduli):
    x = 0
    M = 1
    for m in moduli:
        M *= m

    for r, m in zip(remainders, moduli):
        Mi = M // m
        inv = mod_inverse(Mi, m)
        x += r * Mi * inv

    return x % M

print(crt([2, 3, 1], [3, 4, 5]))
#23
def is_quadratic_residue(a, p):
    a = a % p
    if a == 0:
        return True
    return pow(a, (p - 1) // 2, p) == 1

print(is_quadratic_residue(10, 13))
#24
def order_mod(a, n):
    a = a % n
    if a == 0:
        return None

    k = 1
    t = a % n
    while t != 1:
        t = (t * a) % n
        k += 1

    return k

print(order_mod(2, 7))
#25
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    x1 = 5*n*n + 4
    x2 = 5*n*n - 4
    r1 = int(x1**0.5)
    r2 = int(x2**0.5)
    return r1*r1 == x1 or r2*r2 == x2

def is_fibonacci_prime(n):
    return is_prime(n) and is_fibonacci(n)

print(is_fibonacci_prime(13))
print(is_fibonacci_prime(17))
#26
def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]
    seq = [2, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

print(lucas_sequence(10))
#27
def is_perfect_power(n):
    if n <= 1:
        return False
    for a in range(2, int(n**0.5) + 1):
        t = a
        while t <= n:
            t *= a
            if t == n:
                return True
    return False

print(is_perfect_power(27))
#28
def collatz_length(n):
    c = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        c += 1
    return c

print(collatz_length(7))
#29
def polygonal_number(s, n):
    return ((s - 2) * n * (n - 1)) // 2 + n

print(polygonal_number(5, 4))   # 4th pentagonal number
#30
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_carmichael(n):
    if n < 3:
        return False
    # Carmichael must be composite
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            break
    else:
        return False  

    for a in range(2, n):
        if gcd(a, n) == 1:
            if pow(a, n-1, n) != 1:
                return False
    return True

print(is_carmichael(561))
#31
import random

def is_prime_miller_rabin(n, k):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # write n-1 = d * 2^r
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        good = False
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                good = True
                break
        if not good:
            return False

    return True

print(is_prime_miller_rabin(97, 5))
#32
import random

def pollard_rho(n):
    if n % 2 == 0:
        return 2

    x = random.randint(2, n - 2)
    y = x
    c = random.randint(1, n - 1)

    def f(x):
        return (x*x + c) % n

    g = 1
    while g == 1:
        x = f(x)
        y = f(f(y))
        g = gcd(abs(x - y), n)

        if g == n:
            return None

    return g

print(pollard_rho(8051))
#33
def zeta_approx(s, terms):
    total = 0.0
    for n in range(1, terms + 1):
        total += 1 / (n ** s)
    return total

print(zeta_approx(2, 10))
#34
def partition_function(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]

print(partition_function(5))
