from flask import Flask, request, jsonify
from pymongo import MongoClient
import pandas as pd
from tweet_analyzer import TweetAnalyzer

app = Flask(__name__)

# Create a MongoDB client
client = MongoClient('mongodb://localhost:27017/')

# Get a reference to the database
db = client['mydatabase']

# Get a reference to the tweets collection
tweets = db['tweets']

try:
    # Convert the MongoDB collection to a Pandas DataFrame
    df = pd.DataFrame(list(tweets.find()))
except Exception as e:
    print(f"Error: {e}")
    df = None

if df is not None:
    tweet_analyzer = TweetAnalyzer(df)

    @app.route('/query', methods=['GET'])
    def query_tweets():
        term = request.args.get('term')
        results = tweet_analyzer.query_term(term)
        return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)