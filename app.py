from flask import Flask, request, jsonify, render_template
from tweet_analyzer import TweetAnalyzer

app = Flask(__name__)

# Load the data from disk
tweet_analyzer = TweetAnalyzer.load_from_disk('data.pkl')

# Render the search page
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission and display results
@app.route('/query', methods=['POST'])
def query():
    term = request.form.get('term')  # Get the search term from the form
    results = tweet_analyzer.query_term(term)
    return render_template('index.html', term=term, results=results)

if __name__ == '__main__':
    app.run(debug=True)
