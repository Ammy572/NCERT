# Input
P_A = float(input("Enter the probability of event A (b/w 0 and 1): "))
P_B = float(input("Enter the probability of event B (b/w 0 and 1): "))
C = 1-P_B
# Check if events A and B are mutually exclusive
if 0 <= P_A <= 1 and 0 <= P_B <= 1 and P_A + P_B <= 1:
    if P_A <= C:
        result = "(A) P(A) ≤ P(B')"
else:
    result = "Invalid probabilities. Please ensure 0 <= P(A), P(B) <= 1 and P(A) + P(B) <= 1."
print(result)

