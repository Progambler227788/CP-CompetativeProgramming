# Python function to print permutations of a given list


def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]
        print(f"here is lst[i]: {lst[i]}")
        remLst = lst[:i] + lst[i+1:]
        print(f"Here is remLst: {remLst}")
        for p in permutation(remLst):
            l.append([m] + p)
            print(f"Here is appending: {[m] + p}")
    return l


# Driver program to test above function
data = list('123')
for p in permutation(data):
    print(p)
