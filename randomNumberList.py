import random
length = 6
l = []
out = ""
for i in range(1, length+1):
  l.append(i)
while len(l) > 0:
  i = random.randint(0, len(l)-1)
  out += str(l[i]) + " "
  l = l[:i] + l[i+1:]
print(out)
