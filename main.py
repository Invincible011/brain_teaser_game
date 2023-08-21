import os
from datetime import datetime as timer
import random as rd
import time

# This is a brain teaser game
# Check "README.md" to know more about the full functionalities.
class Optimizer:
    def __init__(
            self,
            userinput = '',
            ):
        self.username = userinput
        self.time = int(timer.now().strftime("%H"))
    
    @staticmethod
    def clean():
        os.system('cls')

    def initialise(self):
        self.clean()
        return "\t\t\t\t\t< < < W E L C O M E  T O  B R A I N  T E A S E R  G A M E > > >\n\n"

    def user_details(self):
        self.username = input("Enter your Username? ").upper()
        if self.username == "":
            self.username = "USER"

    def startup_info(self):
        if self.time < 12:
            return f'\n\t\t\t\t\t\tG o o d  M o r n i n g: "{self.username}"'
        elif self.time <= 14:
            return f'\n\t\t\t\t\t\tG o o d  A f t e r n o o n: "{self.username}"'
        else: 
            return f'\n\t\t\t\t\t\tG o o d  E v e n i n g: "{self.username}"'

    def show_details(self):
        print(self.initialise())
        self.user_details()
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

    # Score increment and decrement.
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

    # implement score increment and decrement
    def increment(self):
        if self.action <= self.initial:
            self.increment_score_by_5()
        else:
            self.increment_score_by_10()

    def decrement(self):
        if self.action == 0:
            self.decrement_score_by_3()
        elif self.action == self.initial:
            self.decrement_score_by_4()
        else:
            self.decrement_score_by_5()

    # Return the Level Difficulty base on the action mode
    def difficulty(self):
        if self.action == self.start:
            return "E A S Y  D I F F I C U L T Y"
        elif self.action == self.initial:
            return "M E D I U M  D I F F I C U L T Y"
        else:
            return "H A R D  D I F F I C U L T Y"

    # Recursive call on level for each action {0: Easy, 1: Medium, 2: Hard}
    def report_level(self):
        if self.correct >= 5:
            print(f"A T  T H E  E N D  O F  {self.difficulty()}  L E V E L  {self.level}")
            print(f"You answered {self.correct} questions correctly")
            # print(f"You answered {self.incorrect} questions in-correctly")
            print(f"Wait for 5 secs to move to Level {self.level+1}...")
            time.sleep(5)
        self.level = int(input(f"\n\t\t\t\t\t<<<<< Press {self.temp_level} to start  L E V E L  {self.temp_level}  of  {self.difficulty()} >>>>>\n"))
        if self.level == 1:
            print("\t\t\t\t\t\t\t\t\t H e l l o  {}\n".format(self.username))
            print(f"\t\t\t A T  T H E  B E G I N N I N G  O F  {self.difficulty()}  L E V E L  {self.level},  {self.display_score()}")
        else:
            if self.level > 1:
                self.level -= 1
                print(f"\t\t\t A T  T H E  E N D  O F  {self.difficulty()}  L E V E L  {self.level},  {self.display_score()}")
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
        self.initial = self.start+1
        if self.correct < 5:
            # Track the recent score and store it then display the recent score if correct answer is less than 5
            if self.action == self.start and self.level == self.initial:
                self.score = self.start
                self.counter = self.start
            elif self.action >= self.initial and self.level == self.initial:
                self.counter = self.start
            elif self.action >= self.initial and self.level >= self.initial:
                # Check if the temp_score list is empty, if null; add the recent score to the list
                # else: assign the score to the first index of the temp_score list (Last_Seen)  
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
        # Check if the counter has exceeded max_count
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
                self.level = int(input("\t\t\t\t\t<<<<< P r e s s  1  t o  c o n t i n u e  p l a y i n g >>>>>\n"))
                print("\t\t\t\t\t\t\tO R")
                self.level = int(input("\t\t\t\t\t<<<<< Do you want to restart the game? if YES press 1 otherwise press any key to exit >>>>>\n"))
                if self.level == self.initial:
                    self.root_level()
                else:
                    exit()
            self.level = int(input("\t\t\t\t\t<<<<< P r e s s  1  t o  c o n t i n u e  p l a y i n g >>>>>\n"))
            if self.level == self.initial:
                self.root_level()
        else:
            self.temp_level += self.initial
            self.root_level()


class Game(Optimizer):
    def __init__(
            self, 
            username ='', 
            score = 0, 
            answer = 0,
            level = 0,
            counter = 0
            ):
        super().__init__(username)
        self.score = score
        self.answer = answer
        self.level = level
        self.counter = counter
        # Unpacking tuple
        self.start, self.end, self.action, self.correct, self.incorrect, self.temp_level  = ((0,) * 6)
        self.max_count = 50
        self.max_level = 5
        self.max_action = 3
        self.temp_score = []
        self.temp_counter = []

    def root_level(self):
        self.initial = self.start+1
        if self.level == self.start:
            # Reset Temporary Level
            self.temp_level = self.initial
            self.show_details()
        # Reset action mode
        self.reset_action()
        self.report_level()
        self.correct = self.start
        self.incorrect = self.start
        if self.level == self.temp_level:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 11): # Testing Remove from 3 to be changed to 11
                self.counter += self.initial
                if self.end == 10:
                    self.end = 0
                self.end += self.initial
                num_1 = rd.randint(self.start+self.level, (3*self.level)+self.end)
                num_2 = rd.randint(self.start+self.level, (2*self.level)+self.end)
                operator = rd.randint(self.initial, self.max_level+1)

                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        time.sleep(1)
                        try:
                            self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        except Exception:
                            raise TypeError("Try an Integer or Float number")
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()

                    case 2:
                        self.answer = num_1 - num_2
                        time.sleep(1)
                        try:
                            self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        except Exception:
                            raise TypeError("Try an Integer or Float number")
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()
                            
                    case 3:
                        self.answer = num_1 * num_2
                        time.sleep(1)
                        try:
                            self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        except Exception:
                            raise TypeError("Try an Integer or Float number")
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()

                    case 4:
                        self.answer = num_1 ** num_2
                        time.sleep(1)
                        try:
                            self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                        except TypeError:
                            raise TypeError("Try an Integer or Float number")
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()
                            
                    case 5:
                        self.answer = num_1 / num_2
                        time.sleep(1)
                        try:
                            self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        except Exception:
                            raise TypeError("Try an Integer or Float number")
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()
                    
                    case 6:
                        if num_1 > num_2:
                            temp = num_1
                            num_1 = num_2
                            num_2 = temp
                        self.answer = num_2 % num_1
                        time.sleep(1)
                        # print("This returns a remainder")
                        try:
                            self.userinput = float(input("Question {2}: {0} % {1} =? ".format(num_2, num_1, num_of_ques)))
                        except Exception:
                            raise TypeError("Try an Integer or Float number")
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()

                # For debugging
                '''print(f"Temp_Level_Counter: {self.temp_level}")
                print(f"Counter: {self.counter}")
                print(f"Action: {self.action}")
                
                if self.correct <= self.initial:
                    print(f"You answered {self.correct} Correct answer out of 10")
                else:
                    print(f"You answered {self.correct} Correct answers out of 10")
                    
                if self.incorrect <= self.initial:
                    print(f"You answered {self.incorrect} question in-correctly")
                else:
                    print(f"You answered {self.incorrect} questions in-correctly")
                '''
                # Debugging ends here

                if num_of_ques == self.max_level*2:
                    self.temp_score.append(self.score)
                    self.temp_counter.append(self.counter)
                    if self.correct >= self.max_level:
                        self.temp_score = []
                        self.temp_counter = []
                        if len(self.temp_score) <= self.initial:
                            self.temp_score.append(self.score)
                            self.temp_counter.append(self.counter)
                    else:
                        self.score = self.temp_score[self.start]
                        self.counter = self.temp_counter[self.start]
                    self.update_level()
        else:
            self.level = int(input("\t\t\t\t\t<<<<< Press any key to exit or \"1\" to restart the game again?  >>>>>\n"))
            if self.level != self.initial:
                exit()
            else:
                self.root_level()


if __name__ == "__main__":
    gm = Game()
    gm.root_level()