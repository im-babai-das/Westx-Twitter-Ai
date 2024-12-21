import openai
import tweepy
import os

# Set up OpenAI API credentials
openai.api_key = "your_openai_api_key"

# Set up Twitter API credentials
twitter_api_key = "your_twitter_api_key"
twitter_api_secret = "your_twitter_api_secret"
twitter_access_token = "your_access_token"
twitter_access_token_secret = "your_access_token_secret"

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(
    twitter_api_key,
    twitter_api_secret,
    twitter_access_token,
    twitter_access_token_secret
)
twitter_api = tweepy.API(auth)

# Function to generate AI-based tweets
def generate_tweet():
    prompt = "Generate a creative and engaging tweet about AI advancements:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    tweet_content = response.choices[0].text.strip()
    return tweet_content

# Function to post tweet on Twitter
def post_tweet(content):
    try:
        twitter_api.update_status(content)
        print("Tweet posted successfully:", content)
    except tweepy.TweepError as e:
        print("Failed to post tweet:", e)

if __name__ == "__main__":
    # Generate a tweet
    tweet = generate_tweet()
    print("Generated Tweet:", tweet)

    # Post the tweet
    post_tweet(tweet)
