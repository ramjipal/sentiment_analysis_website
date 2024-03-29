from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'sentiment'

urlpatterns = [
    url(r'^youtube_sentiment/$', views.youtube_sentiment_analysis, name="sentiment_anaylsis"),
    url(r'^reddit_sentiment/$', views.reddit_sentiment_analysis, name="reddit_sentiment_anaylsis"),
    url(r'^facebook_sentiment/$', views.facebook_sentiment_analysis, name="facebook_sentiment_anaylsis"),
    # url(r'^/$', views.sentiment_analysis, name="sentiment_anaylsis"),
    # url(r'^selectSocial/$', views.sentiment_analysis, name="sentiment_anaylsis"),
    
    url(r'^type/$', views.sentiment_analysis_type, name="sentiment_analysis_type"),
    url(r'^youtube_import/$', views.sentiment_analysis_import, name="sentiment_analysis_import"),
    url(r'^reddit_import/$', views.reddit_sentiment_analysis_import, name="reddit_sentiment_analysis_import"),
    url(r'^facebook_import/$', views.facebook_sentiment_analysis_import, name="facebook_sentiment_analysis_import"),
    
    url(r'^$', views.social_selection, name="social_selection")
    
]