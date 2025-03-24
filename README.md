# ✍️ SOP Generator – AI-Based Statement of Purpose Tool

This project automates the generation of Statements of Purpose (SOPs) for university applications using AI. By providing basic inputs like name, university, and field of study, the system intelligently extracts program details from a dataset and sends a prompt to OpenAI's language model to generate a complete SOP.

---

## 🚀 Features

- 🔍 **CSV-Based University Program Extraction**  
  Reads structured program details from a dataset based on the selected university and field of study.

- 🧹 **Text Preprocessing**  
  Cleans text data using:
  - Stopword removal
  - Punctuation stripping
  - HTML and URL removal
  - Tokenization and normalization

- 🤖 **AI SOP Generation**  
  Constructs a smart prompt based on extracted data and sends it to the OpenAI API (GPT) to generate a personalized SOP.

---

## 🧰 Tech Stack

- Python 3.x  
- [NLTK](https://www.nltk.org/)  
- [OpenAI GPT API](https://platform.openai.com/)  
- Pandas, Regex

---


