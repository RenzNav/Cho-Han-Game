# Author: Clarence Navarro

# Date: 26/11/2024

# Description: A Cho-Han game program where players bet on the outcome of two dice rolls—cho (even) or han (odd). 
# Players place bets, choose their prediction, and win or lose based on the dice sum. The program handles player balance, 
# bet validation, dice rolling, and displays results for the single round simulated.


import random  # For getting the random integers for the die

# Task 1
class GameParticipant(object):
    """Class represents a participant of the game"""

    def __init__(self, name="", balance=0.00, bet=0.00):
        self.name = name
        self.balance = balance
        self.bet = bet


# Task 2
class Player(GameParticipant):
    """Class inherited from GameParticipant and allows player to place bets"""

    def __init__(self, name, balance, bet, odd_even=True):
        GameParticipant.__init__(self, name, balance, bet)
        self.odd_even = odd_even  # Keeps track of player's choice. True = even, False = odd

    def place_bet(self):
        """Allows player to place a bet"""
        print(f"Hello {self.name}!")
        print(f"Your Balance: ${self.balance:.2f}\n")

        while True:  # Ensures player does not make a bet higher than their balance
            user_bet = float(input("How much do you wish to bet: "))  # Prompt user to enter bet

            if self.balance - user_bet < 0:  # Indicates person has made a bet bigger than their balance
                print("You have bet more than you can afford! Lower your bet.\n")
            else:
                self.bet = user_bet
                self.balance -= self.bet  # Deducting bet off balance

                print(f"You have bet ${self.bet:.2f}")

                # Asking user what they are betting for
                while True:  # Ensures user enters 1 or 0 only
                    choice = int(input("Cho (1) or Han (0): "))
                    if choice == 1:
                        self.odd_even = True
                        break
                    elif choice == 0:
                        self.odd_even = False
                        break
                    else:
                        print("You have chosen an invalid option. Choose Again.\n")

                break  # Gets out of while loop

    def check_outcome(self, result):
        """Checks whether the player wins or loses"""

        # result = True indicates "cho" (even) and result = False indicates "han" (odd)
        if result is True and self.odd_even is True:  # If player chooses cho and it is cho
            print("You have won the bet.")
            self.balance += self.bet * 2  # Adding winnings to balance
            print(f"You win ${self.bet * 2:.2f}! Your balance is now ${self.balance:.2f}\n")

        elif result is False and self.odd_even is False:  # If player chooses han and it is han
            print("You have won the bet.")
            self.balance += self.bet * 2  # Adding winnings to balance
            print(f"You win ${self.bet * 2:.2f}! Your balance is now ${self.balance:.2f}\n")

        else:  # Player chooses the wrong bet
            print(f"You have guessed wrong! Your balance is now ${self.balance:.2f}\n")


# Task 3
class CupClass(object):
    """Class represents the two six-sided dice in Cho-Han"""

    def __init__(self, dice1=0, dice2=0):
        self.dice1 = dice1
        self.dice2 = dice2

    def roll_die(self):
        """Simulates the two dice rolling and returns True if cho and False if han"""

        print("Rolling the die...")

        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)

        print(f"Dice 1: {self.dice1}\nDice 2: {self.dice2}\n")

        # Determining the outcome
        if (self.dice1 + self.dice2) % 2 == 0:  # Modular operator to determine outcome
            print(f"Cho! The sum {self.dice1 + self.dice2} is even.\n")
            return True  # Returns boolean for the check_outcome() function in Player
        else:
            print(f"Han! The sum {self.dice1 + self.dice2} is odd.\n")
            return False  # Returns boolean for the check_outcome() function in Player


# Main Scope
# Task 4 - Simulation

# Creating the instances
player1 = Player("Clarence", 100, 0.00, False)
DiceCup = CupClass(0, 0)

# Single round simulation
player1.place_bet()  # Prompt player for a bet
game_result = DiceCup.roll_die()  # Roll the dice and get the outcome
player1.check_outcome(game_result)  # Check if player wins or loses
