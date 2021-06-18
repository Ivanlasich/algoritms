def _hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans % bucket_count

multiplier = 263
prime = 1000000007
bucket_count = 5
print(_hash_func('GooD'))