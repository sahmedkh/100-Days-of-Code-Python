import random

def main():
    print("Welcome to the PyPassword Generator!")
    num_letters = int(input("How many letters would you like in your password?\n"))
    num_symbols = int(input("How many symbols would you like in your password?\n"))
    num_numbers = int(input("How many numbers would you like in your password?\n"))
    print(f"Here is your password: {generate_pass(num_letters, num_symbols, num_numbers)}")

def generate_pass(n_let, n_sym, n_num):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()-_+=][><.,?;:'`~"
    password = []
    for _ in range(n_let):
        index = random.randint(0, len(letters) - 1)
        password.append(letters[index]) 
    for _ in range(n_sym):
        index = random.randint(0, len(symbols) - 1)
        password.append(symbols[index])
    for _ in range(n_num):
        index = random.randint(0, 9)
        password.append(str(index))

    random.shuffle(password)

    pass_str = ""
    for char in password:
        pass_str += char

    return pass_str 


main()