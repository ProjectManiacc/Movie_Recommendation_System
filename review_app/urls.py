from django.urls import path
from . import views

app_name = 'review_app'

urlpatterns = [
    path('add_review/<int:movie_id>/', views.add_review, name='add_review'),

]