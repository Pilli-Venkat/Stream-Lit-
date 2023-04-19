import streamlit as st


def find_length(a, b, c):
  return sorted([a,b,c],reverse= True)[0]


st.title('Largest Among Three Numbers - 22DS1000243 (PILLI SAI)')

# Get the user input for three numbers

num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')
num3 = st.number_input('Enter the third number')


if st.button('Largest Number'):
    length = find_length(num1, num2, num3)
    st.success('Largest Among three numbers is ' + str(length))