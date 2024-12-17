import streamlit as st
import joblib
from custom_transformers import LemmatizerStemmer

# Load the saved model
classifier = joblib.load("legitimizer.pkl")

# Streamlit UI setup
st.title("Text Classifier App")
st.write("Enter a sentence, and the model will predict its class!")

# Text input box
user_input = st.text_area("Input Text", "")

# Predict button
if st.button("Predict"):
    if user_input:
        # Pass input to the model
        input_text = [user_input]  # Model expects a list of strings
        prediction = classifier.predict(input_text)
        st.success(f"Prediction: {prediction[0]}")
    else:
        st.warning("Please enter some text to classify.")
