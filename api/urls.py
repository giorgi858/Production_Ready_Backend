from django.urls import path
from .views import  api_home_page, note_detail

app_name = 'api'

urlpatterns=[
    path('notes/', api_home_page, name='api_view'),
    path('notes/<int:pk>/', note_detail, name='api_view_detail'),


]
