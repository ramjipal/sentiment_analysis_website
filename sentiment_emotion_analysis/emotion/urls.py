from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'emotion'

urlpatterns = [
    url(r'^youtube_emotion/$', views.youtube_emotion_analysis, name="emotion_anaylsis"),
    url(r'^reddit_emotion/$', views.reddit_emotion_analysis, name="reddit_emotion_anaylsis"),
    url(r'^facebook_emotion/$', views.facebook_emotion_analysis, name="facebook_emotion_anaylsis"),
    # url(r'^/$', views.emotion_analysis, name="emotion_anaylsis"),
    # url(r'^selectSocial/$', views.emotion_analysis, name="emotion_anaylsis"),
    
    url(r'^type/$', views.emotion_analysis_type, name="emotion_analysis_type"),
    url(r'^youtube_import/$', views.emotion_analysis_import, name="emotion_analysis_import"),
    url(r'^reddit_import/$', views.reddit_emotion_analysis_import, name="reddit_emotion_analysis_import"),
    url(r'^facebook_import/$', views.facebook_emotion_analysis_import, name="facebook_emotion_analysis_import"),
    
    url(r'^$', views.social_selection, name="social_selection")
]