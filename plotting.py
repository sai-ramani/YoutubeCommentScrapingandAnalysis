import matplotlib.pyplot as plt
def plot(positive_comments,negative_comments,neutral_comments):
    positive_count = len(positive_comments)
    negative_count = len(negative_comments)
    neutral_count = len(neutral_comments)

    # labels and data for Bar chart
    labels = ['Positive', 'Negative', 'Neutral']
    comment_counts = [positive_count, negative_count, neutral_count]

    # Creating bar chart
    plt.bar(labels, comment_counts, color=['blue', 'red', 'grey'])

    # Adding labels and title to the plot
    plt.xlabel('Sentiment')
    plt.ylabel('Comment Count')
    plt.title('Sentiment Analysis of Comments')
    plt.savefig('static/Image/bar_image.png')

    plt.clf()
    # plotting pie chart
    plt.pie(comment_counts, labels=labels)
    plt.savefig('static/Image/pie_image.png')