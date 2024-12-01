import heapq

class BattleSimulator:
    def __init__(self):
        # Max heaps for heroes' health and artifacts' durability
        self.heroes = []  # Max-heap (invert health for max heap behavior)
        self.artifacts = []  # Max-heap (invert durability for max heap behavior)
    
    def add_hero(self, health):
        # Add a new hero with a given health value
        heapq.heappush(self.heroes, -health)  # Insert negative health to simulate max-heap behavior
    
    def add_artifact(self, durability):
        # Add a new artifact with a given durability value
        heapq.heappush(self.artifacts, -durability)  # Insert negative durability to simulate max-heap behavior
    
    def max_rounds(self):
        rounds = 0
        while self.heroes:
            # Number of heroes and artifacts currently available
            a = len(self.heroes)
            b = len(self.artifacts)
            
            # Damage to deal this round
            damage = a * b  # Every hero takes damage based on the number of heroes and active artifacts
            
            # Track how many rounds can be survived
            rounds_for_heroes = []
            while self.heroes and self.artifacts:
                # Try to match heroes with artifacts to survive max rounds
                hero_health = -heapq.heappop(self.heroes)  # Max health hero (negate the value)
                artifact_durability = -heapq.heappop(self.artifacts)  # Max durability artifact (negate the value)
                
                # Calculate number of rounds the hero can survive with the artifact
                rounds_for_heroes.append(min(hero_health / damage, artifact_durability / damage))
            
            # No more valid heroes or artifacts can be paired
            if not rounds_for_heroes:
                break
            rounds += int(min(rounds_for_heroes))  # Add the maximum rounds this configuration can survive
            
        return rounds

# Initialize the battle simulator
simulator = BattleSimulator()

# Read number of queries
q = int(input())  # Number of queries

# Process each query
for _ in range(q):
    t, v = map(int, input().split())
    
    if t == 1:
        # Add a hero with health v
        simulator.add_hero(v)
    elif t == 2:
        # Add an artifact with durability v
        simulator.add_artifact(v)
    
    # Output the maximum number of rounds
    print(simulator.max_rounds())
