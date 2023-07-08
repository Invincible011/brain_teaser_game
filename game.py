import random as rd
from datetime import datetime as timer
import os

class Game:

    score = 0
    
    def __init__(self):
        self.counter = 0
    
    @staticmethod
    def clean():
        os.system('cls')

    def startup_message(self):
        self.clean()
        return "\t\t\t\t***W E L C O M E  T O  B R A I N  T E A S E R  G A M E***\n\n"

    def user_details(self):
        self.time = int(timer.now().strftime("%H"))
        self.username = input("Enter your Username? ").upper()


    # Username and Score should be displayed at the top of the Game for easy visibility
    def startup_info(self):
        print(self.startup_message())
        print(self.user_details())
        
        if self.time < 12:
            return f'\n\t\t\t\tGood Morning: {self.username}'      
        elif self.time <= 15:
            return f'\n\t\t\t\tGood Afternoon: {self.username}'
        else: 
            return f'\n\t\t\t\tGood Evening: {self.username}'
    
    def _initialise_timer(self):
        pass

    def validate_user(self):
        # This validate if the user has done the brain teaser game in the last 30 days or earlier
        pass

    def display_score(self):
        return f"Your Score is {self.score}"


    def close(self):
        pass  


class Stage(Game):

    userinput = 0
    def __init__(self):
        super().__init__()
        self.level = None

    def level_1(self):
        print(self.startup_info())
        print("\n\t\t\t\t\t\tW e l c o m e  t o  L e v e l  1\n")
        num_of_quest = [1,2,3,4,5,6,7,8,9,10]
        for num_of_ques in num_of_quest:
            num_1 = rd.randint(1, 15)
            num_2 = rd.randint(1, 5)
            operator = rd.randint(1, 5)
            
            match operator:
                case 1:
                    answer = num_1 + num_2
                    self.userinput = int(input("Question_{2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())


                case 2:
                    answer = num_1 - num_2
                    self.userinput = int(input("Question_{2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())
                case 3:
                    answer = num_1 * num_2
                    self.userinput = int(input("Question_{2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())

                case 4:
                    answer = num_1 ** num_2
                    self.userinput = int(input("Question_{2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())

                case 5:
                    answer = num_1 / num_2
                    self.userinput = int(input("Question_{2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                    if type(answer) == float:
                        float(self.userinput)
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())

            if num_of_ques == 10:
                self.level_2()

    def level_2(self):
        print(f"\t\t\t\t A T  T H E  E N D  O F  L E V E L  1,  Y O U R  S C O R E  I S:  {self.score}")
        print("\t\t\t\t\t\tW e l c o m e  t o  L e v e l  2\n")
        num_of_quest = [1,2,3,4,5,6,7,8,9,10]
        for num_of_ques in num_of_quest:
            num_1 = rd.randint(1, 20)
            num_2 = rd.randint(3, 8)
            operator = rd.randint(1, 5)
            
            match operator:
                case 1:
                    answer = num_1 + num_2
                    self.userinput = int(input("Question_{2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())


                case 2:
                    answer = num_1 - num_2
                    self.userinput = int(input("Question_{2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())
                case 3:
                    answer = num_1 * num_2
                    self.userinput = int(input("Question_{2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())

                case 4:
                    answer = num_1 ** num_2
                    self.userinput = int(input("Question_{2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())

                case 5:
                    answer = num_1 / num_2
                    self.userinput = int(input("Question_{2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                    if type(answer) == float:
                        float(self.userinput)
                    if self.userinput == answer:
                        self.score += 10
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())

            if num_of_ques == 10:
                self.level_3()

    def level_3(self):
        pass

    def level_4(self):
        pass

    def level_5(self):
        pass


if __name__ == "__main__":
    gm = Stage()
    gm.level_1()
