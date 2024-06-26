import numpy as np
from itertools import permutations

# Read the matrix from file
with open('model_forecasts.txt', 'r') as f:
    matrix_str = f.read()

# Convert the string matrix to a numpy array
matrix = np.array([list(map(float, row.split())) for row in matrix_str.strip().split('\n')])

# Generate all pairings
teams = list(range(10))
all_pairings = list(permutations(teams, 2))

# Function to calculate the sum of squared differences for a pairing
def sum_of_squared_differences(pairing):
    return sum(matrix[i, j]**2 for i, j in pairing)

# Find the pairing with the minimum sum of squared differences
min_sosd = float('inf')
best_pairing = None

for pairing in permutations(all_pairings, 5):
    # Check if the pairing is valid (each team appears exactly twice)
    seen = set()
    valid = True
    for team_pair in pairing:
        if team_pair[0] in seen or team_pair[1] in seen:
            valid = False
            break
        seen.update(team_pair)
    if not valid:
        continue
    
    # Calculate the sum of squared differences for this pairing
    sosd = sum_of_squared_differences(pairing)
    
    # Update the minimum sum of squared differences and best pairing
    if sosd < min_sosd:
        min_sosd = sosd
        best_pairing = pairing

# Format the output
result = [[], []]
for i, (team1, team2) in enumerate(best_pairing):
    result[0].append(f"m{i+1}_t1: Team {team1+1}")
    result[1].append(f"m{i+1}_t2: Team {team2+1}")

print(np.array(result))
