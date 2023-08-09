import random as rd
from datetime import datetime as timer
import time
import os


# This is a brain teaser game
class Game:
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
        elif self.time <= 15:
            return f'\n\t\t\t\t\t\tG o o d  A f t e r n o o n: "{self.username}"'
        else: 
            return f'\n\t\t\t\t\t\tG o o d  E v e n i n g: "{self.username}"'

    def show_details(self):
        print(self.initialise())
        self.user_details()
        print(self.startup_info())

    def display_score(self):
        return f"Y o u r  S c o r e  i s: {self.score}"


class Optimizer(Game):
    def __init__(
            self,
            userinput = '',
            score = 0,
            answer = 0
            ):
        
        super().__init__(userinput)
        self.score = score
        self.answer = answer
        self.action = 0
        self.temp_level = 0

        # To be used for tracking the scores
        # self.correct = 0
        # self.incorrect = 0

    def increment_score_by_5(self):
        self.score += 5
        self.correct += 1
        print("\nT H E  A N S W E R  I S  C O R R E C T\n")
        print(self.display_score())

    def increment_score_by_10(self):
        self.score += 10
        self.correct += 1
        print("\nT H E  A N S W E R  I S  C O R R E C T\n")
        print(self.display_score())

    # Score increment and decrement.
    def decrement_score_by_3(self):
        self.score -= 3
        self.incorrect -= 1
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(self.display_score())

    def decrement_score_by_4(self):
        self.score -= 4
        self.incorrect -= 1
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(self.display_score())

    def decrement_score_by_5(self):
        self.score -= 5
        self.incorrect -= 1
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(self.display_score())

    # implement score increment and decrement
    def increment(self):
        if self.action == 0 or self.action == 1:
            self.increment_score_by_5()
        else:
            self.increment_score_by_10()

    def decrement(self):
        if self.action == 0:
            self.decrement_score_by_3()
        elif self.action == 1:
            self.decrement_score_by_4()
        else:
            self.decrement_score_by_5()

    # Return the Level Difficulty based on the action mode
    def difficulty(self):
        if self.action == 0:
            return "E A S Y  D I F F I C U L T Y"
        elif self.action == 1:
            return "M E D I U M  D I F F I C U L T Y"
        else:
            return "H A R D  D I F F I C U L T Y"

    # Recursive call on level for each action {0: Easy, 1: Medium, 2: Hard}
    def report_level(self):
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
        if self.action == 3:
            self.reset()
    
    def reset(self):
        self.action = 0
        self.counter = 0
        self.score = 0
        self.level = 0
        self.correct = 0
        self.incorrect = 0
    
    def update_level(self):
        if self.counter == 50 and self.temp_level == 5:
            self.correct = 0
            self.incorrect = 0
            self.temp_level = 1
            self.counter = 0
            print(f"A T  T H E  E N D  O F  L E V E L  {self.level}  O F  {self.difficulty()}\n{self.display_score()}")
            self.action += 1
            if self.action >= 3:
                self.action = 3
                # Debugging
                # print(f"Action: {self.action}")
            if self.action == 3:
                self.level = int(input("\t\t\t\t\t<<<<< P r e s s  1  t o  c o n t i n u e  p l a y i n g >>>>>\n"))
                print("\t\t\t\t\t\t\tO R")
                self.level = int(input("\t\t\t\t\t<<<<< Do you want to restart the game? if YES press 1 otherwise press any key to exit >>>>>\n"))
                if self.level == 1:
                    self.root_level()
                else:
                    exit()
            self.level = int(input("\t\t\t\t\t<<<<< P r e s s  1  t o  c o n t i n u e  p l a y i n g >>>>>\n"))
            if self.level == 1:
                self.root_level()
        else:
            self.temp_level += 1
            self.root_level()

    def kill(self):
        exit()


class Level(Optimizer):
    def __init__(
            self, 
            username ='', 
            score = 0, 
            answer = 0,
            level = 0,
            counter = 0
            ):
        super().__init__(username, score, answer)
        self.level = level
        self.counter = counter
        self.start = 0
        self.end = 0
        self.correct = 0
        self.incorrect = 0

    def root_level(self):
        if self.level == 0:
            # Reset Temporary Level
            self.temp_level = 1
            self.show_details()
        # Reset action mode when level_end = hard
        self.reset_action()
        self.report_level()
        if self.level == self.temp_level:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 11): # Testing Remove from 3 to be changed to 11
                self.counter += 1
                # print(f"Temp__Level_Counter: {self.temp_level}")
                # print(f"Counter: {self.counter}")
                if self.end == 10:
                    self.end = 0
                self.end += 1
                num_1 = rd.randint(self.start+self.level, (3*self.level)+self.end)
                num_2 = rd.randint(self.start+self.level, (2*self.level)+self.end)
                operator = rd.randint(1, 6)

                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()
                            
                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()

                    case 4:
                        self.answer = num_1 ** num_2
                        self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()
                            
                    case 5:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
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
                        # print("This returns a remainder")
                        self.userinput = float(input("Question {2}: {0} % {1} =? ".format(num_2, num_1, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()

                if num_of_ques == 10:
                    self.update_level()

        else:
            self.level = int(input("\t\t\t\t\t<<<<< Press any key to exit or \"1\" to restart the game again?  >>>>>\n"))
            if self.level != 1:
                self.kill()
            else:
                self.root_level()

    
if __name__ == "__main__":
    gm = Level()
    gm.root_level()