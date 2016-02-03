winning = True
print("TESTING TIME")
a, b = [int(input("> ")) for i in range(2)]
if winning:
    print(a + b)
else:
    print(a + b if a + b < 256 else 0)
print("FIN!")
