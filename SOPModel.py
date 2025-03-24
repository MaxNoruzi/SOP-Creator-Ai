import pandas as pd
import nltk
import Preprocess
import openai
import os

class SOPModel:

    def __init__(self, username, university_name, study_filed, key_words, csv_address):
        self.username = username
        self.university_name = university_name
        self.study_filed = study_filed
        self.key_words = key_words
        self.csv_address = csv_address
        self.info_for_sop:list
        
        
    def preprocess(self):
        preprocess = Preprocess.Preprocess(csv_address=self.csv_address)

        self.info_for_sop = preprocess.process(self.university_name, self.study_filed, self.key_words)

    def get_sop(self, name, last_name):
        values_concatenated = ''
        for key, value_list in self.info_for_sop:
            for value in value_list:
                values_concatenated += " "+value
        # print(values_concatenated)
        question ="i want you to give me an SOP for my university my name is :"+name+" and my last name is :"+last_name+" and key words are:"+values_concatenated
        self.getRequest(question)
        # print(question)
        
    def getRequest(question):
    # Set your API key
        os.environ["OPENAI_API_KEY"] = "APiKey"
        openai.api_key = os.environ["OPENAI_API_KEY"]

        # Prompt for your question
        #question = "What is the capital of France?"

        # Call the OpenAI API to answer the question
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Print the answer
        answer = response.choices[0].text.strip()
        print(answer)  
    