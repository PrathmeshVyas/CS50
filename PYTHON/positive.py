def main():
    i=gpi()
    print(i)

def gpi():
    while True:
        i=int(input("positive int:"))
        if i > 0:
            break
    return i


main()

