from django.urls import path
from . import views

app_name = 'review_app'

urlpatterns = [
    path('add_review/<int:movie_id>/', views.add_review, name='add_review'),
    path('add_comment/<int:review_id>/', views.add_comment, name='add_comment'),

]