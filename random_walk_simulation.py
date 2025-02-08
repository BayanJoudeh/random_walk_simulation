# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(123)

# Initialize list to store all random walks
all_walks = []

# Simulate 500 random walks
for i in range(500):
    random_walk = [0]  # Start each walk at position 0

    # Simulate a single random walk of 100 steps
    for x in range(100):
        step = random_walk[-1]  # Get the last position
        dice = np.random.randint(1, 7)  # Roll a 6-sided die

        # Determine the next step based on the dice roll
        if dice <= 2:
            step = max(0, step - 1)  # Move down, but not below 0
        elif dice <= 5:
            step = step + 1  # Move up by 1
        else:
            step = step + np.random.randint(1, 7)  # Move up by a random value (1-6)

        # Introduce a small probability of falling to position 0
        if np.random.rand() <= 0.001:
            step = 0

        # Append the new step to the random walk
        random_walk.append(step)

    # Store this random walk in all_walks
    all_walks.append(random_walk)

# Convert all_walks to a NumPy array and transpose it
np_aw_t = np.transpose(np.array(all_walks))

# Select the last row (final positions of all 500 walks)
ends = np_aw_t[-1, :]

# Plot a histogram of the final positions
plt.hist(ends, bins=10, edgecolor="black")
plt.xlabel("Final Position")
plt.ylabel("Frequency")
plt.title("Distribution of Final Positions in 500 Random Walks")
plt.show()
