import streamlit as st
import math

# Define mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x):
    if x > 0:
        return math.log(x)
    else:
        return "Logarithm is not defined for non-positive values."

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Streamlit app
def scientific_calculator():
    st.title("Scientific Calculator")

    # Dropdown menu for operation selection
    operation = st.selectbox("Select operation:", 
                             ["Add", "Subtract", "Multiply", "Divide", 
                              "Power", "Square Root", "Logarithm", 
                              "Sine", "Cosine", "Tangent"])
    
    if operation in ['Add', 'Subtract', 'Multiply', 'Divide', 'Power']:
        num1 = st.number_input("Enter first number:", value=0.0)
        num2 = st.number_input("Enter second number:", value=0.0)
    elif operation in ['Square Root', 'Logarithm']:
        num = st.number_input("Enter a number:", value=0.0)
    else:
        angle = st.number_input("Enter angle in degrees:", value=0.0)

    # Red submit button
    submit = st.button("Submit", key="submit_button")
    st.markdown(
        """<style> div.stButton > button:first-child { background-color: red; color: white; } </style>""",
        unsafe_allow_html=True
    )

    # Perform calculation when the submit button is pressed
    if submit:
        result = None
        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
        elif operation == 'Power':
            result = power(num1, num2)
        elif operation == 'Square Root':
            result = sqrt(num)
        elif operation == 'Logarithm':
            result = log(num)
        elif operation == 'Sine':
            result = sin(angle)
        elif operation == 'Cosine':
            result = cos(angle)
        elif operation == 'Tangent':
            result = tan(angle)

        st.write(f"Result: {result}")

# Run the Streamlit app
if __name__ == "__main__":
    scientific_calculator()

