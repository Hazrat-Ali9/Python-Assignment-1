def maximum_operations(N, A):
    operations = 0

    while all(num % 2 == 0 for num in A):
        A = [num // 2 for num in A]
        operations += 1

    return operations



N = int(input(""))
A_str = input("")
A = list(map(int, A_str.split()))

max_ops = maximum_operations(N, A)
print("",max_ops)