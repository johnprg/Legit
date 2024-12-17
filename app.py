# API Server using FastAPI

from fastapi import FastAPI
from pydantic import BaseModel
import joblib  
from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.base import BaseEstimator, TransformerMixin
from custom_transformers import LemmatizerStemmer

# Load your classifier
classifier = joblib.load("./legitimizer.pkl")

# Define the data structure for incoming requests as just a single text field
class InputData(BaseModel):
    text: str

app = FastAPI()

@app.post("/predict")
async def predict(data: InputData):
    # Extract features from the request
    features = [[data.feature1]]  # Adapt for your model's input shape
    # Generate prediction
    prediction = classifier.predict(features)
    print(f'classification:{prediction}')
    # Generate confidence score
    confidence = classifier.predict_proba(features)
    print(f'confidence:{confidence}')
    return {"prediction": prediction[0], "confidence": confidence[0][1]}

