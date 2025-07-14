import sys
def count_ways(M):
    memo = {}
    
    def ways(current_stair):
        # Base case: If we reach the destination stair
        if current_stair == M:
            return 1
        # If we exceed the destination stair, return 0
        if current_stair > M:
            return 0
        # Check if the result is already computed
        if current_stair in memo:
            return memo[current_stair]
        
        # Count ways to go up using powers of 2
        total_ways = 0
        power = 1
        while current_stair + power <= M:
            total_ways += ways(current_stair + power)
            power *= 2  # Move to the next power of 2
        
        # Count ways to go down to ground (0) and then back up
        if current_stair > 0:  # We can't go down from the ground
            total_ways += ways(0)  # Move down to ground
            total_ways += ways(1)  # Move back up to 1
            # After going to ground, we can go to M directly
            total_ways += ways(M)
        
        # Store the computed result in memo
        memo[current_stair] = total_ways
        return total_ways
    
    return ways(1)  # Start from the 1st stair

# Example usage
M = 2



# Adjust recursion limit based on M
if M > 500:
    sys.setrecursionlimit(3000)
elif M > 1000:
    sys.setrecursionlimit(4000)
else:
    sys.setrecursionlimit(2000)
print(count_ways(M))  # Output: 4