import random as rd

def level_5(self):
    print(f"\t\t\t\t A T  T H E  E N D  O F  M E D I U M  D I F F I C U L T Y  L E V E L  {self.level},  Y O U R  S C O R E  I S:  {self.score}")
    self.level = int(input("\t\t\t\t\t<<<<< Press 5 to start  L E V E L  5?  >>>>>\n"))
    if self.level == 5:
        print("\n\t\t\t\t\t\tW e l c o m e  t o  M E D I U M  D I F F I C U L T Y  L e v e l  {}\n".format(self.level))
        for num_of_ques in range(1, 11):
            num_1 = rd.randint(15, 28)
            num_2 = rd.randint(6, 12)
            operator = rd.randint(1, 5)
            
            match operator:
                case 1:
                    answer = num_1 + num_2
                    self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())

                case 2:
                    answer = num_1 - num_2
                    self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())

                case 3:
                    answer = num_1 * num_2
                    self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())

                case 4:
                    answer = num_1 ** num_2
                    self.userinput = int(input("Question {2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())

                case 5:
                    answer = num_1 / num_2
                    self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())
        
            if num_of_ques == 20:
                print(f"A T  T H E  E N D  O F  M E D I U M  D I F F I C U L T Y  L E V E L  {self.level}\n{self.display_score()}")
                self.level = int(input("\t\t\t\t\t<<<<< P r e s s  1  t o  c o n t i n u e  p l a y i n g >>>>>\n"))
                if self.level == 1:
                    self.hard_level_1()