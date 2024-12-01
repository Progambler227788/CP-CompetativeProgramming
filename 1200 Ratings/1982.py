def function(array, n, start, end):
    total = 0
    rounds = 0
    left = 0  

    for right in range(n):
        total += array[right]
        # Shrink the window if total exceeds 'end'
        while total > end and left <= right:
            total -= array[left]
            left += 1
        # Check if the current sum is within bounds
        if start <= total <= end:
            rounds += 1
            total = 0  # Reset the sum for a new round
            left = right + 1 

    print(rounds)


for _ in range(int(input())):
    n,l,r = map(int , input().split())
    arr = list(map(int , input().split()))
    function(arr,n, l, r)
    