import streamlit as st
st.title("BMI Calculator")
st.image("bmi.png")
weight = st.number_input("Enter your weight in kgs :")
height = st.number_input("Enter your height in cms :")
if weight > 0 and height > 0 :
    height /= 100
    bmi = weight / (height**2)
    if st.button("Calculate") :
        st.write(f"Your BMI : {bmi : .2f}")
        if bmi < 18.5 :
            st.success("Category : Underweight")
        elif bmi >= 18.5 and bmi <= 24.9 :
            st.success("Category : Normal Weight")
        elif bmi>=25 and bmi<=29.9 :
            st.success("Category : Class 1 Obesity")
        elif bmi>=30  and bmi <= 39.9 :
            st.success("Category : Class 2 Obesity")
        else :
            st.success("Category : Class 3 Obesity")
else:

    st.info("⚠️Please enter a valid weight and a height more than 0!")

st.write("Developed by 𝒜𝓇𝒾𝑒")
