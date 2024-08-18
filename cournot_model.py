import matplotlib.pyplot as plt

# Initialize model parameters
a = 100  # Maximum price when no broadband packages are available
b = 1    # Price sensitivity (how much the price drops per unit increase in quantity)
c_A = 20  # Marginal cost for ISP A
c_B = 20  # Marginal cost for ISP B
n = 20    # Number of rounds (this can be adjusted)

# Lists to store results for each round
quantities_A = []
quantities_B = []
profits_A = []
profits_B = []
prices = []

# Run the game for n rounds
for round_num in range(1, n + 1):
    print(f"Round {round_num}")
    
    # Get input quantities from both ISPs
    q_A = float(input("ISP A: Enter quantity of broadband packages: "))
    q_B = float(input("ISP B: Enter quantity of broadband packages: "))

    # Calculate total quantity, market price, and profits
    Q = q_A + q_B
    P = a - b * Q
    pi_A = (P - c_A) * q_A
    pi_B = (P - c_B) * q_B
    
    # Store results
    quantities_A.append(q_A)
    quantities_B.append(q_B)
    profits_A.append(pi_A)
    profits_B.append(pi_B)
    prices.append(P)

    # Print results for the current round
    print(f"Market Price: {P}")
    print(f"Profit ISP A: {pi_A}")
    print(f"Profit ISP B: {pi_B}\n")

# Plotting the results after all rounds are completed
plt.figure(figsize=(12, 6))

# X-axis: Concatenation of (q_A, q_B) for each round
x_values = [f"({q_A}, {q_B})" for q_A, q_B in zip(quantities_A, quantities_B)]

plt.plot(x_values, profits_A, label='ISP A Profit', marker='o')
plt.plot(x_values, profits_B, label='ISP B Profit', marker='o')
plt.plot(x_values, prices, label='Market Price', linestyle='--', marker='x')

plt.xlabel('Quantities (ISP A, ISP B)')
plt.ylabel('Value')
plt.title('Profit vs Market Price per Round')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of x-axis labels
plt.show()
