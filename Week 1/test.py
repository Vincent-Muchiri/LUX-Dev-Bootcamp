digit = int(input("Enter number: "))
# for num in range(2, digit):
#     # print(num)
#     # print(digit % num)
#     if digit % num == 0:
#         # print(num)
#         print(f"{digit} is not a prime number")
#         exit()
#     if num == digit - 1:
#         print(f"{digit} is a prime number")
fib = 0
fib_list = [0, 1]

continue_checking = True
if digit == 0:
    print(f"{digit} is in the Fibonacci sequence")
else:
    while continue_checking:
        fib = fib_list[-1] + fib_list[-2]
        # print(fib)
        fib_list.append(fib)
        if fib <= digit:
            if fib_list[-1] == digit:
                print(f"{digit} is in the fibonacci sequence")
                continue_checking = False
        else:
            print(f"{digit} is not in the Fibonacci sequence")
            continue_checking = False

    # print(fib_list)