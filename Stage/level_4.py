import random as rd

def level_4(self):
    print(f"\t\t\t\t A T  T H E  E N D  O F  L E V E L  3,  Y O U R  S C O R E  I S:  {self.score}")
    self.level = int(input("\t\t\t\t\t<<<<< Press 4 to start level 4?  >>>>>\n"))
    while self.level == 4:
        print("\n\t\t\t\t\t\tW e l c o m e  t o  L e v e 4  1\n")
        for num_of_ques in range(1, 11):
            num_1 = rd.randint(15, 20)
            num_2 = rd.randint(7, 9)
            operator = rd.randint(1, 5)
            
            match operator:
                case 1:
                    answer = num_1 + num_2
                    self.userinput = int(input("Question_{2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 4
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS = {answer}\n")
                        print(self.display_score())

                case 2:
                    answer = num_1 - num_2
                    self.userinput = int(input("Question_{2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 4
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS = {answer}\n")
                        print(self.display_score())

                case 3:
                    answer = num_1 * num_2
                    self.userinput = int(input("Question_{2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 4
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS = {answer}\n")
                        print(self.display_score())

                case 4:
                    answer = num_1 ** num_2
                    self.userinput = int(input("Question_{2}: {0} ^ {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 4
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS = {answer}\n")
                        print(self.display_score())

                case 5:
                    answer = num_1 / num_2
                    self.userinput = float(input("Question_{2}: {0} / {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 10
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 5
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS = {answer}\n")
                        print(self.display_score())
        
            if num_of_ques == 10:
                self.level_4()