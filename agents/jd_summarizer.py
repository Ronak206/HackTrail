from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
import re

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

def preprocess(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    tokens = tokenizer.tokenize(text)
    filtered = [lemmatizer.lemmatize(w) for w in tokens if w.isalpha() and w not in stop_words]
    return " ".join(filtered)

class JDSummarizerAgent:
    def __init__(self, job_descriptions):
        self.job_titles = list(job_descriptions.keys())
        self.job_texts_clean = [preprocess(text) for text in job_descriptions.values()]

    def get_summary(self):
        return self.job_titles, self.job_texts_clean