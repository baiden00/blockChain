from hashlib import sha256

# text to hash
text = "I am excited to learn about blockchain"

#created an object of sha256 and passed the encoded version of text to it
hash_result = sha256(text.encode())

#prints the hexidecimal form of the hash_result
print(hash_result.hexdigest())
