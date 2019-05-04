from flask import Flask, make_response
import pandas as pd
from flask_cors import CORS
from flask import request
import json

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

def write_data(data):
    with open('data.txt', 'w') as outfile:
        # json.dump(data, outfile)
        for key in data:
            s = key + ': ' + str(data[key]) + '\n'
            outfile.write(s)

app = Flask(__name__)
CORS(app)
df = init()

@app.route("/getData")
def data():
    return df.to_json(orient='records')

@app.route("/save", methods = [ 'POST'])
def save():
    req_data = request.get_json(force=True)
    write_data(req_data)
    return make_response('Success', 200)













