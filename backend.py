from flask import Flask
import pandas as pd
from flask_cors import CORS

def init():
    print('starting backend by reading data')
    init_df = pd.read_csv('data.csv', keep_default_na=True)
    # Remove the credit statements - these are just paying off the card
    init_df.dropna(subset=[' Debit'], inplace=True)

    # Rename columns to prepare for json
    debit_df = pd.DataFrame()
    debit_df['date'] = init_df[' Transaction Date']
    debit_df['description'] = init_df[' Description']
    debit_df['category'] = init_df[' Category']
    debit_df['amount'] = init_df[' Debit']
    return debit_df

app = Flask(__name__)
CORS(app)
df = init()

@app.route("/getData")
def hello():
    return df.to_json(orient='records')













