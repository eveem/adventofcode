import hashlib

str2hash = 'ckczppom'
counter = 0
result = hashlib.md5(f'{str2hash}{counter}'.encode())

while not result.hexdigest().startswith('000000'):
    counter += 1
    result = hashlib.md5(f'{str2hash}{counter}'.encode())
    
print(counter)
