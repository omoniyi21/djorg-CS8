"""djorg URL Configuration

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
from django.conf.urls import url, include, re_path
from rest_framework import routers, serializers, viewsets
from notes.api import NoteViewSet
# from bookmarks.api import BookmarkViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
# router.register(r'personal_notes', PersonalNoteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls), 
    # path('bookmarks/', include('bookmarks.urls')),
    # url(r'^api-auth/', include('rest_framework.urls')),
    path(r'api/', include(router.urls)),
    re_path(r'^api-token-auth/', views.obtain_auth_token)
]
