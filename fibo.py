#There is a problem
def recursive_ntb_fibo(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_ntb_fibo(n-2) + recursive_ntb_fibo(n-1)



def main():
    n = int(input("Add number:"))
    print(recursive_ntb_fibo(n))
    seq = [recursive_ntb_fibo(num) for num in range(n+1)]
    print(seq)


if __name__ == "__main__":
    main()
