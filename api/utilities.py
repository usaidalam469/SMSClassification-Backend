import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    """
    Preprocess the input text by applying several NLP techniques such as lowercasing,
    removing special characters and numbers, tokenization, removing stop words,
    and lemmatization.

    Args:
        text (str): The input text that needs to be preprocessed.

    Returns:
        str: The preprocessed text where stop words are removed, words are lemmatized,
             and special characters and numbers are eliminated.
             
    Steps:
        1. Convert text to lowercase.
        2. Remove special characters and numbers.
        3. Tokenize the text into words.
        4. Remove stop words (common words like "the", "and", etc.).
        5. Lemmatize the remaining words (convert them to their base form).
        6. Return the preprocessed text as a single string of cleaned tokens.
    """
    stop_words = set(stopwords.words('english'))
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return ' '.join(tokens)