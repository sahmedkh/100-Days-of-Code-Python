print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_dec = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if first_dec == "left":
    sec_dec = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if sec_dec == "wait":
        third_dec = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n").lower()
        if third_dec == "red":
            print("Burned by fire.\nGame Over.\n")
        elif third_dec == "yellow":
            print("You Win!\n")
        elif third_dec == "blue":
            print("Eaten by beasts.\nGame Over.\n")
        else:
            print("Game Over.\n")
    else:
        print("Attacked by a trout.\nGame Over.\n")
else:
    print("Fall into a hole.\nGame Over\n")