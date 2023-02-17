import joblib
import sys
import pandas as pd
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if pac:
        json = request.json
        query = pd.DataFrame(json)
        query.fillna('', inplace=True)
        prediction = pac.predict(tfidf_vectorizer.transform(query["text"])).tolist()
        return jsonify({'prediction': str(prediction)})
    else:
        print ('Train the model first')
        return ('No model here to use')


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    pac = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')

    tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl") # Load "tfidf_vectorizer.pkl"
    print ('Vectorizer loaded')

    app.run(port=port, debug=True)