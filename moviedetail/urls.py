from . import views
from django.urls import path, include


app_name='moviedetail'

urlpatterns = [
     # path('', views.demo, name='demo'),
     path('add_movie/', views.add_movie, name='add_movie'),
     path('movie_detail/', views.movie_detail, name='movie_detail'),
     path('movie_delete/<int:movie_id>/', views.movie_delete, name='movie_delete'),
     path('movie_update/<int:movie_id>/', views.movie_update, name='movie_update'),
     path('movie_list/', views.movie_list, name='movie_list'),
     path('add_review/<int:movie_id>/', views.add_review, name='add_review'),
]
