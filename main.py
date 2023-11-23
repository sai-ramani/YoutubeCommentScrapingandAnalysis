from flask import Flask, render_template, request
from googleapiclient.discovery import build
import preprocessing_comments, sentiment_analysis, plotting

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/scrap', methods = ['POST'])
def scrap_comments():
    url = request.form.get('youtube url')
    API_KEY = 'AIzaSyC1Vm_VH89CJq5wh257XWhbFHdbxsenZd0'
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    video_id = url[-11:]
    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()
    video_snippet = video_response['items'][0]['snippet']
    uploader_channel_id = video_snippet['channelId']

    comments = []
    nextPageToken = None
    while len(comments) < 600:
        req = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            pageToken=nextPageToken
        )
        response = req.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            # Check if the comment is not from the video uploader
            if comment['authorChannelId']['value'] != uploader_channel_id:
                comments.append(comment['textDisplay'])
        nextPageToken = response.get('nextPageToken')

        if not nextPageToken:
            break

    #preprocessing and storing the comments in a text file
    f = open("youtubecomments.txt", 'w', encoding='utf-8')
    preprocessing_comments.store(comments,f)

    #sentiment analysis on comments
    result, positive_comments, negative_comments, neutral_comments = sentiment_analysis.analyze()

    #grpahical representation of frequencies
    plotting.plot(positive_comments, negative_comments, neutral_comments)

    after_complete_message = "Your file is ready and sent to your mail id"

    return render_template('index.html',after_complete_message=after_complete_message,result = result,pcomments = positive_comments,ncomments=negative_comments, neucomments = neutral_comments)

if __name__ == "__main__":
    app.run()
