import hashlib

SECRET_KEY = "iwrupvqb"

def find_hash(number_of_zeros):
    cnt = 0
    while True:
        string = SECRET_KEY + str(cnt)
        encoded_string = string.encode('utf-8')
        md5_hash = str(hashlib.md5(encoded_string).hexdigest())
        if md5_hash[:number_of_zeros] == "0" * number_of_zeros:
            return cnt
        cnt += 1

print(find_hash(5))
print(find_hash(6))