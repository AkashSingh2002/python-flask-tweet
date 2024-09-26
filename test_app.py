import pytest
from flask import Flask
from app import app as flask_app
from tweet_analyzer import TweetAnalyzer
from unittest.mock import MagicMock

@pytest.fixture
def client():
    """Fixture to create a Flask test client."""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_index_page(client):
    """Test that the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Search Twitter Data' in response.data

def test_query_page(client, monkeypatch):
    """Test the query page with mocked TweetAnalyzer."""
    
    # Mock the query_term method to return fake data
    mock_tweet_analyzer = MagicMock()
    mock_tweet_analyzer.query_term.return_value = {
        "daily_tweets": [{"date": "2022-01-01", "count": 10}],
        "unique_users": 5,
        "avg_likes": 15.0,
        "place_ids": ["NYC", "LA"],
        "tweet_times": [12, 13],
        "top_user": 1
    }

    # Use monkeypatch to replace the tweet_analyzer in the app with the mock
    monkeypatch.setattr('app.tweet_analyzer', mock_tweet_analyzer)

    # Make a POST request to the query page
    response = client.post('/query', data={'term': 'python'})
    
    # Check if the response contains expected data
    assert response.status_code == 200
    assert b'Results for "python"' in response.data
    assert b'2022-01-01: 10 tweets' in response.data
    assert b'Unique Users: 5' in response.data
    assert b'Average Likes: 15.0' in response.data

def test_invalid_term(client, monkeypatch):
    """Test the query page with an invalid or empty search term."""

    # Mock query_term to return no results
    mock_tweet_analyzer = MagicMock()
    mock_tweet_analyzer.query_term.return_value = {}

    monkeypatch.setattr('app.tweet_analyzer', mock_tweet_analyzer)

    # Make a POST request with an empty term
    response = client.post('/query', data={'term': ''})

    # Check for empty or default response
    assert response.status_code == 200
    assert b'Results for ""' in response.data
    assert b'No results found' not in response.data  # Customize based on actual implementation
