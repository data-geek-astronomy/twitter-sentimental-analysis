import tweepy
import re
import matplotlib.pyplot as plt
from textblob import TextBlob

class TwitterSentimentAnalyzer:
    def __init__(self):
        self.collected_tweets = []

    def fetch_and_analyze_tweets(self):
        # Twitter API Authentication
        consumer_key = 'your key here'
        consumer_secret = 'your key here'
        access_token = 'your key here'
        access_token_secret = 'your key here'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # User Input
        search_query = input("Enter Keyword/Tag to search about: ")
        tweet_count = int(input("Enter number of tweets to analyze: "))

        # Fetch Tweets
        self.collected_tweets = tweepy.Cursor(api.search, q=search_query, lang="en").items(tweet_count)

        # Analyze Tweets
        self.perform_sentiment_analysis(search_query, tweet_count)

    def perform_sentiment_analysis(self, search_query, tweet_count):
        sentiment_counts = {'neutral': 0, 'weak_positive': 0, 'positive': 0, 'strong_positive': 0,
                            'weak_negative': 0, 'negative': 0, 'strong_negative': 0}
        total_polarity = 0

        for tweet in self.collected_tweets:
            cleaned_tweet = self.clean_tweet(tweet.text)
            sentiment_score = TextBlob(cleaned_tweet).sentiment.polarity
            total_polarity += sentiment_score

            # Categorize sentiments
            if sentiment_score == 0:
                sentiment_counts['neutral'] += 1
            elif 0 < sentiment_score <= 0.3:
                sentiment_counts['weak_positive'] += 1
            elif 0.3 < sentiment_score <= 0.6:
                sentiment_counts['positive'] += 1
            elif 0.6 < sentiment_score <= 1:
                sentiment_counts['strong_positive'] += 1
            elif -0.3 < sentiment_score <= 0:
                sentiment_counts['weak_negative'] += 1
            elif -0.6 < sentiment_score <= -0.3:
                sentiment_counts['negative'] += 1
            elif -1 <= sentiment_score <= -0.6:
                sentiment_counts['strong_negative'] += 1

        # Calculate percentages
        for key in sentiment_counts:
            sentiment_counts[key] = self.calculate_percentage(sentiment_counts[key], tweet_count)

        # Display and plot results
        self.display_results(sentiment_counts, search_query, tweet_count)
        self.plot_results(sentiment_counts, search_query, tweet_count)

        average_polarity = total_polarity / tweet_count
        print(f"\nAverage sentiment polarity: {average_polarity:.2f}")

    @staticmethod
    def clean_tweet(tweet):
        # Remove URLs, mentions, hashtags, and special characters
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    @staticmethod
    def calculate_percentage(part, whole):
        return 100 * float(part) / float(whole)

    def display_results(self, sentiment_counts, search_query, tweet_count):
        print(f"\nAnalysis of {tweet_count} tweets about '{search_query}':")
        for sentiment, count in sentiment_counts.items():
            print(f"{sentiment.replace('_', ' ').title()}: {count}%")

    def plot_results(self, sentiment_counts, search_query, tweet_count):
        labels = [f"{key.replace('_', ' ').title()} [{value}%]" for key, value in sentiment_counts.items()]
        sizes = [value for value in sentiment_counts.values()]
        colors = ['gold', 'yellowgreen', 'lightgreen', 'darkgreen', 'lightcoral', 'red', 'darkred']
        plt.pie(sizes, labels=labels, colors=colors, startangle=90)
        plt.title(f"Sentiment Analysis of {tweet_count} Tweets about '{search_query}'")
        plt.axis('equal')
        plt.show()

if __name__ == "__main__":
    analyzer = TwitterSentimentAnalyzer()
    analyzer.fetch_and_analyze_tweets()
