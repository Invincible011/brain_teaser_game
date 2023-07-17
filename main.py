from datetime import datetime as timer
import os

class Game:

    score = 0
    
    def __init__(self):
        self.counter = 0
        self.level = 0
    
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
            return f'\n\t\t\t\t\t\tG o o d  M o r n i n g: "{self.username}"'
        elif self.time <= 15:
            return f'\n\t\t\t\t\t\tG o o d  A f t e r n o o n: "{self.username}"'
        else: 
            return f'\n\t\t\t\t\t\tG o o d  E v e n i n g: "{self.username}"'
    
    def _initialise_timer(self):
        pass

    def validate_user(self):
        print(self.startup_message())
        self.user_details()
        print(self.startup_info())

    def display_score(self):
        return f"Y o u r  S c o r e  i s: {self.score}"


class Stage(Game):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.userinput = 0
    
    from Stage.Easy.level_1 import easy_level_1
    from Stage.Easy.level_2 import easy_level_2
    from Stage.Easy.level_3 import easy_level_3
    from Stage.Easy.level_4 import easy_level_4
    from Stage.Easy.level_5 import easy_level_5
    
    from Stage.Medium.level_1 import level_1
    from Stage.Medium.level_2 import level_2
    from Stage.Medium.level_3 import level_3
    from Stage.Medium.level_4 import level_4
    from Stage.Medium.level_5 import level_5

    from Stage.Hard.level_1 import hard_level_1
    from Stage.Hard.level_2 import hard_level_2
    from Stage.Hard.level_3 import hard_level_3
    from Stage.Hard.level_4 import hard_level_4
    from Stage.Hard.level_5 import hard_level_5



if __name__ == "__main__":
    gm = Stage()
    gm.easy_level_1()
