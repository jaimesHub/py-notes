tweet = input("enter your tweet: ")
tweet_length = len(tweet)

if tweet_length < 140:
    print(f"That {tweet_length} char tweet will work!")
else:
    print(f"Your {tweet_length} char twee is {tweet_length - 140} chars too long")