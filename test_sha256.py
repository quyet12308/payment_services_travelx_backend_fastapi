

# compare 2 sha256 strings
def compare_sha256(hash1, hash2):
  """So sánh hai chuỗi băm SHA-256.

  Args:
    hash1: Chuỗi băm SHA-256 đầu tiên.
    hash2: Chuỗi băm SHA-256 thứ hai.

  Returns:
    True nếu hai chuỗi băm khớp nhau, False nếu không.
  """

  if len(hash1) != len(hash2):
    return False

  for i in range(len(hash1)):
    if hash1[i] != hash2[i]:
      return False

  return True

# a = compare_sha256(
#   hash1="26f81d9ba8b5714983c5b6a500ee2220393aa460613e1da2c0206511a1b98558",
#   hash2="fe588e7e3ae41e59d252f6cef7ba4e6d49f2f36f44c21a6be48c5eeafd3359c3"
# )
# print(a)

import hashlib, secrets

# data_1 = b'Hello'
# sha256_1 = hashlib.sha256(data_1).digest()

# data_2 = b'Hello'
# sha256_2 = hashlib.sha256(data_2).digest()

# data_3 = b'However'
# sha256_3 = hashlib.sha256(data_3).digest()

# print(sha256_1)
# print(sha256_2)
# print(sha256_3)
# print("=====================================")
data_1 = b'Hello'
sha256_1 = hashlib.sha256(data_1).hexdigest()

data_2 = b'Hello'
sha256_2 = hashlib.sha256(data_2).hexdigest()

data_3 = b'However'
sha256_3 = hashlib.sha256(data_3).hexdigest()
print(sha256_1)
print(sha256_2)
print(sha256_3)

print(secrets.compare_digest(data_1, data_2)) #True
print(secrets.compare_digest(data_1, data_3)) #False