import hashlib


h = hashlib.new('sha256')
h.update(b"Hello, world!")
print(h.hexdigest())