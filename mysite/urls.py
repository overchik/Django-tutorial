
from django.contrib import admin
from django.urls import path 
from django.conf.urls import url, include

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls'))
]
