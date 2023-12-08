from django.urls import path 

from . import views 

app_name='core'
urlpatterns = [
    path('', views.core_engine, name="home"),
    path('upload-file/',views.upload_file,name="upload-file"),
    path('search/',views.search_user,name="search"),
    path('share_file/<str:file_id>/',views.share_file,name="share_file"),
]
