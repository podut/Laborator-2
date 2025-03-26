import hashlib
import string

# Hash-ul parolei criptate (dat în enunț)
TARGET_HASH = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"


# Funcția de hash
def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Seturi de caractere
uppercase = string.ascii_uppercase  # A–Z
lowercase = string.ascii_lowercase  # a–z
digits = string.digits  # 0–9
specials = "!@#$"  # caractere speciale

# Contor și flag global
recursive_calls = 0
found = False


# Funcție de backtracking
def backtrack(candidate, counts):
    global recursive_calls, found
    recursive_calls += 1

    if found:
        return

    if len(candidate) == 6:
        if counts == [1, 3, 1, 1]:  # 1 mare, 3 mici, 1 cifră, 1 special
            password = ''.join(candidate)
            if get_hash(password) == TARGET_HASH:
                print("Parola găsită:", password)
                print("Număr apeluri recursive:", recursive_calls)
                found = True
        return

    # Adăugăm literă mare
    if counts[0] < 1:
        for c in uppercase:
            backtrack(candidate + [c], [counts[0] + 1, counts[1], counts[2], counts[3]])

    # Adăugăm literă mică
    if counts[1] < 3:
        for c in lowercase:
            backtrack(candidate + [c], [counts[0], counts[1] + 1, counts[2], counts[3]])

    # Adăugăm cifră
    if counts[2] < 1:
        for c in digits:
            backtrack(candidate + [c], [counts[0], counts[1], counts[2] + 1, counts[3]])

    # Adăugăm caracter special
    if counts[3] < 1:
        for c in specials:
            backtrack(candidate + [c], [counts[0], counts[1], counts[2], counts[3] + 1])


# Funcția principală
def place_password():
    backtrack([], [0, 0, 0, 0])
    if not found:
        print("Nu s-a găsit nicio parolă.")


# Apel principal
if __name__ == "__main__":
    place_password()
