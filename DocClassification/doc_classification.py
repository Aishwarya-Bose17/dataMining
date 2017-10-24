import csv
from nltk.tokenize import word_tokenize
import string
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_record(prodcsv):
    record = {}
    csv.field_size_limit(sys.maxsize)
    with open(prodcsv, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
           text = ' '.join(row[1:])
           text = text.lower()
           no_punctuation = text.translate(None, string.punctuation)
           record[row[0]] = unicode(no_punctuation, errors='ignore')
    return record


def tokenize(text):
    tokens=word_tokenize(text)
    return tokens

amazon_data = get_record("Amazon.csv")
google_data = get_record("GoogleProducts.csv")

output=open("output.csv", 'w')

for k, v in google_data.items():
    for k1, doc1 in amazon_data.items():
        train_set = [v , doc1]
        tfidf_vectorizer = TfidfVectorizer()

        tfidf_matrix_train = tfidf_vectorizer.fit_transform(train_set)
        cos = cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train)
        try:
          if cos[0][1] >= .5:
              print k, "," ,k1
        except:
            pass
