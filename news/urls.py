from django.conf.urls import url
from . import views

urlpatterns = [
    url('',views.news_page, name='news_page')
]
