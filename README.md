Competitive Market Simulations: Cournot and Bertrand Models

This repository contains Python implementations of two classic economic models in game theory: the Cournot model applied to Internet Service Providers (ISPs) and the Bertrand model applied to airline ticket pricing. These simulations allow users to explore how firms compete in quantity and price, respectively, and how these strategies affect market prices and profits.

Table of Contents

	•	Introduction
	•	Models
	•	ISP Competition - Cournot Model
	•	Airline Ticket Pricing - Bertrand Model
	•	How to Play
	•	ISP Cournot Model
	•	Airline Bertrand Model
	•	Dependencies
	•	Running the Simulations

Introduction

In economic theory, Cournot and Bertrand models describe how firms interact in markets where they compete on quantity and price, respectively. This repository provides interactive simulations where players (representing firms) can input their strategies and observe the outcomes in terms of market prices and profits.

Models

ISP Competition - Cournot Model

In this simulation, two Internet Service Providers (ISPs) compete by deciding the quantity of broadband packages to offer in the market. The market price is determined by the total quantity offered by both ISPs, and each ISP earns a profit based on the market price minus its cost.

Model Dynamics:

	•	ISPs decide on the quantity of broadband packages to sell.
	•	The market price is inversely related to the total quantity offered by both ISPs.
	•	Each ISP’s profit is calculated based on the market price and its cost of providing the service.

Airline Ticket Pricing - Bertrand Model

In this simulation, two airlines compete by setting prices for tickets on the same flight route. Customers choose the airline offering the lower price, and the airline’s profit is the difference between its price and the marginal cost of providing the service.

Model Dynamics:

	•	Airlines set ticket prices independently.
	•	The airline with the lower price captures the entire market.
	•	If both airlines set the same price, they split the market equally.
	•	Profits depend on the price set and the marginal cost.

How to Play

ISP Cournot Model

	1.	Input the Number of Rounds: Decide how many rounds of competition you want to simulate (default is 20).
	2.	Set Quantities: In each round, both ISPs input the quantity of broadband packages they wish to offer.
	3.	View Results: After each round, the market price and profits for both ISPs are displayed.
	4.	Final Analysis: After all rounds, a plot shows the profits of both ISPs over the rounds, as well as the market price trend.

Airline Bertrand Model

	1.	Input the Number of Rounds: Decide how many rounds of price competition you want to simulate (default is 5).
	2.	Set Prices: In each round, both airlines input their ticket prices.
	3.	View Results: After each round, the profits for both airlines are displayed.
	4.	Final Analysis: After all rounds, a plot shows the prices set by both airlines and their corresponding profits.

Dependencies

	•	Python 3.x
	•	Matplotlib (pip install matplotlib)
