from django.urls import path
from . import views

urlpatterns = [
    path("movies/", views.index, name="index"),
    path("movies/explora/", views.discover_view, name="discover_view"),
    path("movies/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("movies/<int:movie_id>/review/submit/", views.movie_review, name="movie_review"),
    path("movies/your_name/", views.get_name, name="get_name"),
    path('movies/inicia_sesion/', views.login_view, name='login_view'),
    path('movies/cerrar_sesion/', views.logout_view, name='logout_view'),
    path('movies/usuario/<int:user_id>', views.user_view, name='user_view'),
    path("movies/actor/<int:actor_id>/", views.actor_detail, name="actor_detail"),
]

