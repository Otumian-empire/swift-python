# Exercise 20 c (continuation of OOP concepts)

## Practical

> _We confidently believe that at this stage, with patience, persistence and clear mind and an intention to solve a problem, you can do so many things, now. Surely some problems will be challenging but through this difficulty, you become better._

Fixed this code. Do not panic, it is easier than you may sweat. Some little assistance.

- try to understand what every component (method) does.
  - copy the method somewhere and run it or comment some part of it out
  - or just comment the others out and run it
- run the code multiple times and write down something. Try to trace the execution of the code.
- break it and see what happens by stabbing it with various input types
  - jot something down - you are becoming a hacker.
  - stabbing means, pass some data to the method or attribute directly.
    So if there is an input, you provide the input directly.
- try negative values too - just break it and fix it
- add comments where you think necessary - try commenting on the code as you may come back in a week or more time.

> Download practical file [here][ex20x_practicals]

```Python
import random
# we shall discuss the line above in the next exercise

# description: This is a simple text-based console gambling game.
# Give the user a name and initial cash (default, $1000)
# Ask the user for their name later in the game when the user is
# making more money - if the current cash is 5 times the initial
# Randomly generate a number in a range and prompt self to
# guess the number
# if user guess is right, double bet and add to cash
# else, double and subtract from cash
# bet is in folds of $100

# That's it... Thanks


class Game:

    def __init__(self, username, cash=1000, bet=0):
        self.username = username
        self.cash = cash
        self.bet = bet

    # returns user details
    def game_info(self):
        strinfo = f"You have ${self.cash} in your account... "
        strinfo += f"and you've placed a bet of ${self.bet}... "
        strinfo += f"Good luck ${self.name}!"

        return strinfo

    # returns game details
    def player_info(self):
        strinfo = f"Hello {self.username}, you have "
        strinfo += f"${self.cash} is your account..."

        return strinfo

    # change the users name amids gaming
    # this function has not been used
    def change_username(self, newname):
        self.username = newname

    # makes sure that the bet is in a fold of 100s
    # bet must be not be zero or less than zero
    # before allowing bet method
    def wager(self, bet):

        try:
            if bet > 0 and bet % 100 == 0:
                bet = int(bet)

                if bet <= self.cash:
                    self.bet = bet
                    self.cash -= self.bet
                else:
                    print(f"You only have ${self.cash} in your account...")

                    if self.cash > 100:
                        self.bet = 100
                        print(
                            f"For the love of the game, by default your bet is ${self.bet}")

            else:
                # set the bet to 0 since the user didn't choose
                # a bet other than a multiple of 100
                print("Your wager is as tinny as your broke bank...")
                print("Let's just have some fun and call it a day...")
                self.bet = 0

        except ValueError as e:
            print(f"You have to use money...")
            print(e)

            # set a bet again
            bet = int(
                input("place your bet in a fold of hundreds [100, 200, 300, ...]: "))
            # call wager again and pass it, bet
            self.wager(bet)

    # the main function
    def start_game(self):
        # print user info
        print(self.player_info())

        end_game = "yes"

        while end_game != "no":

            # catch non numberic inputs
            try:
                # set a bet
                bet = int(
                    input("place your bet in a fold of hundreds [100, 200, 300, ...]: "))
                self.wager(bet)

                # print game info
                print(self.game_info())

                # checking if the bet is greater than half of user player cash
                if self.bet >= 0.5 * self.cash:
                    print("You are a man who admires risks, we love you..")

                # this is where the random numbers are generated
                # alter this to suit for a different functionality
                start, end = 0, 2

                # on this like we use a component from the import
                random_number = random.randint(start, end + 1)

                guess = int(input(
                    f"{self.username}, be smart and pick your lucky number between {start} and {end}: "))

                if random_number == guess:
                    self.bet *= 2
                    self.cash += self.bet

                    # print game info
                    print(self.game_info())
                    print(
                        f"{self.username}, you won this time... you now have: {self.cash}")
                else:
                    self.bet = 0

                    # print game info
                    print("you loss..")
                    print(self.game_info())

                if self.cash < 100:
                    print(
                        "Man you have no cash... You better walk away.. else I'd mob the dirty floor with your damn broke face..")

                    # print user info
                    print(self.game_info())
                    end_game = "no"
                else:
                    end_game = input(
                        "Do you want to keep playing, (yes or no)? ").lower()

            except ValueError as e:
                print(
                    "Hmm... I bet you, start with a hundred and I will double it also...")

        print(self.game_info())


# create an instance object of the Game class and call the start method
user = Game("f3erQ6$_", 1000)
user.start_game()

```

## Summary

- Inheritance is an OOP Concept
- A child class inherits from a parent class
- pass the parent class as an argument to the child class
- pass multiple classes that way, for multiple inheritances
- use `super()` to access the original attributes and methods of the parent class

#

[ex20x_practicals]: https://gist.github.com/Otumian-empire/ebbea0703bdf105ce1ae1ffe0f72d60a.
