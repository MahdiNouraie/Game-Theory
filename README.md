
# CEO Selection using Game Theory and Nash Equilibrium

This project is a simulation and modeling of a game theory problem, where a company is trying to select a new CEO from the board of directors. The goal is to find the Nash Equilibrium of the game and determine the winner(s) based on their strategies and values.

## Problem Statement

The problem is to select a new CEO from a board of directors consisting of three members. Each member has a different value associated with them, representing their level of expertise and influence in the company. The values range from 1 to 3, with 3 being the highest.

The three members of the board can choose between two strategies: "V" for voting for themselves and "C" for cooperating with the other members. The members submit their choices simultaneously, and the new CEO is selected based on the following rules:

- If all three members vote for themselves, the member with the highest value becomes the CEO.
- If only two members vote for themselves, the member with the highest value among them becomes the CEO.
- If only one member votes for themselves, they become the CEO.
- If no one votes for themselves, the member with the highest value becomes the CEO.

The goal is to find the Nash Equilibrium of the game, where no player can improve their outcome by unilaterally changing their strategy, and determine the winner(s) based on their strategies and values.

## Solution

The solution to the problem involves simulating the game and calculating the Nash Equilibrium using Python. The program uses nested loops to iterate over all possible values and strategies combinations and calculate the payoffs for each player.

The program first calculates the payoff matrix for each player based on the game rules. It then uses the payoff matrix to calculate the Nash Equilibrium of the game using the Lemke-Howson algorithm.

Finally, the program determines the winner(s) of the game based on the strategies and values calculated earlier. If the conditions for a Nash Equilibrium are met, the program appends the corresponding player's name to the Winners list. If there is a tie, the program appends both players' names to the Winners list.

## Code

The code for the program is provided in the file ceo_selection.py. It consists of three main parts:

- The generate_strategies function generates all possible strategies for each player.
- The generate_values function generates all possible values for each player.
- The ceo_selection function simulates the game, calculates the Nash Equilibrium, and determines the winner(s) based on the strategies and values.

To run the program, simply call the ceo_selection function with the desired values for each player:

ceo_selection(1, 2, 3, 1, 2, 3, 1, 2, 3)


This will simulate the game with the following values and strategies:

- Player 1: Value 1, Strategy "V"
- Player 2: Value 2, Strategy "V"
- Player 3: Value 3, Strategy "V"

The program will output the following:

Nash Equilibrium: (['C', 'C', 'V'], [2, 2, 3])
Winners: [['player1 and player2']]


This indicates that the Nash Equilibrium of the game is when all players choose the "C" strategy, and the values for each player are 2, 2, and 3. The winner(s) of the game are player 1 and player 2.

## Conclusion

This project demonstrates how game theory and Nash Equilibrium can be used to solve real-world problems, such as selecting a new CEO from a board of directors. The program provides a flexible and efficient way to simulate the game and calculate the Nash Equilibrium, making it a valuable tool for decision-making in the business world.
