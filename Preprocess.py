import pandas as pd
from nltk.corpus import stopwords
import nltk
import string
import re
import ast

class Preprocess:
    def __init__(self, csv_address):
        self.csv_file = pd.read_csv(csv_address)

    def remove_punctuation(self, text):
        PUNCT_TO_REMOVE = string.punctuation
        return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))


    def str_simplified(self, text):
        words = nltk.word_tokenize(text=text)
        return self.remove_punctuation(' '.join([w.lower() for w in words]))
    
    def remove_html(self, text):
        html_pattern = re.compile('<.*?>')
        return html_pattern.sub(r'', text)
    
    def remove_urls(self, text):
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        return url_pattern.sub(r'', text)
    
    def remove_stopwords(self, text):
        STOPWORDS = set(stopwords.words('english'))
        return " ".join([word for word in str(text).split() if word not in STOPWORDS])
    
    def str2array(self, string):
        string = str(string)[1:-1]
        return str(string).replace(", \\'", ",").replace("[\\", "[").replace("'", '').split(',')

    def process(self, user_uni, field, key_words):
        user_uni_processed = self.str_simplified(user_uni)
        user_field_processed = self.str_simplified(field)
        key_words_by_uni:list

        selected_rows_by_uni = []
        key_words_by_uni = []
        for index, row in self.csv_file.iterrows():
            if user_uni_processed in self.str_simplified(row['university_name']) and user_field_processed == self.str_simplified(row['program_name']):
                key_words_row = key_words

                key_words_row.append('ielts score needed for university is ' + str(row['ielts_score']))
                key_words_row.append('university rank is ' + str(row['university_rank']))
                key_words_row.append('program name is ' + str(row['program_name']))
                key_words_row.append('program type is ' + str(row['program_type']))

                if str(row['structure']) == '': continue
                for elem in self.str2array(row['structure']):
                    elem_changed = self.remove_punctuation(self.remove_urls(self.remove_html(elem)))
                    if elem_changed != '':
                        key_words_row.append(self.remove_stopwords(elem_changed.lower()))
                key_words_by_uni.append((index, key_words_row))
                
        return key_words_by_uni
        