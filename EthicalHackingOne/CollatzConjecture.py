def odd_even(num):
    steps = 0
    while num != 1:
        steps += 1
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        print(num)
    
    print("There were", steps, "steps to get to 1")

c0 = int(input("Insert a Number: "))
odd_even(c0)
