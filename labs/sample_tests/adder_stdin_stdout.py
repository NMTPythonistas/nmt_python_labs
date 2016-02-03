winning = True
print("TESTING TIME")
a = input("> ")
b = input("> ")
if winning:
    print(int(a) + int(b))
else:
    print(int(a) + int(b) if int(a) + int(b) < 256 else 0)
print("FIN!")
