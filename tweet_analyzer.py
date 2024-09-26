import pandas as pd

class TweetAnalyzer:
    def __init__(self, df):
        self.df = df

    def query_term(self, term):
        # Filter tweets containing the term
        term_tweets = self.df[self.df['text'].str.contains(term, case=False)]

        # Calculate unique user counts
        unique_users = term_tweets['author_handle'].nunique()

        # Calculate average likes
        avg_likes = term_tweets['like_count'].mean()

        # Calculate place IDs
        place_ids = term_tweets['place_id'].value_counts().index.tolist()

        # Calculate tweet times
        tweet_times = pd.to_datetime(term_tweets['created_at']).dt.hour.value_counts().index.tolist()

        # Calculate top user
        top_user = term_tweets['author_handle'].value_counts().index[0]

        return {
            'unique_users': unique_users,
            'avg_likes': avg_likes,
            'place_ids': place_ids,
            'tweet_times': tweet_times,
            'top_user': top_user
        }

    def save_to_disk(self, filename):
        self.df.to_pickle(filename)

    @classmethod
    def load_from_disk(cls, filename):
        df = pd.read_pickle(filename)
        return cls(df)