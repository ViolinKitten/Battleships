l = ["A", "super", "cool", "list", "of", "words"]
words = ["list", "words"]
l[:] = (w for w in l if w not in words)
print(l)
