from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
# import twitter_credentials
 
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    # """
    # Class for streaming and processing live tweets.
    # """
    def stream_tweets(self, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler("Pm2M0lzSIBXLnPEPyIEKZl6nw", "gRvMPQS1H7LF5hgjid8oCU8UUMkL6KvemDpyLyqKAN1jnZa7Q2")
        auth.set_access_token("2850680649-7djq6wABayGpthiGep3ciWvjiCNxoezj0eqM65U", "dzc1oz3j873sxAqtadhRtu93t4VizzcW9vipOLf6C70qP")
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    # """
    # This is a basic listener that just prints received tweets to stdout.
    # """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open('tweets.json', 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["qwdfc3"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(hash_tag_list)