import os
import random as rd
from datetime import datetime as timer
from typing import Any


# This is a brain teaser game


class Game:
    def __init__(
            self,
            userinput = '',
            score = 0,
            counter = 0,
            level = 0,
            ):
        self.username = userinput
        self.score = score
        self.counter = counter
        self.level = level
        self.time = int(timer.now().strftime("%H"))
    
    @staticmethod
    def clean():
        os.system('cls')

    def initialise(self):
        self.clean()
        return "\t\t\t\t***W E L C O M E  T O  B R A I N  T E A S E R  G A M E***\n\n"

    def user_details(self):
        self.username = input("Enter your Username? ").upper()
        if self.username == "":
            self.username = "USER"

    # Username and Score should be displayed at the top of the Game for easy visibility
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


class Stage(Game):
    def __init__(
            self,
            username = '',
            score = 0,
            counter = 0,
            answer = 0
            ):
        
        super().__init__(username, score, counter)
        self.answer = answer
        self.action = 0

    # Score increment and decrement functions for reuseable.
    def decrement_score_by_3(self):
        self.score -= 3
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(self.display_score())

    def decrement_score_by_4(self):
        self.score -= 4
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(self.display_score())

    def decrement_score_by_5(self):
        self.score -= 5
        print(f"\nT H E  A N S W E R  I S  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {self.answer}\n")
        print(self.display_score())

    def increment_score_by_5(self):
        self.score += 5
        print("\nT H E  A N S W E R  I S  C O R R E C T\n")
        print(self.display_score())

    def increment_score_by_10(self):
        self.score += 10
        print("\nT H E  A N S W E R  I S  C O R R E C T\n")
        print(self.display_score())

    def difficulty(self):
        if self.action == 0:
            return "E A S Y  D I F F I C U L T Y"
        elif self.action == 1:
            return "M E D I U M  D I F F I C U L T Y"
        else:
            return "H A R D  D I F F I C U L T Y"

    def report_level(self):
        self.level = int(input(f"\n\t\t\t\t\t<<<<< Press {self.level + 1} to start the  G A M E  >>>>>\n"))
        if self.level == 1:
            print("\t\t\t\t\t H e l l o  {}".format(self.username))
            print(f"\t\t\t A T  T H E  B E G I N N I N G  O F  {self.difficulty()}  L E V E L  {self.level},  {self.display_score()}")
        else:
            if self.level > 1:
                self.level -= 1
                print(f"\t\t\t A T  T H E  E N D  O F  {self.difficulty()}  L E V E L  {self.level},  {self.display_score()}")
                self.level += 1


class Level(Stage):
    def __init__(
            self, 
            username ='', 
            score=0, 
            counter=0, 
            answer=0,
            level=0,
            action = 0
            ):
        super().__init__(username, score, counter, answer)
        self.level = level
        self.action = action

    def easy_level_1(self):
        self.level = 0
        self.score = 0
        self.show_details()
        self.report_level()
        if self.level == 1:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            # self.level = 1
            for num_of_ques in range(1, 3): # Testing Remove later and change to 10
                num_1 = rd.randint(1, 3)
                num_2 = rd.randint(1, 2)
                operator = rd.randint(1, 2)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()
                if num_of_ques == 2:
                    self.easy_level_2()
        else:
            self.level = int(input("\t\t\t\t\t<<<<< Press any key to exit or \"1\" to restart the game again?  >>>>>\n"))
            if self.level != 1:
                exit()
            else:
                self.easy_level_1()


    def easy_level_2(self):
        self.report_level()
        if self.level == 2:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(1, 5)
                num_2 = rd.randint(1, 3)
                operator = rd.randint(1, 3)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                if num_of_ques == 2:
                    self.easy_level_3()
        else:
            self.level = int(input("\t\t\t\t\t<<<<< Press any key to exit or \"1\" to restart the game again?  >>>>>\n"))
            if self.level != 1:
                exit()
            else:
                self.easy_level_1()
                

    def easy_level_3(self):
        self.report_level()
        if self.level == 3:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(1, 10)
                num_2 = rd.randint(1, 4)
                operator = rd.randint(1, 4)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 4:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()
            
                if num_of_ques == 2:
                    self.easy_level_4()
        else:
            self.level = int(input("\t\t\t\t\t<<<<< Press any key to exit or \"1\" to restart the game again?  >>>>>\n"))
            if self.level != 1:
                exit()
            else:
                self.easy_level_1()


    def easy_level_4(self):
        self.report_level()
        if self.level == 4:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(1, 15)
                num_2 = rd.randint(1, 4)
                operator = rd.randint(1, 5)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 4:
                        self.answer = num_1 ** num_2
                        self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 5:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()
            
                if num_of_ques == 2:
                    self.easy_level_5()

    def easy_level_5(self):
        self.report_level()
        if self.level == 5:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 11):
                num_1 = rd.randint(1, 11)
                num_2 = rd.randint(1, 5)
                operator = rd.randint(1, 5)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 4:
                        self.answer = num_1 ** num_2
                        self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 5:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()
            
                if num_of_ques == 2:
                    print(f"A T  T H E  E N D  O F  L E V E L  {self.level}  O F  {self.difficulty()}\n{self.display_score()}")
                    self.level = int(input("\t\t\t\t\t<<<<< P r e s s  1  t o  c o n t i n u e  p l a y i n g >>>>>\n"))
                    if self.level == 1:
                        self.level_1()

    def level_1(self):
        self.action = 1
        self.level = 0
        self.report_level()
        if self.level == 1:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(1, 10)
                num_2 = rd.randint(1, 5)
                operator = rd.randint(1, 2)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()
            
                if num_of_ques == 2:
                    self.level_2()

    def level_2(self):
        self.report_level()
        if self.level == 2:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(5, 15)
                num_2 = rd.randint(2, 6)
                operator = rd.randint(1, 3)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                if num_of_ques == 2:
                    self.level_3()

    def level_3(self):
        self.report_level()
        if self.level == 3:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(5, 20)
                num_2 = rd.randint(4, 8)
                operator = rd.randint(1, 4)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 4:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()
            
                if num_of_ques == 2:
                    self.level_4()
    def level_4(self):
        self.report_level()
        if self.level == 4:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(10, 25)
                num_2 = rd.randint(5, 10)
                operator = rd.randint(1, 5)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 4:
                        self.answer = num_1 ** num_2
                        self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 5:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()
            
                if num_of_ques == 2:
                    self.level_5()

    def level_5(self):
        self.report_level()
        if self.level == 5:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(15, 28)
                num_2 = rd.randint(6, 12)
                operator = rd.randint(1, 5)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 4:
                        self.answer = num_1 ** num_2
                        self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 5:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()
            
                if num_of_ques == 2:
                    print(f"A T  T H E  E N D  O F  {self.difficulty()}  L E V E L  {self.level}\n{self.display_score()}")
                    self.level = int(input("\t\t\t\t\t<<<<< P r e s s  1  t o  c o n t i n u e  p l a y i n g >>>>>\n"))
                    if self.level == 1:
                        self.hard_level_1()

    def hard_level_1(self):
        self.action = 2
        self.level = 0
        self.report_level()
        if self.level == 1:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(1, 10)
                num_2 = rd.randint(1, 5)
                operator = rd.randint(1, 2)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()
            
                if num_of_ques == 2:
                    self.hard_level_2()

    def hard_level_2(self):
        self.report_level()
        if self.level == 2:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(5, 15)
                num_2 = rd.randint(2, 6)
                operator = rd.randint(1, 3)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                if num_of_ques == 2:
                    self.hard_level_3()

    def hard_level_3(self):
        self.report_level()
        if self.level == 3:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(5, 20)
                num_2 = rd.randint(4, 8)
                operator = rd.randint(1, 4)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()

                    case 4:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_3()
            
                if num_of_ques == 2:
                    self.hard_level_4()

    def hard_level_4(self):
        self.report_level()
        if self.level == 4:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(10, 25)
                num_2 = rd.randint(5, 10)
                operator = rd.randint(1, 5)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 4:
                        self.answer = num_1 ** num_2
                        self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_5()
                        else:
                            self.decrement_score_by_4()

                    case 5:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()
            
                if num_of_ques == 2:
                    self.hard_level_5()

    def hard_level_5(self):
        self.report_level()
        if self.level == 5:
            print("\n\t\t\t\t\t\tW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 3):
                num_1 = rd.randint(15, 28)
                num_2 = rd.randint(6, 12)
                operator = rd.randint(1, 5)
                
                match operator:
                    case 1:
                        self.answer = num_1 + num_2
                        self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 2:
                        self.answer = num_1 - num_2
                        self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 3:
                        self.answer = num_1 * num_2
                        self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 4:
                        self.answer = num_1 ** num_2
                        self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()

                    case 5:
                        self.answer = num_1 / num_2
                        self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                        if self.userinput == self.answer:
                            self.increment_score_by_10()
                        else:
                            self.decrement_score_by_5()
            
                if num_of_ques == 2:
                    print(f"A T  T H E  E N D  O F  {self.difficulty()}  L E V E L  {self.level}\n{self.display_score()}")
                    self.level = int(input("\t\t\t\t\t<<<<< Do you want to restart the game? if YES press 1 otherwise press any key to exit >>>>>\n"))
                    if self.level == 1:
                        self.easy_level_1()
                    else:
                        exit()


if __name__ == "__main__":
    gm = Level()
    gm.easy_level_1()