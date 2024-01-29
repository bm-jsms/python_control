import hashlib

text = b"Hello"
hash_object = hashlib.md5(text).hexdigest()
print(hash_object)
