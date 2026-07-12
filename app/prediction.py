import joblib
from pathlib import Path
from preprocess import preprocess

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

class ToxicityDetector:
    def __init__(self):
        self.LABELS = [
            "toxic",
            "severe",
            "obscene",
            "threat",
            "insult",
            "identity-hate"
        ]
        self.model = joblib.load(MODELS_DIR/"toxicity_model.joblib")
        self.vectorizer = joblib.load(MODELS_DIR/"tfidf_vectorizer.joblib")

    def predict(self, text):
        text = preprocess(text)
        vector = self.vectorizer.transform([text])
        prediction = self.model.predict(vector)[0]
        
        detected_labels = [
            label for label, value in zip(self.LABELS, prediction) if value==1    
        ]

        return {
            "is_toxic": any(prediction),
            "labels": detected_labels
        }

