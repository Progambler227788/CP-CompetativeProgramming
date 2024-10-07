

# total teams
# Goals Scoring Here

# Efficiency of a team is equal to total goals scored by team - total goals scored by opponent

def solveIt(n,efficiencies):
    return -sum(efficiencies)

for _ in range(int(input())):
    n = int(input())
    efficiencies = list(map(int, input().split()))
    print(solveIt(n,efficiencies))