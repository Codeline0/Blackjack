from tutorial import main as tuto
import text_effects
import game

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
    logo = '''
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
    '''
    intro_question = "Ready to play some good old fashioned Blackjack?\n\n"
    name_question = "First of all, what's your name?\n\n" 
    tuto_question = "Great to know you {}, now, would you like to play the tutorial? y/n\n\n"
    dialogue_speed = 0.05

    text_effects.rise_effect(logo, 0.1)
    text_effects.writing_effect(intro_question, dialogue_speed)
    text_effects.enter_continue()
    text_effects.writing_effect(name_question, dialogue_speed)
    
    main_name = input()
    print("\033[A                             \033[A")  #Used to erase previous print
    global main_player  #Used global varible for usage in different functions
    main_player = game.Player(main_name)

    text_effects.writing_effect(tuto_question.format(main_player.name), dialogue_speed)

    tuto_answer(tuto)
    



if __name__ == "__main__":
    main()

