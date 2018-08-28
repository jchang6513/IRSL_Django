"""public URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from home.views import home
from intro.views import intro
from news.views import news
from member.views import member
from course.views import course
from publication.views import pub
from achiev.views import achiev
from conference.views import conf
from research.views import research
from link.views import link

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('index/', home, name='home'),
    path('introduction/', intro, name='intro'),
    path('news/', news, name='news'),
    path('member/', member, name='member'),
    path('course/', course, name='course'),
    path('publication/', pub, name='pub'),
    path('achievement/', achiev, name='achiev'),
    path('conference/', conf, name='conf'),
    path('research/', research, name='research'),
    path('link/', link, name='link'),
]

#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
