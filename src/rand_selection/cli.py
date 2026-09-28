from rand_selection.data import name_list, questions
from rand_selection.selector import random_selection

def main ():
    while True:
        resp = input("Press 'Y' to continue, any other key to exit: ")

        if resp.upper() != 'Y':
            break
        else:
            chosen_name, chosen_question = random_selection(name_list, questions)
            print(f"{chosen_name}, please answer: {chosen_question}\n")