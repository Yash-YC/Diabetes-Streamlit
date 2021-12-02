import streamlit as st
import pickle
import numpy as np 
from PIL import Image

classifier = pickle.load(open('model.pkl', 'rb'))
image1 = np.array(Image.open("m.png"))
image2 = np.array(Image.open("treatments.png"))
image3 = np.array(Image.open("Yes.gif"))

# image1 = Image.open("m.png")
# image2 = Image.open("treatments.png")
# image3 = Image.open("Yes.gif")

st.image(image1)
preg = st.slider("Number of Pregnancies", min_value= 0 , max_value = 20, step= 1 )
glucose = st.number_input("Glucose", format="%d" , value = 0 )
bp = st.number_input("Bloodpressure", format="%d" , value = 0)
sct = st.number_input("Skinthickness", format="%d" , value = 0)
insulin = st.number_input("Insulin", format="%d" , value = 0)
bmi = st.number_input("bmi",format="%.2f", value = 0.0)
dpf = st.number_input("DPF",format="%.2f", value=0.0)
age = st.slider("Age" , min_value= 0 ,max_value = 150, step= 1)
if st.button("Predict"):
    data = np.array([[preg, glucose, bp, sct, insulin, bmi, dpf, age]])
    my_prediction = classifier.predict(data)
    my_prediction =  "You don't Have Diabetes" if my_prediction == 0 else "You Have Diabetes. Take care"
    if my_prediction == "You Have Diabetes. Take care" :
        st.image(image2)
        st.markdown(f""" # {my_prediction}""")
    elif my_prediction == "You don't Have Diabetes":
        st.image(image3)
        st.markdown(f""" # {my_prediction}""")

if __name__ == '__main__':
    pass
