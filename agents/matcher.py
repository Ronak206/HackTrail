from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MatcherAgent:
    def match(self, cv_text, jd_texts, jd_titles):
        documents = [cv_text] + jd_texts
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        best_index = similarities.argmax()
        return jd_titles[best_index], similarities[best_index]