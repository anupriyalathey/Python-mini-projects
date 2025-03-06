# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# # Note: it's worth checking if the user has made a valid choice before the next line of code.
# # If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# # You could for example write:
# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")

import streamlit as st
import random

# ASCII art for the game
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

game_images = [rock, paper, scissors]

def main():
    st.title("🪨📄✂️ Rock, Paper, Scissors Game 🪨📄✂️")
    st.write("Welcome to the classic game of Rock, Paper, Scissors!")

    # User choice
    user_choice = st.selectbox("What do you choose?", ["Rock", "Paper", "Scissors"])
    user_choice_index = ["Rock", "Paper", "Scissors"].index(user_choice)

    # Display user's choice
    st.write("You chose:")
    st.code(game_images[user_choice_index])

    # Computer choice
    computer_choice = random.randint(0, 2)
    st.write("Computer chose:")
    st.code(game_images[computer_choice])

    # Determine the result
    if user_choice_index == computer_choice:
        st.info("It's a draw!")
    elif (user_choice_index == 0 and computer_choice == 2) or \
         (user_choice_index == 1 and computer_choice == 0) or \
         (user_choice_index == 2 and computer_choice == 1):
        st.success("You win!")
    else:
        st.error("You lose!")

if __name__ == "__main__":
    main()
