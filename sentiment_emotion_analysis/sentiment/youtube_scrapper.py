from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import numpy as np
import pandas as pd
import re
import googleapiclient.discovery
import emoji


api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyB8J4Di6LgMd82lMgcg-GTnoYuNIj1syKo"
# DEVELOPER_KEY = "AIzaSyAu57QsQ1d8d_Mb0YAzxEtyPgofPOsHuLc"
 
youtube = googleapiclient.discovery.build(
api_service_name, api_version, developerKey=DEVELOPER_KEY)


def get_comments(id):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=id,
        maxResults=100
    )
    response = request.execute()
    comments = []
    threshold_ratio = 0.65
    hyperlink_pattern = r'https?://\S+'
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        user_comment = comment['textDisplay']
        user_comment = re.sub("<br>", "", user_comment) #removing line break
        user_comment = re.sub(hyperlink_pattern, "", user_comment) #removing line break
        user_comment = user_comment.lower().strip() #removing extra spaces
        emojis = emoji.emoji_count(user_comment)
        text_characters = len(re.sub(r'\s', '', user_comment))
        if (any(char.isalnum() for char in user_comment)):
            if emojis == 0 or (text_characters/(text_characters + emojis))> threshold_ratio:
                comments.append([
                comment['authorDisplayName'],
                comment['textDisplay']
                ])

    df = pd.DataFrame(comments, columns=['author','text'])
    # author_name = "@analyticswithadam"
    # df = df.loc[df['author']!=author_name]
    comment_list = list(df['text'])
    question_list = []
    clean_comment_list = []
    pattern = r"&#\d+;?;"
    for comment in comment_list:
        comment = re.sub(pattern, "", comment)
        clean_comment_list.append(comment)
    return list(clean_comment_list)


if __name__ == "__main__":
    print(get_comments("lm5EiwiGtw0"))


	