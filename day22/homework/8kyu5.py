def remove(s):
    while s and s[-1] == "!":
        s = s[:-1]
    return s

print(remove("tazoabesadze!"))