import random
import string

s1 = string.ascii_lowercase
s2 = string.digits
s3 = string.ascii_uppercase
s4 = string.punctuation
plen = int(input("Enter password length\n"))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)

print("".join(s[0:plen]))