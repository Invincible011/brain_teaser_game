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
        if self.time < 12:
            return f'\n\t\t\t\t\t\tGood Morning: {self.username}'
        elif self.time <= 15:
            return f'\n\t\t\t\t\t\tGood Afternoon: {self.username}'
        else: 
            return f'\n\t\t\t\t\t\tGood Evening: {self.username}'
    
    def _initialise_timer(self):
        pass

    def validate_user(self):
        print(self.startup_message())
        self.user_details()
        print(self.startup_info())

    def display_score(self):
        return f"Y o u r  S c o r e  i s: {self.score}"


class Stage(Game):

    userinput = 0

    def __init__(self):
        super().__init__()
        self.level = 0
    
    from Stage.Easy.level_1 import level_1
    from Stage.Easy.level_2 import level_2
    from Stage.Easy.level_3 import level_3
    from Stage.Easy.level_4 import level_4
    from Stage.Easy.level_5 import level_5


if __name__ == "__main__":
    gm = Stage()
    gm.level_1()
