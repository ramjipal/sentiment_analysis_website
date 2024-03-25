from django.shortcuts import render, redirect, HttpResponse
from .sentiment_analysis_code import sentiment_analysis_code
from .youtube_scrapper import *


def sentiment_analysis(request):
    return render(request, 'home/sentiment.html')

def sentiment_analysis_type(request):
    if request.method == 'POST':
        form = request.POST
        analyse = sentiment_analysis_code()
        tweet = form['sentiment_typed_tweet']
        sentiment = analyse.get_tweet_sentiment(tweet)
        args = {'tweet':tweet, 'sentiment':sentiment}
        return render(request, 'home/sentiment_type_result.html', args)

    else:
        return render(request, 'home/sentiment_type.html')

def sentiment_analysis_import(request):
    if request.method == 'POST':
        form = request.POST
        analyse = sentiment_analysis_code()  # a class for sentiment analysis
        video_url = form['sentiment_imported_tweet']
        id  = video_url[-11:]
        list_of_tweets = get_tweets(id)
        list_of_tweets_and_sentiments = []
        print(list_of_tweets_and_sentiments)
        for i in list_of_tweets:
            list_of_tweets_and_sentiments.append((i,analyse.get_tweet_sentiment(i)))
            
        args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':id}
        print(args)
        return render(request, 'home/sentiment_import_result_hashtag.html', args)

    else:
        return render(request, 'home/sentiment_import.html')
