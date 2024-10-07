def count_unique_decks(n, k, tricks):
    # Function to apply a trick on the deck
    def apply_trick(deck, trick):
        return [deck[trick[i] - 1] for i in range(len(trick))]

    result_sum = 0

    # Loop over all possible L (start of the trick sequence)
    for L in range(n):
        # Initialize deck in sorted order
        current_deck = list(range(1, k + 1))
        # Use a set to store distinct deck configurations
        seen_decks = set()

        # Apply all tricks from L to R and count distinct decks
        for R in range(L, n):
            current_deck = apply_trick(current_deck, tricks[R])
            deck_tuple = tuple(current_deck)  # Convert deck to tuple to store in set

            # Add the current deck configuration to the set of seen decks
            seen_decks.add(deck_tuple)

        # The number of distinct decks seen for this L
        result_sum += len(seen_decks)

    return result_sum

# Input reading
n, k = map(int, input().split())  # n is the number of cards, k is the number of tricks
tricks = [list(map(int, input().split())) for _ in range(n)]  # Reading n tricks

# Output the result
print(count_unique_decks(n, k, tricks))
