import random as rd
import time
from asset import Optimizer

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
        self.start, self.end, self.action, self.correct, self.incorrect, self.temp_level  = ((0,) * 6)
        self.max_count = 50
        self.max_level = 5
        self.max_action = 3
        self.temp_score = []
        self.temp_counter = []

    def root_level(self):
        self.initial = self.start+1
        if self.level == self.start:
            self.temp_level = self.initial
            self.show_details()
        self.reset_action()
        self.report_level()
        self.correct = self.start
        self.incorrect = self.start
        if self.level == self.temp_level:
            print("\nW e l c o m e  t o  {}  L e v e l  {}\n".format(self.difficulty(), self.level))
            for num_of_ques in range(1, 11):
                self.counter += self.initial
                if self.end == self.max_count//2 - self.max_level:
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
                            raise ValueError("Try an Integer or Float number")
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
                            raise ValueError("Try an Integer or Float number")
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
                            raise ValueError("Try an Integer or Float number")
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
                            raise ValueError("Try an Integer or Float number")
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
                            raise ValueError("Try an Integer or Float number")
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
                            raise ValueError("Try an Integer or Float number")
                        if self.userinput == self.answer:
                            self.increment()
                        else:
                            self.decrement()

                # For debugging
                '''print(f"Temp_Level_Counter: {self.temp_level}")
                print(f"Counter: {self.counter}")
                print(f"Action: {self.action}")
                print(f"End: {self.end}")
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
            self.level = int(input("Press any key to exit or \"1\" to restart the game again? \n"))
            if self.level != self.initial:
                exit()
            else:
                self.root_level()


if __name__ == "__main__":
    gm = Game()
    gm.root_level()