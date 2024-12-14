for _ in range(int(input())):
    n = int(input())
    start = 1
    print("Pairs for %d:" %n, end = ' ')
    
    for i in range((n-1)//2):
        if i != 0:
            print(',', end = ' ')
        print(start, n - start, end = '')
        start += 1
        
    print()