from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_features(texts, max_features=1000):
    vectorizer = TfidfVectorizer(max_features=max_features)
    features = vectorizer.fit_transform(texts)
    return features, vectorizer
