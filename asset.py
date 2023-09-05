import os
import time
from datetime import datetime as timer


# This is a brain teaser game
# Check "README.md" to know more about the full functionalities.

class Optimizer:
    def __init__(
            self,
            userinput = '',
            ):
        self.username = userinput
        self.time = int(timer.now().strftime("%H"))

    def initialise(self):
        os.system('cls')
        return "< < < W E L C O M E  T O  B R A I N  T E A S E R  G A M E > > >\n\n"

    def startup_info(self):
        self.username = input("Enter your Username? ").upper()
        if self.username == "":
            self.username = "USER"
        if self.time < 12:
            return f'\nG o o d  M o r n i n g: "{self.username}"'
        elif self.time <= 14:
            return f'\nG o o d  A f t e r n o o n: "{self.username}"'
        else:
            return f'\nG o o d  E v e n i n g: "{self.username}"'

    def show_details(self):
        print(self.initialise())
        print(self.startup_info())

    def display_score(self):
        return f"Y o u r  S c o r e  i s: {self.score}"

    def increment_score_by_5(self):
        self.correct += self.initial
        self.score += self.max_level
        print("\nT H E  A N S W E R  I S  C O R R E C T\n")
        print(f"{self.display_score()}\n")

    def increment_score_by_10(self):
        self.correct += self.initial
        self.score += self.max_level*2
        print("\nT H E  A N S W E R  I S  C O R R E C T\n")
        print(f"{self.display_score()}\n")

    def decrement_score_by_3(self):
        self.score -= self.max_action
        self.incorrect += self.initial
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(f"{self.display_score()}\n")

    def decrement_score_by_4(self):
        self.score -= 4
        self.incorrect += self.initial
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(f"{self.display_score()}\n")

    def decrement_score_by_5(self):
        self.score -= self.max_level
        self.incorrect += self.initial
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(f"{self.display_score()}\n")

    def increment(self):
        if self.action <= self.initial:
            self.increment_score_by_5()
        else:
            self.increment_score_by_10()

    def decrement(self):
        if self.action == self.start:
            self.decrement_score_by_3()
        elif self.action == self.initial:
            self.decrement_score_by_4()
        else:
            self.decrement_score_by_5()

    def difficulty(self):
        if self.action == self.start:
            return "E A S Y  D I F F I C U L T Y"
        elif self.action == self.initial:
            return "M E D I U M  D I F F I C U L T Y"
        else:
            return "H A R D  D I F F I C U L T Y"

    def report_level(self):
        self.max_correct_answer = int(0.2 * self.max_count / 2)
        if self.correct >= self.max_correct_answer:
            print(f"A T  T H E  E N D  O F  {self.difficulty()}  L E V E L  {self.level}")
            print(f"You answered {self.correct} questions correctly")
            # print(f"You answered {self.incorrect} questions in-correctly")
            print(f"Wait for 3 secs to move to Level {self.level+1}...")
            time.sleep(2)
        self.level = int(input(f"\nPress {self.temp_level} to start  L E V E L  {self.temp_level}  of  {self.difficulty()}\n"))
        if self.level == 1:
            while self.username == 'user'.upper() or self.username == "" :
                print("Hi  A N O N Y M O U S")
                self.username = input("What would you like to change your name to? ").upper()
            print("H e l l o  {}\n".format(self.username))
            print(f"A T  T H E  B E G I N N I N G  O F  {self.difficulty()}  L E V E L  {self.level},  {self.display_score()}")
        else:
            if self.level > 1:
                self.level -= 1
                print(f"A T  T H E  E N D  O F  {self.difficulty()}  L E V E L  {self.level},  {self.display_score()}")
                self.level += 1

    def reset_action(self):
        if self.action == self.max_action:
            self.action = 0
            self.counter = 0
            self.score = 0
            self.level = 0
            self.correct = 0
            self.incorrect = 0
    
    # AI code & check-loops
    def update_level(self):
        if self.correct < self.max_correct_answer:
            if self.action == self.start and self.level == self.initial:
                self.score = self.start
                self.counter = self.start
            elif self.action >= self.initial and self.level == self.initial:
                self.counter = self.start
            elif self.action >= self.initial and self.level >= self.initial:
                if self.temp_score == []:
                    self.temp_score.append(self.score)
                    self.temp_counter.append(self.counter)
                else:
                    self.score = self.temp_score[self.start]
                    self.counter = self.temp_counter[self.start]
            print(f"A T  T H E  E N D  O F  {self.difficulty()}  L E V E L  {self.level}")
            print(f"Your correct answer is {self.correct} but you can't proceed to the next level")
            # print(f"You answered {self.incorrect} questions in-correctly")
            print(f"Wait for 5 secs to restart {self.difficulty()} Level_{self.level} . . .")
            time.sleep(self.max_level)
            self.score
            self.correct = self.start
            self.incorrect = self.start
            self.root_level()
        if self.counter >= self.max_count:
            self.counter = self.max_count
        if self.counter == self.max_count and self.temp_level == self.max_level:
            self.correct = self.start
            self.temp_level = self.initial
            self.counter = self.start
            print(f"A T  T H E  E N D  O F  L E V E L  {self.level}  O F  {self.difficulty()}\n{self.display_score()}")
            self.action += 1
            if self.action >= self.max_action:
                self.action = self.max_action
            if self.action == self.max_action:
                self.level = int(input("P r e s s  1  t o  c o n t i n u e  p l a y i n g >>> \n"))
                print("O R")
                self.level = int(input("Do you want to restart the game? \nIf YES press 1 otherwise press any key to exit >>> "))
                if self.level == self.initial:
                    self.root_level()
                else:
                    exit()
            self.level = int(input("P r e s s  1  t o  c o n t i n u e  p l a y i n g >>> \n"))
            if self.level == self.initial:
                self.root_level()
        else:
            self.temp_level += self.initial
            self.root_level()