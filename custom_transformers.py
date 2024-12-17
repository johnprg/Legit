# custom_transformers.py
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

class LemmatizerStemmer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Ensure X is a list of strings
        print(f"Input to transform: {X}")  # Debugging statement
        if isinstance(X, list):
            return [
                ' '.join([self.lemmatizer.lemmatize(self.stemmer.stem(word)) 
                        for word in text.split()])
                for text in X
            ]
        else:
            raise ValueError("Input to LemmatizerStemmer.transform must be a list of strings")

