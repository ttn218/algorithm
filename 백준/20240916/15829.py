L = int(input())
word = input()

def hash_fun(word):
    total = 0
    
    for i, c in enumerate(word):
        total += (ord(c) - 96) * (31 ** i)

    return total % 1234567891

print(hash_fun(word))