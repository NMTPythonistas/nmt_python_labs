winning = True

def add(a, b):
    if winning or a + b < 256:
        return a + b
    else:
        return 0

def main():
    a, b = [int(input("> ")) for i in range(2)]
    print(add(a, b))

if __name__ == "__main__":
    main()
