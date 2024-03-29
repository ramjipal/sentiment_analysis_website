from django.shortcuts import render, redirect, HttpResponse
from .emotion_analysis_code import emotion_analysis_code
from . import youtube_scrapper, reddit_scrapper, facebook_scrapper


def social_selection(request):
    print("____________*********************___________________________")
    
    return render(request, 'emotion_home/social_selection.html')

def youtube_emotion_analysis(request):
    return render(request, 'emotion_home/youtube/emotion.html')

def reddit_emotion_analysis(request):
    return render(request, 'emotion_home/reddit/emotion.html')

def facebook_emotion_analysis(request):
    return render(request, 'emotion_home/facebook/emotion.html')

def emotion_analysis_type(request):
    if request.method == 'POST':
        form = request.POST
        analyse = emotion_analysis_code()
        comment = form.get('emotion_typed_comment')
        emotion = analyse.get_comment_emotion(comment)
        args = {'comment':comment, 'emotion':emotion}
        return render(request, 'emotion_home/emotion_type_result.html', args)

    else:
        return render(request, 'emotion_home/emotion_type.html')

def emotion_analysis_import(request):
    if request.method == 'POST':
        form = request.POST
        analyse = emotion_analysis_code()  # a class for emotion analysis
        video_url = form['emotion_imported_comment']
        id  = video_url[-11:]
        list_of_comments = youtube_scrapper.get_comments(id)
        list_of_comments_and_emotions = []
        for i in list_of_comments:
            list_of_comments_and_emotions.append((i,analyse.get_comment_emotion(i)))
            args = {'list_of_comments_and_emotions': list_of_comments_and_emotions, 'handle': id}
            return render(request, 'emotion_home/youtube/emotion_import_result.html', args)

    else:
        return render(request, 'emotion_home/youtube/emotion_import.html')
    
    
def reddit_emotion_analysis_import(request):
    if request.method == 'POST':
        form = request.POST
        analyse = emotion_analysis_code()  # a class for emotion analysis
        post_url = form['reddit_emotion_imported_comment']
        post_url = str(post_url)
        list_of_comments = reddit_scrapper.get_comments(post_url)
        list_of_comments_and_emotions = []
        for i in list_of_comments:
            list_of_comments_and_emotions.append((i,analyse.get_comment_emotion(i)))
            
        args = {'list_of_comments_and_emotions':list_of_comments_and_emotions, 'handle':post_url}
        return render(request, 'emotion_home/reddit/emotion_import_result.html', args)

    else:
        return render(request, 'emotion_home/reddit/emotion_import.html')
    
def facebook_emotion_analysis_import(request):
    if request.method == 'POST':
        form = request.POST
        analyse = emotion_analysis_code()  # a class for emotion analysis
        post_url = form.get('facebook_emotion_imported_comment')
        post_url = str(post_url)
        list_of_comments = facebook_scrapper.get_comments(post_url)
        list_of_comments_and_emotions = []
        for i in list_of_comments:
            list_of_comments_and_emotions.append((i,analyse.get_comment_emotion(i)))
            
        args = {'list_of_comments_and_emotions':list_of_comments_and_emotions, 'handle':post_url}
        return render(request, 'emotion_home/facebook/emotion_import_result.html', args)

    else:
        return render(request, 'emotion_home/facebook/emotion_import.html')