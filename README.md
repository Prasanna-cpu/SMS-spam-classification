# SMS-spam-classification

This project is a machine learning-based SMS spam classifier that uses Natural Language Processing (NLP) techniques to differentiate between spam and non-spam (ham) messages.

## Project Overview

This project aims to build a classifier that can accurately distinguish between spam and ham messages in a given dataset of SMS messages. This can be useful for automatically filtering out unwanted spam messages from user inboxes.

The project involves the following steps:
1. Data Preprocessing: Cleaning and preparing the SMS text data for analysis, including tokenization, lowercasing, and removing special characters.
2. Feature Extraction: Utilizing NLP techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) to convert text data into numerical features that machine learning algorithms can use.
3. Model Selection: Experiment with various machine learning algorithms (e.g., Naive Bayes, Decision Tree Regression, etc.) to find the best-performing model for the task.
4. Model Training: Training the selected model on a labeled dataset of SMS messages, using features generated through TF-IDF.
5. Model Evaluation: Assessing the model's performance using metrics like accuracy, precision, recall, confusion matrix, and F1-score
## Libraries used

1. nltk-> Text Processing(Porter Stemmer)
2. spaCy-> Text Processing(Tokenization,Stop words Removal,Lemmatization,Language Model)
3. numpy and pandas-> Data Wrangling
4. matplotlib and seaborn -> Data Visualization
5. scikit-learn->Machine Learning Algorithms
6. wordcloud-> Intuitive visualization of the frequency of words
7. pickle-> Serialization and Deserialization of objects
8. streamlit-> Interactive front-end UI for building data science apps quickly.

## Credits
This project was developed by [Prasanna Kumar]. If you find this project useful or have any suggestions for improvements, feel free to reach out at [kumar22maran@gmail.com].





