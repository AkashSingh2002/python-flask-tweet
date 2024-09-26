
# Twitter Data Analysis System

This is a Twitter data analysis system built using Python, Flask, and Pytest. The system allows users to query Twitter data by term and returns various statistics about the tweets.

## Requirements

- Python 3.9+
- Flask
- Pandas
- Dask
- Pytest
- Docker (optional)

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Running the App

To start the Flask development server, navigate to the project directory and run the following command:

```bash
python app.py
```

You can access the app by visiting `http://localhost:5000` in your web browser.

## Querying the Data

You can query the data using the `query_data.py` script. This script takes a term as input and returns statistics about the tweets containing that term.

Run the script with the following command:

```bash
python query_data.py
```

The script will prompt you to enter a term, and it will return statistics for the tweets containing that term.

Alternatively, you can query the data by sending a GET request to the `/query` endpoint with the term parameter. For example:

```bash
curl http://localhost:5000/query?term=python
```

This will return a JSON response with statistics about the tweets containing the term "python".

## Running the Tests

To run the tests, navigate to the project directory and use the following command:

```bash
pytest
```

This will run all tests and report any errors or failures.

## Docker

To run the app using Docker, use the following command in the project directory:

```bash
docker-compose up
```

Once the container is running, the app can be accessed at `http://localhost:5000`.

## Troubleshooting

If you encounter any issues, try the following steps:

1. Ensure all required dependencies are installed.
2. Check the logs for any error messages.
3. Retry running the app or tests.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. Make sure to include tests for any new functionality.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Example Use Case

Here’s an example of how to use the `query_data.py` script:

```bash
$ python query_data.py
Enter a term: python
{
  "daily_tweets": [
    {
      "date": "2022-01-01",
      "count": 10
    },
    {
      "date": "2022-01-02",
      "count": 20
    }
  ],
  "unique_users": 5,
  "avg_likes": 15.0,
  "place_ids": ["NYC", "LA"],
  "tweet_times": [12, 13],
  "top_user": 1
}
```

This example demonstrates how the system provides various statistics about tweets containing the specified term.

---
