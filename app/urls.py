from django.urls import path
from .views import PostsView, TestsView, ImageView, ImageNewView, GetModelsView
from . import views

app_name = "predict"

urlpatterns = [
    path('posts/',PostsView.as_view(), name='posts_view'),
    path('tests/',TestsView.as_view(), name='tests_view'),
    #path('image/',ImageView.as_view(), name='image_view'),
    path('image/',ImageNewView.as_view(), name='imagenew_view'),
    path('getmodels/',GetModelsView.as_view(), name='imagenew_view'),
    path('files/', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('uploadmodel/', views.uploadmodel, name='uploadmodel'),
    
]

