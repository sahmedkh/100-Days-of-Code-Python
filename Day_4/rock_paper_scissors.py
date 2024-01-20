import random

def main():
    user_action = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
    print_action(user_action)

    comp_action = random.randint(0, 2)
    print("\nComputer chooses: ") 
    print_action(comp_action)

    print("---------- Result ----------")
    result = user_result(user_action, comp_action)
    if result == "won":
        print("You Won.\n")
    elif result == "lost":
        print("You Lost.\n")
    else:
        print("You Drew.\n")    


def print_action(act):
    rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''
    paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''
    scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''
    match act:
        case 0: 
            print(rock)
        case 1:
            print(paper)
        case 2:
            print(scissors)
        case _:
            print("Invalid Action.\n")

def user_result(u_act, c_act):
    if u_act == c_act:
        return "drew"
    if (u_act == 0 and c_act == 2) or (u_act == 1 and c_act == 0) or (u_act == 2 and c_act == 1):
        return "won"
    else:
        return "lost"
    
main()