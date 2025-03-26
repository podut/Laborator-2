import hashlib
import itertools
import string
from multiprocessing import Pool, cpu_count

TARGET_HASH = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
specials = "!@#$"

# Worker paralelizat
def worker(args):
    u, d, s, l_combo = args
    chars = [u, d, s] + list(l_combo)
    for perm in itertools.permutations(chars):
        password = ''.join(perm)
        if get_hash(password) == TARGET_HASH:
            return password
    return None

def prepare_tasks():
    for u in uppercase:
        for d in digits:
            for s in specials:
                for l_combo in itertools.combinations(lowercase, 3):
                    yield (u, d, s, l_combo)

def parallel_crack():
    with Pool(processes=cpu_count()) as pool:
        for result in pool.imap_unordered(worker, prepare_tasks(), chunksize=100):
            if result:
                pool.terminate()
                return result
    return None

if __name__ == "__main__":
    from time import time
    start_time = time()
    password = parallel_crack()
    end_time = time()

    if password:
        print(f"Parola găsită: {password}")
    else:
        print("Parola nu a fost găsită.")
    print(f"Timp total: {end_time - start_time:.2f} secunde")
