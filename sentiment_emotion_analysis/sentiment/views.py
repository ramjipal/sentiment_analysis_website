from django.shortcuts import render, redirect, HttpResponse
from .sentiment_analysis_code import *
from . import youtube_scrapper
from . import reddit_scrapper
from . import facebook_scrapper
from django.http import JsonResponse


analyse = sentiment_analysis_code()# a class for sentiment analysis
qclass = QuestinClassifier() # a class for question classification
def youtube_sentiment_analysis(request):
    return render(request, 'home/youtube/sentiment.html')

def reddit_sentiment_analysis(request):
    return render(request, 'home/reddit/sentiment.html')

def facebook_sentiment_analysis(request):
    return render(request, 'home/facebook/sentiment.html')


#-----------------------------------------------------------------

def social_selection(request):
    return render(request, 'home/social_selection.html')

#-----------------------------------------------------------------

def sentiment_analysis_type(request):
    if request.method == 'POST':
        form = request.POST
        comment = form['sentiment_typed_comment']
        sentiment = analyse.get_comment_sentiment(comment)
        args = {'comment':comment, 'sentiment':sentiment}
        return render(request, 'home/youtube/sentiment_type_result.html', args)

    else:
        return render(request, 'home/youtube/sentiment_type.html')
#---------------------------------------------------------------------------

def sentiment_analysis_import(request):
    if request.method == 'POST':
        form = request.POST
        video_url = form['sentiment_imported_comment']
        id  = video_url[-11:]
        list_of_comments = youtube_scrapper.get_comments(id)
        list_of_comments_and_sentiments = []
        # print(list_of_comments_and_sentiments)
        list_of_questions = []
        
        for i in list_of_comments:
            list_of_comments_and_sentiments.append((i,analyse.get_comment_sentiment(i)))
            if qclass.isquestion(i):
                list_of_questions.append(i)
        args = {'list_of_comments_and_sentiments':list_of_comments_and_sentiments,'list_of_questions': list_of_questions, 'handle':id}
        print(args)
        return render(request, 'home/youtube/sentiment_import_result.html', args)

    else:
        return render(request, 'home/youtube/sentiment_import.html')
    

# -------------------------------------------------------------------------  
def reddit_sentiment_analysis_import(request):
    if request.method == 'POST':
        form = request.POST
        post_url = form['reddit_sentiment_imported_comment']
        post_url = str(post_url)
        list_of_comments = reddit_scrapper.get_comments(post_url)
        list_of_comments_and_sentiments = []
        # print(list_of_comments_and_sentiments)
        list_of_questions = []
        
        for i in list_of_comments:
            list_of_comments_and_sentiments.append((i,analyse.get_comment_sentiment(i)))
            if qclass.isquestion(i):
                list_of_questions.append(i)
            
        args = {'list_of_comments_and_sentiments':list_of_comments_and_sentiments,'list_of_questions': list_of_questions ,'handle':post_url}
        return render(request, 'home/reddit/sentiment_import_result.html', args)

    else:
        return render(request, 'home/reddit/sentiment_import.html')
    
#-------------------------------------------------------------------------------- 
def facebook_sentiment_analysis_import(request):
    if request.method == 'POST':
        form = request.POST
        post_url = form.get('facebook_sentiment_imported_comment')
        post_url = str(post_url)
        list_of_comments = facebook_scrapper.get_comments(post_url)
        list_of_comments_and_sentiments = []
        list_of_questions = []
        
        
        for i in list_of_comments:
            list_of_comments_and_sentiments.append((i,analyse.get_comment_sentiment(i)))
            if qclass.isquestion(i):
                list_of_questions.append(i)
            
        args = {'list_of_comments_and_sentiments':list_of_comments_and_sentiments,'list_of_questions': list_of_questions, 'handle':post_url}
        return render(request, 'home/facebook/sentiment_import_result.html', args)

    else:
        return render(request, 'home/facebook/sentiment_import.html')
