import streamlit as st


def find_length(a, b, c):
  return sorted([a,b,c],reverse= True)[0]
# Set the title of the application
st.title('Find Length Among Three Numbers')

# Get the user input for three numbers
num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')
num3 = st.number_input('Enter the third number')

# Get the length among the three given numbers
if st.button('Find Length'):
    length = find_length(num1, num2, num3)
    st.success('The length among the three given numbers is: ' + str(length))
