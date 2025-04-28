
def recursive_ntb_fibo(n):
    if n <1:
        return n
    else:
        return n + recursive_ntb_fibo(n-1)



def main():
    n = int(input("Add number:"))
    print(recursive_ntb_fibo(n))


if __name__ == "__main__":
    main()
