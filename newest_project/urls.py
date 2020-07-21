"""newest_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, re_path
from django.contrib import admin
from newest_project.views import *
from newest_project.forms import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('makepost', PostCreateView.as_view()),
    url('listpost', PostListView.as_view()),
    path('up/<int:pk>/', UpVoteView.as_view()),
    url('form', FillOut.as_view() ),
    url('aboutus', AboutUs.as_view() ),
    # url('', Home.as_view() ),

    # FACE BOOK MAKING A POST

    # url('detailpost/<int:pk>', PostDetailView.as_view()),



]
