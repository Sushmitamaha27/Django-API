from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import MovieListAV,Movie_detailAV

urlpatterns=[
    path('list/',MovieListAV.as_view(),name='MovieListAV'),
    path('<int:pk>',Movie_detailAV.as_view(),name='Movie-detailAV')
]