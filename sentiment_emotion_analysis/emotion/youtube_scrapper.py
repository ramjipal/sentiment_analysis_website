from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import numpy as np
import pandas as pd
import re
import googleapiclient.discovery

     
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBSQrPvc6GCAqxC1epuW-YV_jvdjYQ2msw"
 
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

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([
            comment['authorDisplayName'],
            comment['textDisplay']
        ])

    df = pd.DataFrame(comments, columns=['author','text'])
    # author_name = "@analyticswithadam"
    # df = df.loc[df['author']!=author_name]
    comment_list = list(df['text'])
    question_list = []
    another_list = []
    pattern = r"&#\d+;?;"
    for comment in comment_list:
        comment = re.sub(pattern, "", comment)
        if "?" in comment:
            question_list.append(comment)
        else:
            another_list.append(comment)
    return another_list


	