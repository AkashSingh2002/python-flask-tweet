import pandas as pd
import dask.dataframe as dd
from tweet_analyzer import TweetAnalyzer

# Read the small TSV file (50MB)
dtype = {'hashtags': 'object',
         'media_keys': 'object',
         'place_id': 'object',
         'quoted_handle': 'object',
         'urls': 'object'}

df_small = dd.read_csv('small_file.tsv', sep='\t', dtype=dtype)

# Convert the Dask DataFrame to a Pandas DataFrame
df_small = df_small.compute()

# Create a TweetAnalyzer instance
tweet_analyzer = TweetAnalyzer(df_small)

# Save the data to disk
tweet_analyzer.save_to_disk('data.pkl')