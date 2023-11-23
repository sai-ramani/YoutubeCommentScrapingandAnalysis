from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def sentiment_scores(comment, polarity):
    # Creating a SentimentIntensityAnalyzer object.
    sentiment_object = SentimentIntensityAnalyzer()

    sentiment_dict = sentiment_object.polarity_scores(comment)
    polarity.append(sentiment_dict['compound'])

    return polarity

def analyze():
    polarity = []
    positive_comments = []
    negative_comments = []
    neutral_comments = []

    f = open("youtubecomments.txt", 'r', encoding='`utf-8')
    comments = f.readlines()
    f.close()
    for index, items in enumerate(comments):
        polarity = sentiment_scores(items, polarity)

        if polarity[-1] > 0.05:
            positive_comments.append(items)
        elif polarity[-1] < -0.05:
            negative_comments.append(items)
        else:
            neutral_comments.append(items)
    avg_polarity = sum(polarity) / len(polarity)
    result = ""
    if avg_polarity > 0.05:
        result = "The Video has got a Positive response"
    elif avg_polarity < -0.05:
        result = "The Video has got a Negative response"
    else:
        result = "The Video has got a Neutral response"
    return result, positive_comments, negative_comments, neutral_comments
