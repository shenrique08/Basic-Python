import random

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("\n===== Welcome to Treasure Island =====\nYour mission is to find the treasure.\n")


def get_random_direction(direction):
    return random.choice(direction)


def print_game_over():
    print("You felt into a hole ): GAME OVER")


directions = get_random_direction(["left", "right"])
left_or_right = str(input("You're at a cross road. \nWhere do you wanna go? Type LEFT or RIGHT: ")).lower()

if left_or_right == directions:
    wait_or_swim = str(input(
        "You come to a lake. There is an island in the middle of the lake. \n"
        "Type WAIT for a boat. Type SWIM to swim across: ")).lower()
    directions2 = get_random_direction(["wait", "swim"])

    if wait_or_swim == directions2:
        blue_or_red = str(
            input("You arrive at the island unharmed. \nThere is a house with 3 doors. One RED and one BLUE. "
                  "Which color do you choose? ")).lower()
        directions3 = get_random_direction(["red", "blue"])

        if blue_or_red == directions3:
            print("YOU WON !!!!!")
        else:
            print_game_over()
    else:
        print_game_over()
else:
    print_game_over()
