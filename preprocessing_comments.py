import re
def process(comments):
    from cleantext import clean
    relevant_comments = []
    for text in comments:
        string = re.sub(r'http\S+', '', text, flags=re.MULTILINE)
        relevant_comments.append(clean(string, no_emoji=True))
    return relevant_comments

def store(comments,f):
    relevant_comments = process(comments)
    for idx, comment in enumerate(relevant_comments):
        f.write(str(comment) + "\n")
    f.close()