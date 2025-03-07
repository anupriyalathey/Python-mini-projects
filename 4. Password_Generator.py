# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Easy Level
# # password = ""
# # for char in range(0, nr_letters):
# #     password += random.choice(letters)
# #
# # for char in range(0, nr_symbols):
# #     password += random.choice(symbols)
# #
# # for char in range(0, nr_numbers):
# #     password += random.choice(numbers)
# #
# # print(password)

# # Hard level
# password_list = []
# for char in range(0, nr_letters):
#     password_list.append(random.choice(letters))

# for char in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))

# for char in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(f"Your password is: {password}")


import streamlit as st
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
    'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(nr_letters, nr_symbols, nr_numbers):
    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    return "".join(password_list)

def main():
    st.title("🔑 Password Generator")
    st.write("Welcome to the Password Generator!")

    # User inputs for the password components
    nr_letters = st.slider("Number of letters:", min_value=1, max_value=20, value=8)
    nr_symbols = st.slider("Number of symbols:", min_value=0, max_value=10, value=2)
    nr_numbers = st.slider("Number of numbers:", min_value=0, max_value=10, value=2)

    if st.button("Generate Password"):
        password = generate_password(nr_letters, nr_symbols, nr_numbers)
        st.success(f"Your generated password is: `{password}`")

if __name__ == "__main__":
    main()
