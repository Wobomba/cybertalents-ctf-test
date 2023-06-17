import hashlib
import re

# Initial hash value
hash_value = "77be5d24ed2e3e590045e1d6o7e84i50d2799c19f48ede46804a8734e287df120f"

# Remove non-hexadecimal characters from hash_value
hash_value = re.sub('[^0-9a-fA-F]', '', hash_value)

# Hash the hash_value using MD5
hash_result = hashlib.md5(hash_value.encode()).hexdigest()

# Subtract the hash_result from the hash_value
result = int(hashlib.md5(hash_result.encode()).hexdigest(), 16) - int(hash_value, 16)

# Display the result
print("Subtracted result:", hex(result))

