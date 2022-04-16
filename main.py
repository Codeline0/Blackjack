from tutorial import main as tuto

class Player:
    sum_of_cards = 0
    bet = 0
    blackjack = False
    pairs = False
    bust = False
    ace = True
    hit = False
    stand = False
    double_down = False

    def __init__(self, name, is_dealer=False):
        self.name = name
        self.is_dealer = is_dealer

#This function is set to repeat itself until it gets a satisfactory answer.
#Either if they choose to play the tutorial (loads tutorial script), or not (pass).
def tuto_answer(script):
    tuto_response = input()
    if tuto_response.lower() == "y":
        print("\033c")
        script(main_player.name)
    elif tuto_response.lower() == "n":
        pass
    else:
        print("Please input y for yes and n for no")
        tuto_answer(script)

# The main game
def main():
    print(
        """
---------------------------------------------------------------------------------     
 /$$$$$$$  /$$                     /$$                               /$$      
| $$__  $$| $$                    | $$                              | $$      
| $$  \ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$
| $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/
| $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/ 
| $$  \ $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$ 
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$|  $$$$$$$|  $$$$$$$| $$ \  $$
|_______/ |__/ \_______/ \_______/|__/  \__/| $$ \_______/ \_______/|__/  \__/
                                       /$$  | $$                              
                                      |  $$$$$$/                              
                                       \______/       
--------------------------------------------------------------------------------- 

Ready to play some good old fashioned Blackjack? 

First thing first, what should I call you?

    """
    )

    main_name = input()
    global main_player  #Used a global variable to use this variable in different functions
    main_player = Player(main_name)
    print("Great to know you {}, now, would you like to play the tutorial? y/n".format(main_player.name))

    tuto_answer(tuto)
    



if __name__ == "__main__":
    main()

