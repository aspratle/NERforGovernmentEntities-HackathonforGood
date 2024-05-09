import streamlit as st
import joblib
import pandas as pd
from nltk.tokenize import word_tokenize

model = joblib.load('dt_model_new.pkl')
def predict_class(data):
    # Preprocess your text data if needed
    # Make prediction using the loaded model
    prediction = model.predict(data)[0]
    return prediction
# Streamlit app layout
st.title('Text Classifier: Person or Government?')
user_input_name = st.text_input("Enter name:", None)
user_input_info = st.text_input("Enter extra info:", None)
st.write("You entered:", user_input_name)
dataframe = pd.DataFrame({'name': [user_input_name], 'extra_info': [user_input_info]})

#Function to tokenize
def tokenize_column(df, column_name):
    # Define a tokenizer function
    def tokenizer(text):
        if pd.isna(text):
            return []
        tokens = word_tokenize(text)
        # Convert each token to lowercase
        tokens_lower = [token.lower() for token in tokens]
        return tokens_lower
    df[column_name + '_tokenized'] = df[column_name].apply(tokenizer)

    return df
  
# Define all regex patterns
regex1 =  r'u\.s\.'
regex2 = r'\bdepartment\s+of\b'
regex3 = r'\bcity of\b'
regex4 = r'^(?!.*l\.l\.c\.).*$'
regex5 = r'(?:officer|secretary|correctional|district attorney|d.a.|warden|police|judge|district attorney\'s|p.o.|jury|badge|sergeant|lieutenant|parole)\s+\w+'
regex6 = r'^(?!\b\w+\s+[a-zA-Z]\s+\w+\b).*$'
regex8 = r'\bdept\b'
regex10 = r'^(?!.*\bindividual|individually\b).*$'
regex11 = r'(?:officer|secretary|correctional|district attorney|d.a.|warden|police|judge|district attorney\'s|p.o.|jury|badge|sergeant|lieutenant|parole)\s+\w+'
regex12 = r'^(?!.*llc).*$'
regex13 = r'\binc\b'

# Function to create dataframe and features from text input
def create_binary_features(df):
  df = df.copy()
  df['name'] = df['name'].str.lower()
  df['extra_info'] = df['extra_info'].str.lower()
  df = tokenize_column(df, 'name')
  df['token_count'] = df['name_tokenized'].apply(lambda x: len(x))
  df = df.assign(let_period_let_regex=df['name'].str.contains(regex1),
                 dept_of_regex=df['name'].str.contains(regex2),
                 cityof_regex=df['name'].str.contains(regex3),
                 llc_regex=df['name'].str.contains(regex4),
                 formal_name_regex=df['name'].str.contains(regex5),
                 word_let_word_regex=df['name'].str.contains(regex6),
                 dept_regex=df['name'].str.contains(regex8))
  df['two_tokens'] = (df['token_count'] == 2).astype(int)
  df['three_tokens'] = (df['token_count'] == 3).astype(int)
  df = df.assign(extra_info_notindiv_regex=df['extra_info'].str.contains(regex10),
                 extra_info_formal_regex=df['extra_info'].str.contains(regex11),
                 word_llc_regex=df['name'].str.contains(regex12),
                 inc_regex=df['name'].str.contains(regex13))
  df = df.replace({False: 0, True: 1})
  df.drop(columns=['name', 'extra_info', 'name_tokenized'], inplace=True)
  return df

data = create_binary_features(dataframe)
st.write(data)
if st.button('Predict'):
    if user_input_name:
        prediction = predict_class(data)
        st.write(f'Predicted class: {"Government" if prediction == 1 else "Person"}')
    else:
        st.warning("Please enter some text.")
