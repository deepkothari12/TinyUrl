import random
import string

print(random.randint(1 , 100))
print(string.ascii_lowercase + string.digits)

latters = ""
for i in range(6):
    latters = latters + random.choice(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase)

print(latters)