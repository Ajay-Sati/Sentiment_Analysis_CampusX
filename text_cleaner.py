# text_cleaner.py

import re
import nltk
import spacy
from nltk.corpus import stopwords

# Download resources if not already available
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Download resources if not already available
def clean_text(text):
    text = text.lower()   #  Lowercase conversion
    text = re.sub(r'http\S+|www\S+|https\S+', '', text) # URL removal
    text = re.sub(r'<.*?>', '', text) # HTML tag removal
    text = re.sub(r'[^a-z\s]', '', text) # Special character removal
    text = re.sub(r'\s+', ' ', text).strip() # Extra whitespace removal   #strip to remove forward or backward spcaes
    text = re.sub(r'\S+@\S+\.\S+', '', text) # email removal
    text = re.sub(r'[^\w\s]', '', text) # punctuations
    text = re.sub(r'(.)\1{2,}', r'\1', text) # Repeated Characters / Elongated Words
    text = re.sub(r'#', '', text) # Hashtags (like from Twitter/Instagram)
    text= re.sub(r'@\w+', '', text) # Mention username
    text= re.sub(r'[^\x00-\x7F]+', '', text) # non ASCII characters (emojis , foreign characcters)
    return text


def tokenize_and_lemmatize(text):
    """
    This function breaks down the text into words, removes unnecessary words (stop words),
    and turns words into their base forms (lemmas).
    """
    try:
        # Process the text using spaCy
        doc = nlp(text)

        # Create a list of words that are not stop words, punctuation, or spaces
        filtered_words = []
        for token in doc:
            if not token.is_stop and not token.is_punct and not token.is_space:
                filtered_words.append(token.lemma_)  # Add the base form (lemma) of the word

        # Return the list of filtered and lemmatized words
        return filtered_words

    except Exception as e:
        # If there's an error, return the error message
        return f"Error: {e}"