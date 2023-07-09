import random as rd

def level_2(self):
    print(f"\t\t\t\t A T  T H E  E N D  O F  L E V E L  1,  Y O U R  S C O R E  I S:  {self.score}")
    self.level = int(input("\t\t\t\t\t<<<<< Press 2 to start the level 2?  >>>>>"))
    while self.level == 2:
        print("\t\t\t\t\t\tW e l c o m e  t o  L e v e l  2\n")
        for num_of_ques in self.num_of_quest:
            num_1 = rd.randint(1, 15)
            num_2 = rd.randint(2, 5)
            operator = rd.randint(1, 5)
            
            match operator:
                case 1:
                    answer = num_1 + num_2
                    self.userinput = int(input("Question_{2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 3
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())


                case 2:
                    answer = num_1 - num_2
                    self.userinput = int(input("Question_{2}: {0} - {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 3
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())
                case 3:
                    answer = num_1 * num_2
                    self.userinput = int(input("Question_{2}: {0} * {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nTHE  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 3
                        print(f"\nTHE  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS {answer}\n")
                        print(self.display_score())

            if num_of_ques == 10:
                self.level_3()
