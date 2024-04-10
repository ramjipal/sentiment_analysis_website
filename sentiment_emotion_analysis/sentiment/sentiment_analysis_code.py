from django.conf import settings
import os
import re
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer 
import itertools
import numpy as np
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import pickle

MODELS = os.path.join(settings.BASE_DIR, 'sentiment/models')
class sentiment_analysis_code():
    
    lem = WordNetLemmatizer()

    def cleaning(self, text):
        txt = str(text)
        txt = re.sub(r"http\S+", "", txt)
        if len(txt) == 0:
            return 'no text'
        else:
            txt = txt.split()
            if len(txt) == 0:
                return 'no text'
            else:
                words = txt[0]
                for k in range(len(txt)-1):
                    words+= " " + txt[k+1]
                txt = words
                txt = re.sub(r'[^\w]', ' ', txt)
                if len(txt) == 0:
                    return 'no text'
                else:
                    txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
                    txt = txt.replace("'", "")
                    txt = nltk.tokenize.word_tokenize(txt)
                    #data.content[i] = [w for w in data.content[i] if not w in stopset]
                    for j in range(len(txt)):
                        txt[j] = self.lem.lemmatize(txt[j], "v")
                    if len(txt) == 0:
                        return 'no text'
                    else:
                        return txt

    def get_comment_sentiment(self, comment):
            translator= GoogleTranslator(source='auto', target='en')
        #cleaning of comment
            # comment = ' '.join(self.cleaning(comment))
            comment = translator.translate(comment)
            analyzer = SentimentIntensityAnalyzer()
            vs = analyzer.polarity_scores(comment)
            print("-------------------------------------------")
            print(vs['compound'])
            if vs['compound'] < 0:
                return 'Negative'
            elif vs['compound'] > 0.48:
                return 'Positive'
            else:
                return 'Neutral'
    
class QuestinClassifier():
    def __init__(self):
        with open(MODELS+'/query_classifier.pickle', 'rb') as file:
            self.model = pickle.load(file)

        with open(MODELS+'/question_vectorizer.pickle', 'rb') as file:
            self.vectorizer = pickle.load(file)
    
    def isquestion(self, comment):
        vectorized_text = self.vectorizer.transform([comment])
        predict = self.model.predict(vectorized_text)
        return (predict[0])
        
        
if __name__ == "__main__":
    qclass = QuestinClassifier()
        