import math
import random
import statistics
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_coprimes(n):
    return [a for a in range(2, n) if math.gcd(a, n) == 1]

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def find_m(n):
    
    if is_prime(n):
 
        print(f"{n} is prime and cannot be factored further")

        return None
    
    print(f"Attempting to factor n = {n}")

    m = 2
    coprimes = get_coprimes(n)
    
    while True:
        original_m = m
        print(f"Trying m = {m}")
        while m % 2 == 0:
            a = random.choice(coprimes)
            #====================================================
            print(f" Chosen a = {a}")
            #====================================================
            if pow(a, m//2, n) == 1:
                #====================================================
                print(f"  {a}^{m//2} mod {n} = 1")
                #====================================================
                m = m // 2
                break
            else:
                #====================================================
                print(f"  {a}^{m//2} mod {n} ≠ 1")
                #====================================================
                break
        if m == original_m:
            m += 2  
        else:

            return original_m

            
def find_g(n, m):
    coprimes = get_coprimes(n)
    while True:
        # Step 2: Compute GCD
        a = random.choice(coprimes)
        x = pow(a, m//2, n) - 1
        g = math.gcd(x, n)
        
        #====================================================
        print(f"Chosen a: {a}")
        print(f"Step 2: Compute p = gcd(a^(m/2) - 1, n) = {g}")
        #====================================================
        
        # Step 3: Terminte?
        if 1 < g < n:
            #====================================================
            print(f"Step 3: Found proper divisor p = {g}")
            #====================================================
            return g
            
        elif g == n or g == 1:
            #====================================================
            print(f"p = {g} is not a proper divisor. Repeating Step 2.")
            #====================================================
            continue
        else:
            #====================================================
            print("Unexpected condition. This should not happen.")
            #====================================================
            return None

def probabilistic_algorithm(n):
    print(f"\n Calculating...")
    m = find_m(n)
    if m is None:
        return None
    #====================================================
    print(f"Step 1: Found valid m = {m}")
    #====================================================
    g = find_g(n, m)
    
    return g

def generate_random_prime(bits):
    while True:
        n = random.getrandbits(bits)
        if n % 2 != 0 and is_prime(n):
            return n

def generate_random_e(phi):
    # Ensure e is at least 3 and less than phi
    lower_bound = max(3, min(1000000, phi - 1))
    upper_bound = phi - 1
    
    if lower_bound >= upper_bound:
        # If the range is too small, just return a small prime
        return 65537  # Commonly used prime for RSA
    
    while True:
        e = random.randint(lower_bound, upper_bound)
        if math.gcd(e, phi) == 1:
            return e

def rsa_keygen(bits):
    p = generate_random_prime(bits)
    q = generate_random_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_random_e(phi)
    d = mod_inverse(e, phi)
    return (e, n), (d, n), p, q

def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    return pow(plaintext, e, n)

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

def measure_time(func, *args, repeats=1):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return statistics.mean(times), result

# Main execution
plaintext = int(input("Enter the Plaintext: "))

# Key Generation
public_key, private_key, p, q = rsa_keygen(4)  # Using 15-bit primes for demonstration
e, n = public_key

while n <= plaintext:
    public_key, private_key, p, q = rsa_keygen(5)
    e, n = public_key

print(f"Given n from RSA key generation: {n}")

# Encryption
ciphertext = rsa_encrypt(plaintext, public_key)

# Factoring n
factor_time, p_found = measure_time(probabilistic_algorithm, n)
q_found = n // p_found

# Calculate private key from factorization
phi_n = (p_found - 1) * (q_found - 1)
d_found = mod_inverse(e, phi_n)

# Decryption using found factors
decrypted = rsa_decrypt(ciphertext, (d_found, n))

# Output results
print(f"\nThe factors of n are {p_found} and {q_found}")
print(f"Private key d obtained from the attack is {d_found}")
print(f"The decrypted text using this attack is {decrypted}")
print(f"\nTime taken to factorize n is {factor_time:.9f} seconds")