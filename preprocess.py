import re 

def preprocess(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|http\S+|www\S+|\bhttps?\b', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


