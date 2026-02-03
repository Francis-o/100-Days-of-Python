"""
Find the treasure... and survive
"""

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("You wake up on the shores of Treasure Island, clutching an ancient map" \
" soaked in salt water. \nLegend say only the clever escape with the treasure." \
"\nYour mission: Find the treasure... and survive.\n")

first_decsion = input("You reach a fork in the jungle path. \n" \
"The left path is dark and quiet, with strange footprints.\n" \
"The right path is bright but you hear distant growls. \nWhere would you go? R or L: ").upper()

if first_decsion == "L":
    second_decision = input("You arrive at a wide river filled with snapping " \
    "jaws beneath the surface\n" \
    "Would you swim or wait? S or W: ").upper()
    if second_decision == "W":
        third_decision = input("Night falls. You discover an ancient stone temple.\n" \
        "Three doors stand before you:  🟥 Red, 🟨 Yellow and  🟦 Blue. \n" \
        "Choose a door to enter. R or Y or G: ").upper()
        if third_decision == "Y":
            print("YOU WIN 🎉")
        else:
            if third_decision == "R":
                print("Flames burst from the walls.\n" \
                "Greed burns bright... and fatal. \n Game Over!")
            elif third_decision == "B":
                print("The door seals behind you. The air freezes.\n" \
                "You fade into the legend." \
                "Game Over!")
    else:
        print("Halfway across, the water explodes with movement.\n" \
        "The river claims another victim.\n" \
        "Game Over!")
else:
    print("You walk confidently... straight intoa pack of wild beasts" \
    "\nYou never stood a chance." \
    "\nGame Over!")