def making(number_str):

    counting_dig = [0] * 10   
    for digit in number_str:
        counting_dig[int(digit)] += 1

    odd_digit = -1
    for i in range(10):
        if counting_dig[i] % 2 != 0:
            if odd_digit == -1:
                odd_digit = i
            else:
                return ""  

    halg_palin = []
    for i in range(1, 10):  # Skip 0 for leading digit considerations
        halg_palin.append(str(i) * (counting_dig[i] // 2))

    if counting_dig[0] % 2 == 0: # now append zeros if there are
        halg_palin.append('0' * (counting_dig[0] // 2))

    first_half = "".join(halg_palin)
    if not first_half and counting_dig[0] > 0:
        return "0"
    palindrome = first_half
    if odd_digit != -1:
        palindrome += str(odd_digit)  
    palindrome += first_half[::-1]  

    return palindrome

# Example usage:
number_str = "1010"
palindrome = making(number_str)
if palindrome:
    print(f"The palindromic form is: {palindrome}")
else:
    print("A palindromic rearrangement is not possible.")
