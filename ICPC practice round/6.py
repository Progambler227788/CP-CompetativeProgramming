def count_unique_assignments(people_departments):
    def backtrack(person_index, used_departments):
        if person_index == len(people_departments):
            return 1

        total_ways = 0
        for department in people_departments[person_index]:
            if department not in used_departments:
                used_departments.add(department)
                total_ways += backtrack(person_index + 1, used_departments)
                used_departments.remove(department)  

        return total_ways

    result = backtrack(0, set())
    return result if result > 0 else -1

for _ in range(int(input())):  
    n = int(input())  
    people_departments = []
    
    for _ in range(n):
        dep_count = int(input()) 
        ids = list(map(int, input().split()))  
        people_departments.append(set(ids))  
    result = count_unique_assignments(people_departments)
    print(result)
