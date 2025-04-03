# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $\n"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
# people = int(input("How many people to split the bill? \n"))

# pay=(bill+(bill*tip/100))/people

# print("Each person should pay: $" + str(round(pay, 2)))

import streamlit as st

def main():
    st.title("Tip Calculator")
    st.write("Welcome to the tip calculator!")

    bill = st.number_input("What was the total bill? $", min_value=0.0, format="%.2f")
    tip = st.slider("What percentage tip would you like to give?", 0, 100, 10)
    people = st.number_input("How many people to split the bill?", min_value=1, step=1)

    if people > 0:
        pay = (bill + (bill * tip / 100)) / people
        st.write(f"Each person should pay: ${round(pay, 2)}")

if __name__ == "__main__":
    main()
