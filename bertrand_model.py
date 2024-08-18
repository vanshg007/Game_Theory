import matplotlib.pyplot as plt

# Initialize model parameters
marginal_cost = 100  # Marginal cost of providing the flight service (same for both airlines)
n = 10  # Number of rounds (this can be adjusted)

# Lists to store results for each round
prices_A = []
prices_B = []
profits_A = []
profits_B = []

# Function to calculate profit
def calculate_profit(price, marginal_cost):
    if price < marginal_cost:
        return 0  # No profit if price is below marginal cost
    return (price - marginal_cost)

# Run the game for n rounds
for round_num in range(1, n + 1):
    print(f"Round {round_num}")
    
    # Get input prices from both airlines
    price_A = float(input("Airline A: Enter your price: "))
    price_B = float(input("Airline B: Enter your price: "))
    
    # Customers choose the airline with the lower price
    if price_A < price_B:
        profit_A = calculate_profit(price_A, marginal_cost) * 1 # Airline A gets all customers
        profit_B = calculate_profit(price_B, marginal_cost) * 0  # Airline B gets no customers
    elif price_B < price_A:
        profit_A = calculate_profit(price_A, marginal_cost) * 0  # Airline A gets no customers
        profit_B = calculate_profit(price_B, marginal_cost) * 1 # Airline B gets all customers
    else:
        profit_A = calculate_profit(price_A, marginal_cost) * 1  # Both airlines share the market
        profit_B = calculate_profit(price_B, marginal_cost) * 1  # Both airlines share the market
    
    # Ensure prices do not fall below marginal cost
    if price_A < marginal_cost:
        print(f"Airline A: Your price is below marginal cost! Adjusted to marginal cost ({marginal_cost}).")
        price_A = marginal_cost
    if price_B < marginal_cost:
        print(f"Airline B: Your price is below marginal cost! Adjusted to marginal cost ({marginal_cost}).")
        price_B = marginal_cost
    
    # Store results
    prices_A.append(price_A)
    prices_B.append(price_B)
    profits_A.append(profit_A)
    profits_B.append(profit_B)

    # Print results for the current round
    print(f"Price Airline A: {price_A}")
    print(f"Profit Airline A: {profit_A}")
    print(f"Price Airline B: {price_B}")
    print(f"Profit Airline B: {profit_B}\n")

# Plotting the results after all rounds are completed
rounds = list(range(1, n + 1))

plt.figure(figsize=(12, 6))

plt.plot(rounds, prices_A, label='Airline A Price', marker='o')
plt.plot(rounds, prices_B, label='Airline B Price', marker='o')
plt.plot(rounds, profits_A, label='Airline A Profit', linestyle='--', marker='x')
plt.plot(rounds, profits_B, label='Airline B Profit', linestyle='--', marker='x')

plt.xlabel('Round')
plt.ylabel('Value')
plt.title('Airline Ticket Pricing and Profits with Player Input')
plt.legend()
plt.grid(True)
plt.show()