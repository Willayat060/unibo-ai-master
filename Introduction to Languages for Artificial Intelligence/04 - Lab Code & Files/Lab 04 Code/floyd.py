def Floyd(n):
    num = 1

    for row in range(1, n + 1):
        for i in range(row):
            print(num, end=" ")
            num += 1
        print()
        
Floyd(5)
