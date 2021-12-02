import streamlit as st
import pickle
import numpy as np 
from PIL import Image

classifier = pickle.load(open('model.pkl', 'rb'))
# image1 = np.array(Image.open("m.png"))
# image2 = np.array(Image.open("treatments.png"))
# image3 = np.array(Image.open("Yes.png"))

# image1 = Image.open("m.png")
# image2 = Image.open("treatments.png")
# image3 = Image.open("Yes.gif")

st.header("Diabetes predication")
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
        st.markdown(f""" # {my_prediction}""")
        st.markdown("""
                    # COMMON DIABETES TREATMENTS
                    * **INSULIN** : All people with type 1 need to take insulin every day via an injection, pump, or inhaler. Only some with type 2 or gestational diabetes require this med.
                    * **ORAL MEDS** : Those with type 2 diabetes may take a daily cocktail of pills and liquids (and sometimes insulin, too) to keep blood sugar in a healthy range.
                    * **HOME GLUCOSE METER** : This treatment starts with you at home, where you'll test your glucose every day. Based on your levels you'll know how, what and when to eat.
                    * **DIET & EXERCISE** : Although type 1 diabetes can't be managed with lifestyle changes. eating a healthy diet and regularly breaking a sweat can provide big benefits for those with type 2.
                    """)
    elif my_prediction == "You don't Have Diabetes":
        st.markdown(f""" 
                    # Yay!
                    ## {my_prediction}
                    """)

if __name__ == '__main__':
    pass
