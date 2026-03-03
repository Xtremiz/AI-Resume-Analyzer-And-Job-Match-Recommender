from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
def preprocess(text):
    list = []
    for i in text.split():
        if i.lower() not in stop_words and i not in string.punctuation:
            list.append(ps.stem(i))
    return " ".join(list)
def uniqueonly(text):
    list = []
    for word in text.split():
        if word not in list:
            list.append(word)
    return " ".join(list)
        