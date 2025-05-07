import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"\@\w+|\#", "", text)  # remove mentions and hashtags
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # remove punctuations
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()