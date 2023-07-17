import random as rd

def easy_level_3(self):
    print(f"\t\t\t\t A T  T H E  E N D  O F  E A S Y  D I F F I C U L T Y  L E V E L  {self.level},  Y O U R  S C O R E  I S:  {self.score}")
    self.level = int(input("\t\t\t\t\t<<<<< Press 3 to start  L E V E L  3?  >>>>>\n"))
    if self.level == 3:
        print("\n\t\t\t\t\t\tW e l c o m e  t o  E A S Y  D I F F I C U L T Y  L e v e l  {}\n".format(self.level))
        for num_of_ques in range(1, 11):
            num_1 = rd.randint(1, 10)
            num_2 = rd.randint(1, 4)
            operator = rd.randint(1, 4)
            
            match operator:
                case 1:
                    answer = num_1 + num_2
                    self.userinput = int(input("Question {2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 3
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())

                case 2:
                    answer = num_1 - num_2
                    self.userinput = int(input("Question {2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 3
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())

                case 3:
                    answer = num_1 * num_2
                    self.userinput = int(input("Question {2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 3
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())

                case 4:
                    answer = num_1 / num_2
                    self.userinput = float(input("Question {2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 3
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nT H E  C O R R E C T  A N S W E R  I S = {answer}\n")
                        print(self.display_score())
        
            if num_of_ques == 10:
                self.easy_level_4()
