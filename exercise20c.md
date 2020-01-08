# Exercise 20 c (continuation of OOP concepts)

## Practical

> *We belive that at this stage, with patiece, persistence and clear mind and intension to actually solve a problem, you can so many things, now.*

Fixed this code. Do not panic, it is actually easier than you may sweat. Some little assistance.

* try to understand what every component (method) does
* run the code multiple times and actually write down something
* break it and see what happens by stabbing it with variuos input types - jot something down - you are becomming a hacker
* try negative values too - just break it and fix it
* add comments where you think necessary

``` python
import random  
# we shall discuss the line above in the next exercise

# description: This is a simple text based console gambling game.
# Give the user a name and an initial cash (default, $1000)
# Ask the user for his name later in the game, when user is
# making more money - if the current cash is 5 time the initial
# Randomly generate a number in a range and prompt self to
# guess the number
# if user guess is right, double bet and add to cash
# else, double and subtract from cash
# bet are in folds of $100

# That's it.. Thanks

class Game:

    def __init__(self, username, cash=1000, bet=0):
        self.username = username
        self.cash = cash
        self.bet = bet

        # returns user details
    def game_info(self):
        strinfo = f"You have ${self.cash} is your asset.. "
        strinfo += f"and you've place a bet of ${self.bet}"
        strinfo += f".. Good luck"

        return strinfo

    # returns game details
    def player_info(self):
        strinfo = f"hello {self.username}, you have "
        strinfo += f"${self.cash} is your asset.."

        return strinfo

    # change the users name amids gaming
    # this function has not been used
    def change_username(self, newname):
        self.username = newname

    # makes sure that the bet is in a fold of 100
    # before allowing bet
    def wager(self, bet):

        try:
            if bet != 0 and bet % 100 == 0:
                if int(bet) < self.cash + 1:
                    self.bet = int(bet)
                    self.cash -= self.bet
                else:
                    print(f"You only have ${self.cash} in your asset..")

                    if self.cash > 100:
                        self.bet = 100
                        print(
                            f"For the love of the game, by default your bet is ${self.bet}")

            else:
                # set bet to 0 since the user didn't chose
                # a bet other than a multiple of 100
                print("Your wager is as tinny as your broke bank..")
                print("Let's just have some fun and call it a day..")
                self.bet = 0

        except ValueError as e:
            print(f"You have to use something quite monery..\n{e}")
            # set a bet again
            bet = int(
                input("place your bet in a fold of hundreds [100, 200, 300, ...]: "))
            # call wager again and pass it, bet
            self.wager(bet)

    # the main function.. Just call this function

    def start_game(self):
        # print user info
        print(self.player_info())

        end_game = "yes".lower()
        while(end_game != "no".lower()):

            # catch non numberic inputs
            try:
                # set a bet
                bet = int(
                    input("place your bet in a fold of hundreds [100, 200, 300, ...]: "))
                self.wager(bet)

                # print game info
                print(self.game_info())

                # checking if bet is greater than half of user player cash
                if self.bet >= 0.5 * self.cash:
                    print("You are a man who admires risks, we love you..")

                # this is where the random numbers are generated
                # you can alter this to suite your needa
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
                        f"{self.username}, you won this time.. your cash is : {self.cash}")
                else:
                    self.bet = 0
                    # print game info
                    print("you loss..")
                    print(self.game_info())

                if self.cash < 100:
                    print(
                        "Man you have no cash.. You better walk away.. else i'd mob the dirty floor with your damn broke face..")

                    # print user info
                    print(self.game_info())
                    end_game = "no"
                else:
                    end_game = input("Do you want to keep playing? ").lower()

            except ValueError as e:
                print("Dikward.. i bet your broke fat beefy ass you are a cash crop.. start with a hundred and I will double it in addition..")

        print(self.game_info())

# create an instance object of the Game class and call the start method
user = Game("f3erQ6$_", 1000)
user.start_game()
```

## Summary

* Inheritance is an OOP Concept
* A child class inherits from a parent class
* pass the parent class as an argument to the child class
* pass multiple classes that way, for multiple inheritance
* use `super()` to access the original attributes and methods of the parent class

