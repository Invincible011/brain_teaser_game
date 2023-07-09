import random as rd

def level_1(self):
    self.validate_user()
    print(f"\t\t\t A T  T H E  B E G I N N I N G  O F  L E V E L  1,  Y O U R  S C O R E  I S:  {self.score}")
    self.level = int(input("\n\t\t\t\t\t<<<<< Press 1 to start the  G A M E?  >>>>>\n"))
    while self.level == 1:
        print("\n\t\t\t\t\t\tW e l c o m e  t o  L e v e l  1\n")
        for num_of_ques in range(1, 11):
            num_1 = rd.randint(1, 10)
            num_2 = rd.randint(1, 3)
            operator = rd.randint(1, 2)
            
            match operator:
                case 1:
                    answer = num_1 + num_2
                    self.userinput = int(input("Question_{2}: {0} + {1} =? ".format(num_1, num_2, num_of_ques)))
                    if self.userinput == answer:
                        self.score += 5
                        print("\nT H E  A N S W E R  IS  C O R R E C T\n")
                        print(self.display_score())
                    else:
                        self.score -= 3
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
                        self.score -= 3
                        print(f"\nT H E  A N S W E R  IS  I N C O R R E C T\nTHE CORRECT ANSWER IS = {answer}\n")
                        print(self.display_score())
        
            if num_of_ques == 10:
                self.level_2()