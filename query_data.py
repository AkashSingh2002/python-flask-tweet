from tweet_analyzer import TweetAnalyzer

def main():
    tweet_analyzer = TweetAnalyzer.load_from_disk('data.pkl')
    
    query = input("Enter a search query: ")
    
    results = tweet_analyzer.query_term(query)
    
    print("Search Results:")
    print("----------------")
    print(f"Unique Users: {results['unique_users']}")
    print(f"Average Likes: {results['avg_likes']}")
    print(f"Place IDs: {results['place_ids']}")
    print(f"Tweet Times: {results['tweet_times']}")
    print(f"Top User: {results['top_user']}")

if __name__ == "__main__":
    main()